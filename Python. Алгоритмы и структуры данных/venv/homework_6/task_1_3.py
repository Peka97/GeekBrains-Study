# Тут я впал в тильт, ибо на курсе базы мы не писали особо большие задачи\проекты и я изначально старался всё
# оптимизировать. С вашего разрешения возьму задачи, которые я брал со сборника во время "специальных каникул" и попробую
# их оптимизировать.

# Task 138 из книги Бена Стивенсена "Python. Сборник упражений 2021".
# Программа должна принимать на ввод буквы, как в своё время было на аналоговых телефонах при наборе смс и возвращать
# цифры, которые нужно было бы набрать.
from memory_profiler import memory_usage


def usage(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@usage
def phone_keyboard(txt: str):
    dct = {1: ['.', ',', '?', '!', ':'],
           2: ['A', 'B', 'C'],
           3: ['D', 'E', 'F'],
           4: ['G', 'H', 'I'],
           5: ['J', 'K', 'L'],
           6: ['M'' N', 'O'],
           7: ['P', 'Q', 'R', 'S'],
           8: ['T', 'U', 'V'],
           9: ['W', 'X', 'Y', 'Z'],
           0: [' ']
           }
    reply = ''
    for el in txt.upper():
        for key, val in dct.items():
            if el in val:
                count = val.index(el) + 1
                reply += str(key) * count
                break
    return reply


@usage
def phone_keyboard_2(txt: str):
    data = ((' '),
            ('.', ',', '?', '!', ':'),
            ('A', 'B', 'C'),
            ('D', 'E', 'F'),
            ('G', 'H', 'I'),
            ('J', 'K', 'L'),
            ('M'' N', 'O'),
            ('P', 'Q', 'R', 'S'),
            ('T', 'U', 'V'),
            ('W', 'X', 'Y', 'Z'),
            )
    reply = ''
    txt_content = txt.upper()
    txt_idx, data_idx = 0, 0
    while True:
        if txt_idx > len(txt_content) - 1:
            break
        if txt_content[txt_idx] in data[data_idx]:
            reply += str(data_idx) * (data[data_idx].index(txt_content[txt_idx]) + 1)
            txt_idx += 1
            data_idx = 0
        else:
            data_idx += 1
    return reply



if __name__ == '__main__':
    # И это дерьмо явно работает не правильно, ибо в первом случае я ВСЕГДА получаю 0.0390625, а во втором 0.0 при
    # последовательном запуске и просто 0.0390625 при одинарном. С этим заданием я вожусь уже неделю и не нахожу
    # ответа ни в конспекте, ни в записи урока. Я без понятия в чём дело, но я ЯВНО оптимизировал функцию.

    res, mem_diff = phone_keyboard("Hello World!")
    print(f"Выполнение заняло {mem_diff} Mib")

    res, mem_diff = phone_keyboard_2('Hello World!')
    print(f"Выполнение заняло {mem_diff} Mib")
