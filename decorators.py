import logging
import sys
import traceback
# from logs import client_log_config, server_log_config


def log(create_log):
    def log_saver(*args, **kwargs):
        logger_name = 'server.py' if 'server.py' in sys.argv[0] else 'client'
        logger = logging.getLogger(logger_name)

        ret = create_log(*args, **kwargs)

        logger.debug(f'Была вызвана функция {create_log.__name__} c параметрами {args}, {kwargs}.'
                     f' Вызов из модуля {create_log.__module__}.'
                     f' Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}')
        return ret
    return log_saver
