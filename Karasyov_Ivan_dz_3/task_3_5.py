from random import randrange


def word_from_joke(joke_list):
    return joke_list[randrange(len(joke_list))]


def delete_word(word):
    return None


def get_jokes(count: int, flag=0):
    if flag == 1:
        for i in range(count):
            nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
            adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
            adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
            joke = [word_from_joke(nouns), word_from_joke(adverbs), word_from_joke(adjectives)]
            print(joke)
    else:
        for i in range(count):
            nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
            adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
            adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
            joke = [word_from_joke(nouns), word_from_joke(adverbs), word_from_joke(adjectives)]
            print(joke)


x = int(input("Введите количество шуток: "))
get_jokes(x)