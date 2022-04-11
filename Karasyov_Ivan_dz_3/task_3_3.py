
name_dict = {}


def thesaurus(names: list):
    for name in names:
        letter = name[0]
        if name_dict.get(letter):
            name_dict.update({letter: [*name_dict.get(letter), name]})
        else:
            name_dict.setdefault(letter, letter)
            name_dict[letter] = [name]


name_list = ["Иван", "Мария", "Петр", "Илья"]
thesaurus(name_list)
print(name_dict)
