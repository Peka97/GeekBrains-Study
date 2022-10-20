# Task 125 из книги Бена Стивенсена "Python. Сборник упражений 2021".
# Программа должна выводить все карты из колоды в текстомов виде
from task_1_1 import usage

@usage
def createDeck():
    suits = ['s', 'c', 'd', 'h']
    nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    cards = []
    for suit in suits:
        for nominal in nominals:
            cards.append(f'{nominal}{suit}')
    return cards


@usage
def createDeck_2():
    suits = ['s', 'c', 'd', 'h']
    nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    cards = []
    for suit in suits:
        for nominal in nominals:
            yield f'{nominal}{suit}'


if __name__ == '__main__':
    # Ничего нового, результаты снова те же. Но генератор на возврате явно лучше списка - и быстрее, и легче
    print(createDeck())  # -> 0.00390625
    print(createDeck_2())  # -> 0.00390625

