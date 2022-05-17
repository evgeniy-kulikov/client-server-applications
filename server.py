""" Сторона сервера """

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message
import logging
from logs import server_log_config
from decorators import log

# прописывание логера-конфига для серверной части
logger_server = logging.getLogger('server')


def client_message_processing(message):
    """
    Функция проверки сообщения от клиента. Работа с JIM — протоколом.
    На входе словарь (проверка корректности данных в функции "get_message")
    Производится проверка коректности значений ключей словаря.
    Возвращаемые данные (отчет проверки) - словарь
    :param message:
    :return:
    """
    logger_server.debug(f'Оценка принятого сообщения от клиента: {message[USER][ACCOUNT_NAME]}')
    if ACTION in message and message[ACTION] == PRESENCE \
            and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }


@log
def main_server():
    """
    Загрузка параметров командной строки. Если параметров нет, то берутся значения по умолчанию.
    server.py -p 8888 -a 127.0.0.1
    :return:
    """

    # Проверяем коректность загрузки номера порта
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            logger_server.info(f'Порт сервера: {listen_port} (значение взято из командной строки)')
        else:
            listen_port = DEFAULT_PORT
            logger_server.info(f'Порт сервера по умолчанию: {listen_port}')
    except ValueError:
        logger_server.critical('После параметра "-p" нужно указать номер порта. Сервер остановлен')
        sys.exit(1)
    # Проверка правильности диапазона значений номера порта
    if not 1023 < listen_port < 65536:
        logger_server.critical(f'Сервер был запущен с неверным номером порта для подключения: {listen_port} '
                               f'Сервер остановлен')
        sys.exit(1)

    # Проверка коректности IP адреса.
    try:
        if '-a' in sys.argv:
            listen_ip_address = sys.argv[sys.argv.index('-a') + 1]
            logger_server.info(f'IP адрес для приема сервером клиента: {listen_ip_address} '
                               f'(значение взято из командной строки)')
        else:
            listen_ip_address = ''  # сервер будет принимать клиента с любого адреса
            logger_server.info(f'IP адрес для приема сервером клиента: "" (любой адрес). '
                               f'Используется значение по умолчанию')
    except IndexError:
        logger_server.critical('После параметра "-a" необходимо указать IP адрес, через который будет слушать сервер.')
        sys.exit(1)

    # запускаем сокет сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((listen_ip_address, listen_port))

    # прослушиваем порт
    server_socket.listen(MAX_CONNECTIONS)
    logger_server.debug(f'Сервер готов принять клиента по адресу: {listen_ip_address} (если пусто - любой адрес)')

    while True:
        client, client_ip_address = server_socket.accept()
        logger_server.info(f'Установлено соединение с удаленным клиентом: {client_ip_address}')
        try:
            message_from_client = get_message(client)
            logger_server.debug(f'Получено сообщение от клиента: {message_from_client}')
            response = client_message_processing(message_from_client)
            logger_server.info(f'Код корректности приема сообщения от клиента: {response}')
            send_message(client, response)
            client.close()
            logger_server.info(f'Соединение с клиентом: {client_ip_address} закрыто')
        except json.JSONDecodeError:
            logger_server.error(f'Принято некорректное сообщение клиента: {client_ip_address}. Соединение закрыто')
            client.close()


if __name__ == '__main__':
    main_server()
