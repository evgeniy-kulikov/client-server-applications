import logging

"""
Конфигурация логгера для клиентской части
"""


# Создаём объект-логгер с именем client
LOG_CLIENT = logging.getLogger('client')

# Создаём объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаём файловый обработчик логгирования (client_info.log - имя создаваемого файла):
FILE_HANDLER = logging.FileHandler("client_info.log", encoding='utf-8')
# вывод сообщений с уровнем DEBUG
FILE_HANDLER.setLevel(logging.DEBUG)
# Формат сообщений
FILE_HANDLER.setFormatter(FORMATTER)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логгирования
LOG_CLIENT.addHandler(FILE_HANDLER)
LOG_CLIENT.setLevel(logging.DEBUG)  # Корневой уровень критичности

if __name__ == '__main__':
    # Создаём потоковый обработчик логгирования (по умолчанию sys.stderr):
    STREAM_HANDLER = logging.StreamHandler()
    STREAM_HANDLER.setLevel(logging.DEBUG)  # Текущий уровень критичности
    STREAM_HANDLER.setFormatter(FORMATTER)
    LOG_CLIENT.addHandler(STREAM_HANDLER)
    # В логгирование передаем имя текущей функции и имя вызвавшей функции
    LOG_CLIENT.debug('Отладочное сообщение клиетнта')
