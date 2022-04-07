# Задание 3

base_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
base_list_len = len(base_list)
for idx, item in enumerate(base_list):
    if idx == base_list_len:
        break
    elif item.isdigit():
        base_list.append(f'"{int(item):02d}"')
    elif item[0] == "+":
        base_list.append(f'"+{int(item):02d}"')
    else:
        base_list.append(item)
print(" ".join(base_list[base_list_len:]))
