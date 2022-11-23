tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def gen():
    diff = len(tutors) - len(klasses)
    if diff > 0:
        for _ in range(diff):
            klasses.append(None)
    for child, klass in zip(tutors, klasses):
        yield child, klass


print(type(gen()))
print(*gen())
