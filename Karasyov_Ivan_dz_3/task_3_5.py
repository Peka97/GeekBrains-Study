from random import randrange


def word_from_joke(joke_list):
    """Выбирает 3 рандомные шутки"""

    return joke_list[randrange(len(joke_list))]


def delete_words(lst: list, word: str):
    """Удаляет уже использованные слова шуток"""

    lst.remove(word)


def get_jokes(count: int, flag=0) -> str:
    """Создает шутку из заданной базы слов. Принимает количество шуток и параметр уникальности"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    words = {}
    if count > 5:
        return print("Рекомендуем ввести значение от 1 до 5. Повторите попытку")  # Написал ограничение во избежание ошибок
    if flag == 1:
        for i in range(count):
            words.update({1: word_from_joke(nouns), 2: word_from_joke(adverbs), 3: word_from_joke(adjectives)})
            delete_words(nouns, words.get(1))
            delete_words(adverbs, words.get(2))
            delete_words(adjectives, words.get(3))
            print(*words.values())
    else:
        for i in range(count):
            words.update({1: word_from_joke(nouns), 2: word_from_joke(adverbs), 3: word_from_joke(adjectives)})
            print(*words.values())


x = int(input("Введите количество шуток: "))
y = int(input("Укажите уникальность шуток (0 - откл., 1 - вкл.): "))
get_jokes(x, y)
