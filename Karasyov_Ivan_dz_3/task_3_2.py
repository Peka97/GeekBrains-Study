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


def num_lower(num_str: str):
    """Проверяет наличие ключа в словаре для слов со строчной буквы"""
    if num_str in num_dict.keys():
        return num_dict.get(num_str)
    else:
        return "Такого числа нет в словаре"


def num_upper(num_str: str):
    """Проверяет наличие ключа в словаре для слов с заглавной буквы"""
    if num_str.lower() in num_dict.keys():
        return num_dict.get(num_str.lower()).capitalize()
    else:
        return "Такого числа нет в словаре"


def num_translate_adv(num: str) -> str:
    """Переводит числа от 0 до 10 с английского на русский в прежнем формате"""
    if num == num.lower():
        print(num_lower(num))
    elif num == num.capitalize():
        print(num_upper(num))
    else:
        return None


num_translate_adv(number)
