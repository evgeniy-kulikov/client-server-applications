import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.getcwd(), '..'))  # добавление в скрипт модулей расположенных не в корне проекта
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_answer, setup_ip_port



class TestClient(unittest.TestCase):
    """
    Тест проверки функций клиента
    """

    def test__create_presence(self):
        """
        Тест успешной процедуры запроса
        :return
        """
        test = create_presence()
        test[TIME] = 1650953345.1  # для реализации теста - время константа
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1650953345.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test__process_answer_200(self):
        """
        Тест, когда значение ключа RESPONSE равно 200 (успешный запрос)
        :return:
        """
        self.assertEqual(process_answer({RESPONSE: 200}), 'code 200 : OK')

    def test__process_answer_400(self):
        """
        Тест, когда значение ключа RESPONSE равно 400 (ошибка запроса)
        :return:
        """
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), 'code 400 : Bad Request')

    def test__process_answer_no_response(self):
        """
        Тест возникновения исключения (нет ключа RESPONSE)
        :return:
        """
        self.assertRaises(ValueError, process_answer, {ERROR: ''})

    def test___setup_ip_port__ip(self):
        """
        Тест получения IP адреса для приема сервером клиента по умолчанию
        :return:
        """
        ip_port = setup_ip_port()
        self.assertEqual(ip_port[0], '127.0.0.1')

    def test___setup_ip_port__port(self):
        """
        Тест получения адрес порта для приема сервером клиента по умолчанию
        :return:
        """
        ip_port = setup_ip_port()
        self.assertEqual(ip_port[1], 7777)


if __name__ == '__main__':
    unittest.main()
