"""Константы проекта"""

# Используемый по умолчанию TCP-порт для соединения.
DEFAULT_PORT = 7777
# Используемый по умолчанию IP адрес сервера для подключения клиента.
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений.
MAX_CONNECTIONS = 5
# Максимальная длина сообщения (пакета) в байтах.
MAX_PACKAGE_LENGTH = 1024
# # Используемая кодировка для проекта.
# ENCODING = 'utf-8'

# JIM прртокол. Используемые ключи.
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Ключи
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
