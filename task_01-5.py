# Homework for lesson 1

import subprocess
import platform  # определение семейства OS
import chardet  # сторонний пакет определяющий тип кодировки


def encode_ping(url):
    # определяем вид OS для определения используемого параметра, отвечающего за кол-во пингования
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', url]  # список передаваемых аргументов в запускаемый процесс пингования
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result_code = chardet.detect(line)  # результат определения кодировки
        # преобразоваие результа пинга из байтовового в строковый тип на кириллице
        line = line.decode(result_code['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


encode_ping('youtube.com')
encode_ping('yandex.ru')
