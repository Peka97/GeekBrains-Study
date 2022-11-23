import sys


def gen():
    """Генератор чисел по условию задачи №4"""
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    for idx, num in enumerate(src):
        if src[idx] > src[idx - 1] and idx > 1:
            yield num


def lst():
    """Функция, выполняющая ту же задачу. Прописана для сравнения оптимизации кода"""
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = []
    for idx, num in enumerate(src):
        if src[idx] > src[idx - 1] and idx > 1:
            result.append(num)
    return result


print("Сравним вывод данных:\n",    *gen(), "\n",    *lst())
print(f"Сравним тип данных:\n  {type(gen())}\n  {type(lst())}")
print(f"Сравним вес данных:\n  {sys.getsizeof(gen())}\n  {sys.getsizeof(lst())}")
