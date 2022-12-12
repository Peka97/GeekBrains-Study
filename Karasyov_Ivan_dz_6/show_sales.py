def sum_sale(argv):
	"""
	Выводит числа из bakery.py.
	Если сообщить один аргумент - вернёт срез от аргумента до конца.
	Если сообщить два аргумента - вернёт срез от первого до второго аргумента (включительно)
	"""
	print(argv)
	if len(argv[1:]) == 1:
		print("Have Start")
		start = int(argv[1]) - 1
		with open('bakery.csv', 'r', encoding='utf-8') as file:
			for item in file.readlines()[start:]:
				print(item.strip('\n'))
	elif len(argv[1:]) == 2:
		print("Have Start and Finish")
		start = int(argv[1]) - 1
		finish = int(argv[2])
		with open('bakery.csv', 'r', encoding='utf-8') as file:
			for item in file.readlines()[start:finish]:
				print(item.strip('\n'))
	else:
		with open('bakery.csv', 'r', encoding='utf-8') as file:
			print(file.read())


if __name__ == '__main__':
	import sys

	exit(sum_sale(sys.argv))
