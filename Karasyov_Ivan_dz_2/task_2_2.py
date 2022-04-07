base_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
changed_list = []
for idx, item in enumerate(base_list):
    if item.isdigit():
        changed_list.append(f'"{int(item):02d}"')
    elif item[0] == "+":
        changed_list.append(f'"+{int(item):02d}"')
    else:
        changed_list.append(item)
print(" ".join(changed_list))