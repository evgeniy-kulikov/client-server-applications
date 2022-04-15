# Homework for lesson 1

# 04. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).


def encode_decode(in_str):
    for i in in_str:
        input_encode = i.encode('utf-8')
        out_decode = input_encode.decode('utf-8')
        print(out_decode)


list_str_4 = ['разработка', 'администрирование', 'protocol', 'standard']
encode_decode(list_str_4)
