def add_sale(argv):
	"""
	Добавляет первый аргумент как число в bakery.csv.
	Если сообщить два аргумента - заменяет первый аргумент на второй (в случае отсутствия в bakery.csv возвращает ошибку)
	"""
	if len(argv) > 1:
		reply = []
		num_old = argv[1]
		num_new = argv[2]
		fail = True
		with open('bakery.csv', 'r+', encoding='utf-8') as file:
			for line in file:
				if num_old == line.strip(", \n"):
					reply.append(line.replace(num_old, num_new))
					print(f"\nЧисло {num_old} заменено на {num_new}\n")
					fail = False
				else:
					reply.append(line)
		if fail is True:
			return print(f"Ошибка: число {num_old} не найдено")
		with open('bakery.csv', 'w+', encoding='utf-8') as file:
			file.writelines(reply)
		with open('bakery.csv', 'r+', encoding='utf-8') as file:
			print(file.read())
	else:
		with open('bakery.csv', 'a+', encoding='utf-8') as file:
			file.write(f'{argv[1]}, \n')
			print(f"Число {argv[1]} добавлено")


if __name__ == '__main__':
	import sys

	exit(add_sale(sys.argv))
