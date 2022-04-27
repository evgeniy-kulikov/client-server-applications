import unittest
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, \
    PRESENCE, TIME, USER, ERROR
from server import client_message_processing, setup_ip, setup_port


class TestServer(unittest.TestCase):
    """
    Тест проверки функций сервера
    """
    good_dict = {RESPONSE: 200}  # верная структура словоря
    # структура словаря содержит ошибки
    error_dict = {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }

    def test_def_client_message_processing_response__200(self):
        """
        Тест верного получения структуры словаря (сообщения) сервером от клиента
        :return:
        """
        self.assertEqual(client_message_processing(
            {
                ACTION: PRESENCE,
                TIME: 1650953345.1,  # для реализации теста - время константа
                USER: {ACCOUNT_NAME: 'Guest'}
            }
        ), self.good_dict)

    def test_def_client_message_processing_response__no_action(self):
        """
        Тест некорректного получения структуры словаря (сообщения) сервером от клиента:
        отсутствует ключ ACTION
        :return:
        """
        self.assertEqual(client_message_processing(
            {
                TIME: 1650953345.1,  # для реализации теста - время константа
                USER: {ACCOUNT_NAME: 'Guest'}
            }
        ), self.error_dict)

    def test_def_client_message_processing_response__action_bed(self):
        """
        Тест некорректного получения структуры словаря (сообщения) сервером от клиента:
        неверное значение ключа ACTION
        :return:
        """
        self.assertEqual(client_message_processing(
            {
                ACTION: '',
                TIME: 1650953345.1,  # для реализации теста - время константа
                USER: {ACCOUNT_NAME: 'Guest'}
            }
        ), self.error_dict)

    def test_def_client_message_processing_response__no_time(self):
        """
        Тест некорректного получения структуры словаря (сообщения) сервером от клиента:
        отсутствует ключ TIME
        :return:
        """
        self.assertEqual(client_message_processing(
            {
                ACTION: PRESENCE,
                USER: {ACCOUNT_NAME: 'Guest'}
            }
        ), self.error_dict)

    def test_def_client_message_processing_response__no_user(self):
        """
        Тест некорректного получения структуры словаря (сообщения) сервером от клиента:
        отсутствует ключ USER
        :return:
        """
        self.assertEqual(client_message_processing(
            {
                ACTION: PRESENCE,
                TIME: 1650953345.1  # для реализации теста - время константа
            }
        ), self.error_dict)

    def test_ip(self):
        """
        Тест получения IP адреса для приема сервером клиента по умолчанию
        :return:
        """
        self.assertEqual(setup_ip(), '')

    def test_port(self):
        """
        Тест получения адрес порта для приема сервером клиента по умолчанию
        :return:
        """
        self.assertEqual(setup_port(), 7777)


if __name__ == '__main__':
    unittest.main()
