# Задание 5

price_list = [40.56, 58.9, 3.87, 16.97, 34.58, 16.35, 37, 49.81, 25.41, 64.95]  # Ручной список из цен на 10 товаров
print(f"Начальный список:\n{price_list}")  # Вывод списка
print(f"ID в начале: {id(price_list)}")  # Вывод ID списка в начале кода
price_list_len = len(price_list)

for idx, price in enumerate(price_list):
    if idx == price_list_len:
        break
    rub = str(price).split('.')[0]
    if type(price) == int:
        price_list[idx] = f"{int(rub):02d} руб {int(0):02d} коп"
    elif len(str(price).split('.')[1]) == 1:
        cop = str(price).split('.')[1] + "0"
        price_list[idx] = f"{int(rub):02d} руб {int(cop):02d} коп"
    else:
        price_list[idx] = f"{int(rub):02d} руб {int(str(price).split('.')[1]):02d} коп"

print("\nОтформатированный список цен:")
print(", ".join(price_list))  # Вывод отформатированного списка цен

price_list.sort()
print("\nСписок по возрастанию и его ID:")
print(", ".join(price_list))  # Вывод отсортированного списка по возрастанию
print(f"ID в конце: {id(price_list)}")  # Вывод ID списка в конце кода

price_list.sort(reverse=True)
print("\nСписок по убыванию:")
print(", ".join(price_list))  # Вывод отсортированного списка по убыванию

print("\nТОП-5 самых дорогих товаров:")
print(", ".join(price_list[:5]))  # Вывод ТОП-5 самых дорогих товаров с минимумом кода
