"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class Node:
    def __init__(self, key):
        """
        Создает экземпляр узла(корня).

        :param key: ключ узла(корня)
        """
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, key):
        """
        Метод вставки ключа на место левого потомка. В случае, если в текущем узле ключ меньше передаваемого, то
        метод спускается на уровень глубже. В случае, если значение недопустимо (больше или равно текущему), то
        пробрасывает ошибку.
        """

        if key < self.key:
            if self.left_child == None:
                self.left_child = Node(key)

            else:
                if key < self.left_child.key:
                    self.left_child.insert_left_child(key)

                else:
                    new_node = Node(key)
                    new_node.insert_left_child(self.left_child.key)
                    self.left_child = new_node

        else:
            raise IndexError(f"Child key ({key}) more or equel to parrent key ({self.key}). Fix it")

    def insert_right_child(self, key):
        """
        Метод вставки ключа на место правого потомка. В случае, если в текущем узле ключ больше передаваемого, то
        метод спускается на уровень глубже. В случае, если значение недопустимо (меньше или равно текущему), то
        пробрасывает ошибку.
        """

        if key > self.key:
            if self.right_child == None:
                self.right_child = Node(key)

            else:
                if key > self.right_child.key:
                    self.right_child.insert_right_child(key)

                else:
                    new_node = Node(key)
                    new_node.insert_right_child(self.right_child.key)
                    self.right_child = new_node
        else:
            raise IndexError(f"Child key ({key}) more or equel to parrent key ({self.key}). Fix it")

    def add(self, key):
        """Метод, автоматически добавляющий значение на подходящее место."""

        if key < self.key:
            if self.left_child == None:
                self.left_child = Node(key)

            else:
                if key < self.left_child.key:
                    self.left_child.insert_left_child(key)

                else:
                    new_node = Node(key)
                    new_node.insert_left_child(self.left_child.key)
                    self.left_child = new_node
        elif key > self.key:
            if self.right_child == None:
                self.right_child = Node(key)

            else:
                if key > self.right_child.key:
                    self.right_child.add(key)

                else:
                    new_node = Node(key)
                    new_node.add(self.right_child.key)
                    self.right_child = new_node

        else:
            raise IndexError(f"Child key ({key}) more or equel to parrent key ({self.key}). Fix it")

    def show_tree(self, dct: dict):
        """
        Функция для вывода содержания дерева в виде словаря, который нужно заранее передать.
        Ключём словаря является ключ узла, а значением кортеж из левого и правого узла (или листьев) соответственно.
        Если один из узлов (листьев) остутствует, то на его место указывается None.

        Шаблон: {Родитель: (Левый потомок, Правый потомок), ...}
        Пример: {8: (6, 10), ...}
        """

        if self.left_child and self.right_child:
            dct[self.key] = self.left_child.key, self.right_child.key
            self.left_child.show_tree(dct)
            self.right_child.show_tree(dct)

        elif self.right_child and not self.left_child:
            dct[self.key] = None, self.right_child.key
            self.right_child.show_tree(dct)

        elif not self.right_child and self.left_child:
            dct[self.key] = self.left_child.key, None
            self.left_child.show_tree(dct)

        else:
            dct[self.key] = None, None

    def get_right_child(self):
        """Возвращает правого потомка узла(корня)"""
        return self.right_child

    def get_left_child(self):
        """Возвращает левого потомка узла(корня)"""
        return self.left_child

    def set_root_val(self, obj):
        """Устанавливает новое значение для узла(корня)"""
        if self.left_child.key < obj < self.right_child.key:
            self.key = obj
        else:
            raise ValueError(f"New root val for {self.key} must be between {self.left_child.key} and {self.right_child.key}")

    # метод доступа к корню
    def get_root_val(self):
        return self.key


if __name__ == '__main__':
    tree = Node(8)

    # Демонстрация работы универсального метода add:
    tree.add(4)
    tree.add(16)
    tree.add(10)
    tree.add(6)
    tree.add(3)
    tree.add(14)
    tree.add(15)
    tree.add(2)

    # Демонстрация работы методов добавления левого и правого потомка:
    tree.insert_left_child(1)
    tree.insert_right_child(11)

    # Демонстрация работы метода, выводящего всё дерево:
    result = {}
    tree.show_tree(result)
    print(result)

    # Демонстрация работы метода замены ключа узла(корня):
    tree.set_root_val(9)

    result = {}
    tree.show_tree(result)
    print(result)

    # Демонстрация работы методов получения узлов потомков:
    print(tree.get_left_child())  # -> Node
    print(tree.get_right_child())  # -> Node
    print(tree.left_child.get_right_child())  # -> None
    print(tree.right_child.get_right_child())  # -> Node


