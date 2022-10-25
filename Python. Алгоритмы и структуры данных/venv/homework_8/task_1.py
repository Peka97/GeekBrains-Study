"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.

У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque


class Haffman:
    def __init__(self, text: str):
        self.text = text
        self.count = Counter(text)
        self.sorted_elements = deque(sorted(self.count.items(), key=lambda item: item[1]))
        self.code_table = dict()

    def haffman_tree(self):
        if len(self.sorted_elements) != 1:
            while len(self.sorted_elements) > 1:
                weight = self.sorted_elements[0][1] + self.sorted_elements[1][1]
                comb = {0: self.sorted_elements.popleft()[0],
                        1: self.sorted_elements.popleft()[0]}

                for i, _count in enumerate(self.sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        self.sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    self.sorted_elements.append((comb, weight))
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = self.sorted_elements[0][1]
            comb = {0: self.sorted_elements.popleft()[0], 1: None}
            self.sorted_elements.append((comb, weight))
        return self.sorted_elements[0][0]

    def haffman_encode(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.haffman_encode(tree[0], path=f'{path}0')
            self.haffman_encode(tree[1], path=f'{path}1')

    def get_encode_text(self):
        return ' '.join([self.code_table[i] for i in self.text])


if __name__ == '__main__':
    haff = Haffman("beep boop beer!")
    haff.haffman_encode(haff.haffman_tree())
    print(haff.get_encode_text())
