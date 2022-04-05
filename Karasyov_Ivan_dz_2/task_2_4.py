workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for human in workers:
    name = human.split()
    f_name = name[-1].title()
    print(f"Привет, {f_name}!")