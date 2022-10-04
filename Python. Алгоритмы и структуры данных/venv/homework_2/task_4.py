"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_of_elements(start_count: int = None, count: int = None, number: float = None, result: float = None) -> str:
    if count is None:
        count = int(input('Введите количество элементов: '))
        start_count = count
        return sum_of_elements(start_count, count, 1, 0)
    # Базовый случай
    elif count == 1:
        return f'Количество элементов - {start_count}, их сумма - {number + result}'
    # Шаг рекурсии
    else:
        return sum_of_elements(start_count, count - 1, number / -2, result + number)


if __name__ == '__main__':
    print(sum_of_elements())
