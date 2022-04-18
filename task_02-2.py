# Homework for lesson 2

import json

# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
# Для этого: Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', encoding="utf-8") as fl:
        data = json.loads(fl.read())

    data["orders"].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', "w", encoding="utf-8") as fl:
        json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    write_order_to_json('Любанович Билл – Простой Python', '1', '800', 'Иванов И.И.', '17.04.2022')
    write_order_to_json('Дауни А. - Основы Python', '1', '900', 'Петров П.П.', '18.04.2022')
    write_order_to_json('Златопольский Д.М. - 1400 задач по программированию', '1', '900', 'Сидоров С.С.', '18.04.2022')
