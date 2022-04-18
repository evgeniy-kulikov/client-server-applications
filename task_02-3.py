# Homework for lesson 2

import yaml

# 3. Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
# Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

data = {
    'Name_product': ['computer', 'monitor', 'mouse', 'printer'],
    'items_quantity': 4,
    'items_price': {
        'computer': '500€-1000€',
        'monitor': '200€-500€',
        'mouse': '4€-20€',
        'printer': '100€-500€'
    }
}

with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('file.yaml', encoding='utf-8') as yaml_file:
    print(yaml_file.read())
