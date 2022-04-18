# Homework for lesson 2

import re
import csv

# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
# и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data() в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data —
# и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().


def get_data():  # функция получения данных из исходных файлов
    data = []  # список с выборкой данных из исходных файлов

    for filename in source_files:
        with open(filename) as fl:
            for line in fl.readlines():
                # выборка всех строчек начинающихся с прописной буквы и заканчивающихся  символом перевода строки
                data += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)

    result_manufacture_list, result_name_list, result_code_list, result_type_list = [], [], [], []

    # выборка полей определенных в ТЗ.
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for item in data:  # убираем лишние строки из "data"
        result_manufacture_list.append(item[1]) if item[0] == main_data[0][0] else None
        result_name_list.append(item[1]) if item[0] == main_data[0][1] else None
        result_code_list.append(item[1]) if item[0] == main_data[0][2] else None
        result_type_list.append(item[1]) if item[0] == main_data[0][3] else None

    for i in range(len(result_manufacture_list)):  # формирование двухмерного списка
        main_data.append([result_manufacture_list[i], result_name_list[i], result_code_list[i], result_type_list[i]])

    return main_data


def write_to_csv():  # функция создания *.csv файла
    source_data = get_data()
    with open('result_file.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')  # разделяем данные запятой

        for line in source_data:
            writer.writerow(line)  # запись сразу всех данных


# для простоты файлы с данными находятся в одной директории со скриптом
source_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
write_to_csv()
