# Homework for lesson 1

# 02. Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению,
# (т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип,
# содержимое и длину соответствующих переменных.


def str_byte(in_str):
    for i in in_str:
        str_b = f"b'{i}'"
        eval(str_b)
        print(
            f'строка "{i}" в байтовом типе выглядит: {str_b} '
            f'и имеет тип: {type(eval(str_b))} длиной {len(eval(str_b))} символов')


list_str_2 = ['class', 'function', 'method']
str_byte(list_str_2)
