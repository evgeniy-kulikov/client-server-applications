# Homework for lesson 1

list_str = ['разработка', 'сокет', 'декоратор']
for i in list_str:
    print(f'строка "{i}" является типом: {type(i)}')

print('\nПосле использования онлайн конвертера текста в юникод:\n')

list_bytes_str = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                  '\u0441\u043e\u043a\u0435\u0442',
                  '\u0441\u043e\u043a\u0435\u0442']
for i in list_bytes_str:
    print(f'строка в Unicode формате "{i}" вляется типом: {type(i)}')
