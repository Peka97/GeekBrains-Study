"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackClass:
    def __init__(self):
        self.elems = [[], ]
        self.current_idx = 0
        self.limit = 10

    def is_empty(self):
        return self.elems[self.current_idx] == []

    def stack_size(self):
        return len(self.elems[self.current_idx])

    def push_in(self, el):  # Предусматриваем ситуацию для перехода на новый стек в случае переполнения стека
        if self.stack_size() < self.limit:
            self.elems[self.current_idx].append(el)
        else:
            self.current_idx += 1
            self.elems.append([])
            self.elems[self.current_idx].append(el)

    def pop_out(self):  # Предусматриваем ситуацию с пустым стеком
        if self.stack_size() != 0:
            return self.elems[self.current_idx].pop()
        else:
            self.current_idx -= 1
            del self.elems[-1]
            return self.elems[self.current_idx].pop()

    def get_val(self):
        return self.elems[self.current_idx][self.stack_size() - 1]

    def count_of_stacks(self):
        return len(self.elems)


if __name__ == '__main__':
    a = StackClass()  # Создаем экземпляр класса
    print(a.is_empty())  # Проверяем, что он пустой

    for num in range(1, 92):  # В цикле заполняем его данными
        a.push_in(num)

    print(a.limit)  # Проверяем ограничение количества данных в одном стеке
    print(a.stack_size())  # Проверяем наполняемость стеков
    print(a.count_of_stacks())  # Проверяем количество стеков
    print(a.elems)  # Проверяем элементы стека
    a.pop_out()  # Выразаем несколько элементов (взято специально на пороге для проверки удаления пустого стека)
    a.pop_out()
    a.pop_out()
    print(a.elems)  # Проверяем стэки. Убеждаемся, что пустой стек удалился

    for num in range(89, 96):  # Пробуем заполнить стэки до перехода на следующий
        a.push_in(num)

    print(a.elems)  # Убеждаемся в корректной заполняемости
    print(a.get_val())  # Достаём последнее число из стэка
