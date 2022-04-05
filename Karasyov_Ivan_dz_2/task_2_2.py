import string

base_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for item in base_list:
    if item.isdigit() or item[0] == "+":
        item
words = " ".join(base_list)
print(words)