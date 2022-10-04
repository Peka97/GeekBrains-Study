"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess_the_number(random_number: int, attempt: int, user_number: int = None):
    # Шаг рекурсии
    if user_number is None:
        user_number = int(input('Попробуй угадай моё число: '))
        return guess_the_number(random_number, attempt + 1, user_number)
    else:
        # Базовый случай
        if random_number == user_number:
            return 'Ты прав! С победой!'
        # Базовый случай
        elif attempt == 10:
            return f'Ты не прав. Попытки кончились, это было число {random_number}. Поражение!'
        # Шаг рекурсии
        elif user_number > random_number:
            user_number = int(input('Моё число меньше. Попробуй ещё раз: '))
            return guess_the_number(random_number, attempt + 1, user_number)
        # Шаг рекурсии
        elif user_number < random_number:
            user_number = int(input('Моё число больше. Попробуй ещё раз: '))
            return guess_the_number(random_number, attempt + 1, user_number)


if __name__ == '__main__':
    print(guess_the_number(randint(0, 100), 0))
