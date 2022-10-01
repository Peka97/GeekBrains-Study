"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min_num() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


def my_min_1(collection: list | tuple) -> int:
    """Функция для нахождения минимального значения в коллекции данных. Сложность O(n)"""

    min_num = collection[0]                                                   # O(1)
    for el in collection:                                                 # O(n)
        for idx in range(collection.index(el) + 1, len(collection) - 1):  # O(n)
            if min_num > collection[idx]:                                     # O(len(lst[j])
                min_num = collection[idx]                                     # O(1)
    return min_num                                                            # O(1)


def my_min_2(collection: list | tuple) -> int:
    """Функция для нахождения минимального значения в коллекции данных. Сложность O(n**2)"""

    min_num = collection[0]            # O(1)
    for el in collection:          # O(n)
        if el == min_num or el > min_num:  # O(1)
            continue
        min_num = el                   # O(1)
    return min_num                     # O(1)


# Зададим несколько массивов для тестов
tpl_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl_2 = [9, 10, 4, 11, 20, 4, 5, 2, 4]

# Проверим результаты наших функций
print(my_min_1(tpl_1))
print(my_min_2(tpl_2))

# Сравним с результатами функции min()
print(my_min_1(tpl_1) == min(tpl_1))
print(my_min_2(tpl_2) == min(tpl_2))
