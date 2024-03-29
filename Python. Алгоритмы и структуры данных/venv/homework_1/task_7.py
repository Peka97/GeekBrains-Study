"""
Задание 7. На закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""

from task_14 import DequeClass


def pal_checker(string):
    dc_obj = DequeClass()
    string = string.replace(' ', '')  # Доработка

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        print(first, last)
        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(pal_checker("топот"))
    print(pal_checker("молоко делили ледоколом"))
