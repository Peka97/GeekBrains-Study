num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

number = input("Введите чисто от одного до десяти: ")


def num_lower():
    return True


def num_upper():
    return True


def num_translate_adv(num: str) -> str:
    """Переводит числа от 0 до 10 с английского на русский в прежнем формате"""
    if num == num.lower():  # Сделать проверку главной буквы через фукнции выше
        print(1)
    elif num == num.capitalize():
        print(2)
    if num in num_dict.keys():
        print(num_dict.get(num))
    else:
        return None


num_translate_adv(number)
