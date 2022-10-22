"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные по длине части:

в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def median_(m: int):
    arr = [randint(0, 100) for _ in range(2 * m + 1)]
    n, i = len(arr), 0
    while True:
        if i + 1 == n:
            break
        if arr[i + 1] >= arr[i]:
            i += 1
        else:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return arr[m]


if __name__ == '__main__':
    print(timeit('median_(100)', globals=globals(), number=10))  # -> 0.03437440004199743
    print(timeit('median_(100)', globals=globals(), number=100))  # -> 0.34674269997049123
    print(timeit('median_(100)', globals=globals(), number=1000))  # -> 3.3703555999090895
