""" Конфигурация логгера для серверной части """

import sys
import os
import logging
import logging.handlers

# Создаём объект-логгер с именем server
LOG_SERVER = logging.getLogger('server')

# Создаём объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s ")
# Создаём файловый обработчик логгирования (можно задать кодировку):
# FILE_HANDLER = logging.FileHandler("server_info.log", encoding='utf-8')
FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(
    "server_info.log", encoding='utf-8', when='D', interval=1, backupCount=7)
FILE_HANDLER.setFormatter(FORMATTER)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логгирования
LOG_SERVER.addHandler(FILE_HANDLER)
LOG_SERVER.setLevel(logging.DEBUG)  # Корневой уровень критичности

if __name__ == '__main__':
    # Создаём потоковый обработчик логгирования (по умолчанию sys.stderr):
    STREAM_HANDLER = logging.StreamHandler()
    STREAM_HANDLER.setLevel(logging.DEBUG)  # Текущий уровень критичности
    STREAM_HANDLER.setFormatter(FORMATTER)
    LOG_SERVER.addHandler(STREAM_HANDLER)
    # В логгирование передаем имя текущей функции и имя вызвавшей функции
    LOG_SERVER.debug('Отладочное сообщение сервера')
