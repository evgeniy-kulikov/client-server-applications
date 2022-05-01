import sys
import os
import unittest
import json
sys.path.insert(0, os.path.join(os.getcwd(), '..'))  # добавление в скрипт модулей расположенных не в корне проекта
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, MAX_PACKAGE_LENGTH
from common.utils import get_message, send_message

# print(sys.path)


class TestSocket:
    """
    Класс имитирующий реальный сокет, для возможности приема и передачи сообщений
    """
    def __init__(self, test_dict):
        self.max_package_length = MAX_PACKAGE_LENGTH
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):  # аргумент "message_to_send" это то что отправляем в сокет (метод класса)
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode('utf-8')
        self.received_message = message_to_send

    def recv(self, max_package_length=1024):  # прием данных (метод класса) max_package_length - аргумент "пустышка"
        # т.к. данный метод сокета дплжен иметь два аргумента
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
        """
        Тестируем корректность работы функции отправуи сообщения " send_message() "
        Для этого создаем тестовый сокет и проверяем корректность отправки сообщения (словаря)
        :return:
        """
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_false(self):
        """
        Тестируем корректность работы функции отправуи сообщения " send_message() "
        Для этого создаем тестовый сокет и проверяем возникновение ошибки
        :return:
        """
        # экземпляр класса " TestSocket " содержит тестовый словарь " test_dict_send "
        test_socket = TestSocket(self.test_dict_send)
        # Вызов тестируемой функции " send_message() ". Результаты будут сохранены в экземпляре класса " TestSocket "
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, 'incorrect dictionary')

    def test_get_message_true(self):
        """
        Тест функции приема сообщения
        Случай верного декодирования сообщения (код успеха RESPONSE: 200)
        :return:
        """
        test_socked_true = TestSocket(self.test_dict_receive_good)
        self.assertEqual(get_message(test_socked_true), self.test_dict_receive_good)

    def test_get_message_false(self):
        """
        Тест функции приема сообщения
        Случай верного декодирования сообщения (код ошибки RESPONSE: 400)
        :return:
        """
        test_socked_false = TestSocket(self.test_dict_receive_bed)
        self.assertEqual(get_message(test_socked_false), self.test_dict_receive_bed)


if __name__ == '__main__':
    unittest.main()
