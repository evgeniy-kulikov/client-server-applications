import unittest
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_answer


class TestClient(unittest.TestCase):
    """
    Тест проверки функций клиента
    """

    def test_def_create_presence(self):
        """
        Тест успешной процедуры запроса
        :return
        """
        test = create_presence()
        test[TIME] = 1650953345.1  # для реализации теста - время константа
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1650953345.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_def_process_answer_200(self):
        """
        Тест, когда значение ключа RESPONSE равно 200
        :return:
        """
        self.assertEqual(process_answer({RESPONSE: 200}), 'code 200 : OK')

    def test_def_process_answer_400(self):
        """
        Тест, когда значение ключа RESPONSE равно 400
        :return:
        """
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), 'code 400 : Bad Request')

    def test_def_process_answer_no_response(self):
        """
        Тест возникновения исключения без ключа RESPONSE
        :return:
        """
        self.assertRaises(ValueError, process_answer, {ERROR: ''})


if __name__ == '__main__':
    unittest.main()
