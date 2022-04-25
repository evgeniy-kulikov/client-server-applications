""" Сторона клиента """

import json
import socket
import sys
import time
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, ACTION, TIME, \
    USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):
    """
    Функция формирующая сервисное сообщение серверу о своем присутствии.
    Тип сообщения - словарь. Работа с JIM протоколом.
    :param account_name:
    :return:
    """
    # формируем структуру словаря для сообщения
    user_presence = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return user_presence


def process_answer(message):  # обработка сообщения
    """
    Функция анализа ответа сервера (коды ошибок HTTP которые использует JIM-протокол)
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:  # Успешное завершение обработки
            return 'Код ответа сервера - code 200 : OK'
        return f'code 400 : {message[ERROR]}'  # ошибка запроса (сторона клиента)
    raise ValueError


def main_client():
    """
    Функция загрузки параметров командной строки
    :return:
    """
    try:
        server_address = sys.argv[1]  # загрузка второго параметра командной строки - IP адрес
        server_port = int(sys.argv[2])  # загрузка третьего параметра командной строки - номер порта
        print(f'IP адрес сервера: {server_address} Порт сервера: {server_port} (значения взяты из командной строки)\n')
        if server_port < 1024 or server_port > 65535:  # проверка корретности диапазона
            raise ValueError
    except IndexError:  # установка значений по умолчанию
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        print(f'IP адрес сервера: {server_address} Порт сервера: {server_port} (значения взяты по умолчанию)\n')
    except ValueError:
        print('Номер порта должен соответствовать диапазону от 1024 до 65535')
        sys.exit(1)

    # активация сокета, обмен сообщениями
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message_to_server = create_presence()  # текст сообщение серверу (тип: словарь)
    print(f'Сообщение серверу от клиента: {message_to_server}')
    send_message(client_socket, message_to_server)  # функция отправки сообщения
    try:
        answer = process_answer(get_message(client_socket))
        print(f'Код ответа от сервера для клиента (принято сообщение или нет): {answer}')
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера')


if __name__ == '__main__':
    main_client()
