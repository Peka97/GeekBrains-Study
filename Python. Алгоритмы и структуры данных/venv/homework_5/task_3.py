"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from timeit import timeit
from collections import deque

dq = deque()
ls = list()


def dq_app():
    for n in range(1000):
        dq.append(n)


def ls_app():
    for n in range(1000):
        ls.append(n)


def dq_pop():
    for _ in range(1000):
        dq.pop()


def ls_pop():
    for _ in range(1000):
        ls.pop()


def dq_ext():
    for _ in range(1000):
        dq.extend(range(10))


def ls_ext():
    for _ in range(1000):
        ls.extend([range(10)])


def dq_appleft():
    for n in range(100):
        dq.appendleft(n)


def ls_appleft():
    for n in range(100):
        ls.insert(0, n)


def dq_popleft():
    for _ in range(100):
        dq.popleft()


def ls_popleft():
    for _ in range(100):
        ls.pop(0)


def dq_extleft():
    for _ in range(100):
        dq.extendleft(range(10))


def ls_extleft():
    for _ in range(100):
        ls.insert(0, range(10))


def dq_get_elem():
    for elem in dq:
        pass


def ls_get_elem():
    for elem in ls:
        pass


if __name__ == '__main__':
    # Тест 1:
    print('dq_app', timeit('dq_app()', globals=globals(), number=1000))  # -> Быстрее чем list
    print('ls_app', timeit('ls_app()', globals=globals(), number=1000))

    print('dq_pop', timeit('dq_pop()', globals=globals(), number=1000))  # -> Быстрее чем list
    print('ls_app', timeit('ls_app()', globals=globals(), number=1000))

    print('dq_ext', timeit('dq_ext()', globals=globals(), number=1000))  # -> Медленнее чем list
    print('ls_ext', timeit('ls_ext()', globals=globals(), number=1000))
    # Вывод: на данных функциях deque показывает себя в целом быстрее, чем list. Только с методом extend у списка лучше
    # эффективность.
    print()

    # Тест 2:
    print('dq_appleft', timeit('dq_appleft()', globals=globals(), number=100))  # -> Быстрее чем list
    print('ls_appleft', timeit('ls_appleft()', globals=globals(), number=100))

    print('dq_popleft', timeit('dq_popleft()', globals=globals(), number=100))  # -> Быстрее чем list
    print('ls_popleft', timeit('ls_popleft()', globals=globals(), number=100))

    print('dq_extleft', timeit('dq_extleft()', globals=globals(), number=100))  # -> Быстрее чем list
    print('ls_extleft', timeit('ls_extleft()', globals=globals(), number=100))
    # Вывод: number и кол-во элементов сильно порезал ввиду долгой работы с list. Deque в сравнении с list показал себя
    # явным фаворитом.
    print()

    # Тест 3:
    print('dq_get_elem', timeit('dq_get_elem()', globals=globals(), number=100))  # -> Медленнее чем list
    print('ls_get_elem', timeit('ls_get_elem()', globals=globals(), number=100))
    # Вывод: number так же сократил ввиду долго работы. Deque показал себя значительно хуже, чем list.

    # Как итог мы понимаем, что если есть необходимость часто менять данные в массиве и редко к ним обращаться, то
    # deque будет отличным решением. В противном случае предпочтение отдаём list.
