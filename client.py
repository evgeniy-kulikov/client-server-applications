""" Сторона клиента """

import json
import socket
import sys
import time
import logging
import logs.client_log_config
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, ACTION, TIME, \
    USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR
from common.utils import get_message, send_message

# прописывание логера-конфига для клиентской части
logger_client = logging.getLogger('client')


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
    logger_client.debug(f'Запись сообщения "{PRESENCE}" для сервера от пользователя: {account_name}')
    return user_presence


def process_answer(message):  # обработка сообщения
    """
    Функция анализа ответа сервера (коды ошибок HTTP которые использует JIM-протокол)
    :param message:
    :return:
    """
    # logger_client.debug(f'Ответ сервера клиенту: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:  # Успешное завершение обработки
            logger_client.debug(f'Ответ сервера клиенту: {message}')
            return 'code 200 : OK'
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
        logger_client.info(
            f'IP адрес сервера:{server_address} Порт сервера: {server_port} (значения взяты из командной строки)')
        # проверка корретности диапазона порта сервера
        if server_port < 1024 or server_port > 65535:
            logger_client.critical(f'Клиент запустился с номером порта: {server_port} '
                                   f'не входящий в допустимый диапазон. Клиент остановлен')
            sys.exit(1)
            # raise ValueError
    except IndexError:  # установка значений по умолчанию
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        logger_client.info(
            f'Запуск клиента со значениями - адрес сервера: {server_address}, порт сервера: {server_port}')
    except ValueError:
        logger_client.critical('Номер порта должен соответствовать диапазону от 1024 до 65535')
        # print('Номер порта должен соответствовать диапазону от 1024 до 65535')
        logger_client.critical('Клиент закрыт')
        sys.exit(1)
        # logger_client.critical('лиент закрыт')

    # активация сокета, обмен сообщениями
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_address, server_port))
    except ConnectionRefusedError:
        logger_client.critical(f'Не удалось соединиться с сервером {server_address} : {server_port} '
                               f'(конечный компьютер отверг запрос на соединение)')
    message_to_server = create_presence()  # текст сообщение серверу (тип: словарь)
    logger_client.info(f'Отправка сообщения серверу от клиента: {message_to_server}')
    send_message(client_socket, message_to_server)  # функция отправки сообщения
    try:
        answer = process_answer(get_message(client_socket))
        logger_client.info(f'Код ответа от сервера для клиента: {answer}')
    except json.JSONDecodeError:
        logger_client.error(f'Не удалось декодировать JSON сообщение сервера')
    except ConnectionRefusedError:
        logger_client.critical(f'Не удалось соединиться с сервером {server_address} : {server_port} '
                               f'(конечный компьютер отверг запрос на соединение)')


if __name__ == '__main__':
    main_client()
