# Homework for lesson 1

from chardet import detect

# 06. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
# что перед нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того,
# в какой кодировке он был создан.


# создание файла
def create_file(content, file_name, user_encoding):
    file_doc = open(file_name, 'w', encoding=user_encoding)
    for i in content:
        file_doc.write(i + '\n')
    file_doc.close()


# определение кодировки файла и вывод содержимого
def read_file(file_name):
    with open(file_name, 'rb') as file_doc:
        file_content = file_doc.read()
    encoding = detect(file_content)['encoding']

    with open('test_file.txt', encoding=encoding) as file_doc:
        for el_str in file_doc:
            print(el_str, end='')


user_encoding_1 = 'cp1251'
content_1 = ['сетевое программирование', 'сокет', 'декоратор']
file_name_1 = 'test_file.txt'

create_file(content_1, file_name_1, user_encoding_1)
read_file(file_name_1)
