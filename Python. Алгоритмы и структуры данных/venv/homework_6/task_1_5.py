# Task 120 из книги Бена Стивенсена "Python. Сборник упражений 2021".
# Программа должна выводить слова из списка любой длины с соединением через запятую и в конце через 'и'.
from task_1_1 import usage

lst_1 = ['яблоки', "апельсины", "бананы", "лимоны"]
lst_2 = ['яблоки', "бананы", "лимоны"]
lst_3 = ["бананы", "лимоны"]


@usage
def func(l):
    reply = ""
    for el in l[0:-1]:
        reply += f"{el}, "
    reply = reply.rstrip(', ')
    reply += f' и {l[-1]}'
    return reply


@usage
def func_2(l):
    yield ', '.join(l)
    yield f' и {l[-1]}'


if __name__ == '__main__':
    # Ничего нового, но решение явно оптимизировано

    print(func(lst_1))  # -> 0.00390625
    print(func(lst_2))  # -> 0.0
    print(func(lst_3))  # -> 0.0

    print(func_2(lst_1))  # -> 0.0
    print(func_2(lst_2))  # -> 0.0
    print(func_2(lst_3))  # -> 0.0
