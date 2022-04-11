
name_dict = {}


def thesaurus_adv(names: list):
    for name in names:
        first_name = name.split()[0]
        second_name = name.split()[1]
        letter_FN = first_name[0]
        letter_SN = second_name[0]
        print(name)
        if name_dict.get(letter_SN):
            if name_dict[letter_SN].values():
                if name_dict[letter_SN].keys() == letter_SN:
                    name_dict[letter_SN] = {letter_FN: [*name_dict[letter_SN].values(), name]}
                elif letter_FN in name_dict[letter_SN].keys():
                    print("УРА")
                    name_dict[letter_SN].update({letter_FN: [*name_dict[letter_SN].values(), name]})
                else:
                    print(0)
                    print(*name_dict[letter_SN].values())
                    print(0)
                    name_dict[letter_SN].update({letter_FN: [*name_dict[letter_SN].values(), name]})
            else:
                name_dict[letter_SN] = {letter_FN: [name]}
        else:
            print(1)
            name_dict.update({letter_SN: {letter_FN: name}})
        print(name_dict)


name_full_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
thesaurus_adv(name_full_list)
print(name_dict)
