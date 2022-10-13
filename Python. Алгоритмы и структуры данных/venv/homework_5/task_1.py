"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple
from statistics import mean


def get_report():
    data = []
    count_of_company = int(input('Введите количество предприятий для расчета прибыли: '))
    while count_of_company > 0:
        count_of_company -= 1
        company_name = input('Введите название предприятия: ')
        company_income = input(
            'Через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ').split(' ')
        company_mean_income = mean(map(int, company_income))
        COMPANY = namedtuple('company_data', 'name income')
        result = COMPANY(
            name=company_name,
            income=company_mean_income
        )
        data.append(result)

    all_incomes = []
    less_that_mean = []
    more_that_mean = []
    for elem in data:
        all_incomes.append(int(elem.income))
    mean_of_all_income = (mean(all_incomes))
    for elem in data:
        if int(elem.income) < mean_of_all_income:
            less_that_mean.append(elem.name)
        elif int(elem.income) > mean_of_all_income:
            more_that_mean.append(elem.name)

    # Среднее значение почему-то получилось отличное от примера, хотя делаю вроде верно.
    print(f'Средняя годовая прибыль всех предприятий: {mean_of_all_income}')
    print(f'Предприятия, с прибылью выше среднего значения: {" ".join(more_that_mean)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {" ".join(less_that_mean)}')


if __name__ == '__main__':
    get_report()
