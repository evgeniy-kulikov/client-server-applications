"""
Функции приема и передачи сообщения. Используются сервером и клиентом
"""

import json
from common.variables import MAX_PACKAGE_LENGTH
from decorators import log


@log
def get_message(client):  # Внимание! в качестве агумента "client" подается объект СОКЕТ
    """
    Функция приема и декодирования сообщения.
    Входные данные - байты, выходные данные - словарь.
    Если на входе/выходе другие данные - возвращается ValueError (тип ошибки)
    :param client:
    :return:
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)  # полученное сообщение от клиента
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode('utf-8')  # если на входе байты, то декодируем
        if isinstance(json_response, str):
            response = json.loads(json_response)  # если тип полученного строка - загружаем ее
            if isinstance(response, dict):
                return response  # если "response" словарь, то возвращаем его
                # иначе - ошибки!
            raise ValueError('json объект не является типом "dict"')
        raise ValueError('Результат декодирования не является типом "str"')
    raise ValueError('Полученное сообщение не является типом "bytes"')


@log
def send_message(sock, message):
    """
    Функция отправки сообщения.
    Принимает для отправки тип "dict", получает из него строку, кодирует в байты и отправляет.
    :param sock:
    :param message:
    :return:
    """
    if not isinstance(message, dict):  # проверка что на вход подан тип данных "dict"
        raise TypeError(' Сообщение не является типом "dict"')
    json_message = json.dumps(message)  # переводим словарь в строку
    encoded_message = json_message.encode('utf-8')
    sock.send(encoded_message)  # отправляем закодированное сообщение
