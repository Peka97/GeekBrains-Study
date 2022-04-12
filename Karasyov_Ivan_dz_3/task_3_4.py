def thesaurus_adv(names: list):
    name_dict = {}
    for name in names:
        first_name = name.split()[0]
        second_name = name.split()[1]
        letter_FN = first_name[0]
        letter_SN = second_name[0]
        if name_dict.get(letter_SN) is None:
            name_dict[letter_SN] = {letter_FN: name}
        else:
            if name_dict.get(letter_SN) is not None:
                if name_dict[letter_SN].get(letter_FN):
                    name_dict[letter_SN].update({letter_FN: [*name_dict[letter_SN].values(), name]})
                else:
                    name_dict[letter_SN].update({letter_FN: [name]})
    for key in sorted(name_dict.keys()):  # Вариант с сортировкой
        print(key, ':', name_dict[key])
    print(f"\n{name_dict}")  # Вариант без сортировки


name_full_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
thesaurus_adv(name_full_list)
