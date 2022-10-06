"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""
from queue import QueueClass


# Вариант, который работает с числами оканчивающимися на 0:
def reverse_number(number: int = None) -> str:
    if not number:
        number = int(input('Введите число, которое требуется перевернуть: '))
        return reverse_number(number)
    elif number > 10:
        q.push_in(number % 10)
        number //= 10
        return reverse_number(number)
    elif number < 10:
        q.push_in(number % 10)
        return ''.join(map(str, q.all_out()))


# Вариант, который НЕ работает с числами оканчивающимися на 0:
def reverse_number_2(number: int = None, reverse: int = None):
    if not number and not reverse:
        number = int(input('Введите число, которое требуется перевернуть: '))
        reverse = 0
        return reverse_number_2(number, reverse)
    else:
        if number > 0:
            reverse = reverse * 10 + number % 10
            number //= 10
            return reverse_number_2(number, reverse)
        else:
            return reverse


if __name__ == '__main__':
    q = QueueClass()
    print(reverse_number())
    print(reverse_number_2())
