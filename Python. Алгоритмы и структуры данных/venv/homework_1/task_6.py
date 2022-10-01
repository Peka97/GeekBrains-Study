"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class StackClass:
    def __init__(self):
        self.elems = [[], [], []]

    def get_board(self, task: str) -> list | None:
        """Функция получения списка задач. На вход принимаются строго предопределенные названия досок: base, rework и
        done. Ввод любых других будет сопровожден сообщением о некорректности введённых данных"""

        if task == 'base':
            return self.elems[0]
        elif task == 'rework':
            return self.elems[1]
        elif task == 'done':
            return self.elems[2]
        else:
            print('Некорректные данные. Введите base, rework или done')

    def push_in(self, task: str, el: str) -> None:
        if task == 'base':
            self.elems[0].insert(0, el)
        elif task == 'rework':
            self.elems[1].insert(0, el)
        elif task == 'done':
            self.elems[2].insert(0, el)
        else:
            print('Некорректные данные. Введите base, rework или done')

    def pop_out(self, task: str) -> str | None:
        try:
            if task == 'base':
                return self.elems[0].pop()
            elif task == 'rework':
                return self.elems[1].pop()
            elif task == 'done':
                return self.elems[2].pop()
            else:
                print('Некорректные данные. Введите base, rework или done')
        except IndexError:
            print(f'Список задач {task} пустой. Невозможно удалить данные')

    def move_task_to(self, task_from: str, task_to: str) -> None:
        if task_to in ['base', 'rework', 'done'] and task_from in ['base', 'rework', 'done']:
            self.push_in(task_to, self.pop_out(task_from))
        else:
            print('Некорректные данные. Введите base, rework или done')

    def get_val(self, task: str) -> list | None:
        if task == 'base':
            return self.elems[0][len(self.elems[0]) - 1]
        elif task == 'rework':
            return self.elems[1][len(self.elems[1]) - 1]
        elif task == 'done':
            return self.elems[2][len(self.elems[2]) - 1]
        else:
            print('Некорректные данные. Введите base, rework или done')

    def stack_size(self, task: str) -> int | None:
        if task == 'base':
            return len(self.elems[0])
        elif task == 'rework':
            return len(self.elems[1])
        elif task == 'done':
            return len(self.elems[2])
        else:
            print('Некорректные данные. Введите base, rework или done')


if __name__ == '__main__':
    a = StackClass()

    # Наполняем наши доски данными:
    a.push_in('base', 'task1')
    a.push_in('base', 'task2')
    a.push_in('rework', 'task3')
    a.push_in('done', 'task4')
    a.push_in('done', 'task5')
    print(a.elems)

    a.move_task_to('base', 'rework')  # Пробуем переместить из base в rework
    print(a.elems)
    a.move_task_to('rework', 'done')  # Пробуем переместить из rework в done
    print(a.elems)
    a.move_task_to('done', 'rework')  # Пробуем переместить из done в rework
    print(a.elems)

    # Проверяем методы, которые возвращают текущее количество задач в очереди:
    print(a.stack_size('base'))
    print(a.stack_size('rework'))
    print(a.stack_size('done'))

    # Проверяем методы, которые показывают последнюю задачу в очереди:
    print(a.get_val('base'))
    print(a.get_val('rework'))
    print(a.get_val('done'))

    # Проверяем методы, которые показывают доски целиком:
    print(a.get_board('base'))
    print(a.get_board('rework'))
    print(a.get_board('done'))

    # Проверяем срабатывание исключения при вызове метода вырезания задачи из пустой очереди:
    print(a.pop_out('base'))  # Удачно | task2
    a.pop_out('base')  # Исключение
    a.pop_out('base')  # Исключение




