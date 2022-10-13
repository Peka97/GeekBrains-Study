"""
Задача 4.

Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.

Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

dct = dict()
odct = OrderedDict()


def dct_add():
    for n in range(10000):
        dct[n] = n


def odct_add():
    for n in range(10000):
        odct[n] = n


def dct_get():
    for n in range(10000):
        dct.get(n)


def odct_get():
    for n in range(10000):
        odct.get(n)


def dct_pop():
    for n in range(10000):
        dct.pop(n, n)


def odct_pop():
    for n in range(10000):
        odct.pop(n, n)


if __name__ == '__main__':
    # Тесты
    print('dct_add', timeit('dct_add()', globals=globals(), number=5000))    # -> 2.78834
    print('odct_add', timeit('odct_add()', globals=globals(), number=5000))  # -> 3.9078

    print('dct_get', timeit('dct_get()', globals=globals(), number=5000))    # -> 3.0800
    print('odct_get', timeit('odct_get()', globals=globals(), number=5000))  # -> 3.1132

    print('dct_pop', timeit('dct_pop()', globals=globals(), number=5000))    # -> 2.5894
    print('odct_pop', timeit('odct_pop()', globals=globals(), number=5000))  # -> 2.8042
    # Вывод: во всех операциях показал себя лучше встроенный словарь. Хоть в конспекте было указано, что по некоторым
    # данным ordereddict быстрее стандартного dict, мне таких данных получить не удалось. Стало быть вовсе не нужен, ибо
    # условная договоренность и явное указывание на важность порядка не стоит дополнительных затрат по ресурсам. Разве
    # что оставили для поддержки старых проектов.
