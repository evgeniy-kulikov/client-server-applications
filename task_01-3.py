# Homework for lesson 1

# 03. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.


def str_byte_3(in_str):
    for i in in_str:
        try:
            str_b = f"b'{i}'"
            eval(str_b)
            print(f'строку "{i}" можно представить в байтовом типе.')
        except SyntaxError:
            print(f'строку "{i}" невозможно представить в байтовом типе.')


list_str_3 = ['attribute', 'класс', 'функция', 'type']
str_byte_3(list_str_3)
