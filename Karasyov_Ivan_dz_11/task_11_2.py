class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt


def division(x, y):
	try:
		if y == 0:
			raise OwnError("Нельзя делить на 0")
		result = x / y
	except TypeError:
		print("Ошибка типа данных")
	except ValueError:
		print("Необходимо ввести число")
	except OwnError as err:
		print(err)
	else:
		print(f"Разделили и получили: {result}")


# Тесты
division(100, 0)
division(50, 5)
division("11", 3)

# Ну и раз в задании фигурирует "вводимых пользователем"
param1 = int(input("Введите первое число: "))
param2 = int(input("Введите второе число: "))
division(param1, param2)
