""" Сторона сервера """

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message


def client_message_processing(message):
    """
    Функция проверки сообщения от клиента. Работа с JIM — протоколом.
    На входе словарь (проверка корректности данных в функции "get_message")
    Производится проверка коректности значений ключей словаря.
    Возвращаемые данные (отчет проверки) - словарь
    :param message:
    :return:
    """
    if ACTION in message and message[ACTION] == PRESENCE \
            and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }


def setup_port():
    """
    Загрузка параметров командной строки. Если параметров нет, то берутся значения по умолчанию.
    server.py -p 8888 -a 127.0.0.1
    :return:
    """

    # Проверяем коректность загрузки номера порта
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            print(f'Порт сервера: {listen_port} (значение взято из командной строки)')
        else:
            listen_port = DEFAULT_PORT
            print(f'Порт сервера по умолчанию: {listen_port}')

    except ValueError:
        print('После параметра "-p" нужно указать номер порта')
        sys.exit(1)

    # Проверка диапазона значений номера порта
    try:
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except ValueError:
        print('Номер порта должен соответствовать диапазону от 1024 до 65535')
        sys.exit(1)
    return listen_port


def setup_ip():
    """
    Загрузка параметров командной строки. Если параметров нет, то берутся значения по умолчанию.
    server.py -p 8888 -a 127.0.0.1
    :return:
    """
    # Проверка коректности IP адреса.
    try:
        if '-a' in sys.argv:
            listen_ip_address = sys.argv[sys.argv.index('-a') + 1]
            print(f'IP адрес для приема сервером клиента: {listen_ip_address} (значение взято из командной строки)')
        else:
            listen_ip_address = ''  # сервер будет принимать клиента с любого адреса
            print(f'IP адрес для приема сервером клиента: "" (любой адрес)')

    except IndexError:
        print('После параметра "-a" необходимо указать IP адрес, через который будет слушать сервер')
        sys.exit(1)
    return listen_ip_address


def main_server():
    """
    Запуск серверной части
    :return:
    """
    listen_ip_address = setup_ip()
    listen_port = setup_port()

    # запускаем сокет сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((listen_ip_address, listen_port))

    # прослушиваем порт
    server_socket.listen(MAX_CONNECTIONS)
    print(f'Сервер готов принять клиента по адресу: {listen_ip_address} (если пусто - любой адрес)\n')

    while True:
        client, client_ip_address = server_socket.accept()
        try:
            message_from_client = get_message(client)
            print(f'Получено сообщение от клиента: {message_from_client}\n')
            response = client_message_processing(message_from_client)
            print(f'Код корректности приема сообщения от клиента: {response}\n')
            send_message(client, response)

            client.close()
            print('Соединение с клиентом закрыто')
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение клиента')
            client.close()
            print('Соединение с клиентом закрыто (ошибка приема сообщения)')


if __name__ == '__main__':
    main_server()
