"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:

в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:
2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def median_(m: int):
    arr = [randint(0, 100) for _ in range(2 * m + 1)]
    for _ in range(m):
        arr.remove(max(arr))
    return max(arr)


if __name__ == '__main__':
    print(timeit('median_(100)', globals=globals(), number=10))  # -> 0.005476600024849176
    print(timeit('median_(100)', globals=globals(), number=100))  # -> 0.05556759994942695
    print(timeit('median_(100)', globals=globals(), number=1000))  # -> 0.42303130007348955
