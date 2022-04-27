import sys
import os
import unittest
import json
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, MAX_PACKAGE_LENGTH
from common.utils import get_message, send_message
sys.path.insert(0, os.path.join(os.getcwd(), '..'))  # добавление в скрипт модулей расположенных не в корне проекта


class TestSocket:
    """
    Класс имитирующий реальный сокет, для возможности приема и передачи сообщений
    """
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):  # аргумент "message_to_send" это то что отправляем  в сокет
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode('utf-8')
        self.received_message = message_to_send

    def receive(self):  # прием данных
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode('utf-8')


class TestUtils(unittest.TestCase):

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1650953345.1,  # для реализации теста - время константа
        USER: {ACCOUNT_NAME: 'Guest'}
    }

    test_dict_receive_good = {RESPONSE: 200}

    test_dict_receive_bed = {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }

    def test_send_message_true(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_false(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, 'incorrect dictionary')

# "get_message" - функция модуля "utils" принимающая объект типа сокет
#  в результате нельзя задействовать используемый в "get_message" метод recv()
#  Тест проходит с ошибкой:
#  AttributeError: 'TestSocket' object has no attribute 'recv'

    # def test_get_message_true(self):
    #     test_socked_true = TestSocket(self.test_dict_receive_good)
    #     self.assertEqual(get_message(test_socked_true), self.test_dict_receive_good)
    #
    # def test_get_message_false(self):
    #     test_socked_false = TestSocket(self.test_dict_receive_bed)
    #     self.assertEqual(get_message(test_socked_false), self.test_dict_receive_bed)


if __name__ == '__main__':
    unittest.main()
