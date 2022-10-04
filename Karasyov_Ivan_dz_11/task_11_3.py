class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt


result = []


def digit_in_list(el: str):
	try:
		if not el.isdigit():
			raise OwnError("Вы ввели не число. Повторите попытку")
	except OwnError as err:
		print(err)
	else:
		print(f"Число добавлено в список")
		result.append(int(user_inp))


while True:
	user_inp = input("Введите число или напишите 'stop' для выхода: ")
	if user_inp.lower() == "stop":
		print(f"Получен список:\n{result}")
		break
	else:
		digit_in_list(user_inp)
