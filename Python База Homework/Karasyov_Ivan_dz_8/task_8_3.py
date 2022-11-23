def type_logger(func):
	cache = {}

	# Тут должна быть маскировка, но я не разобрался в ней
	def wrapper(*args):
		nonlocal cache

		for item in args:
			key = str(item)
			if key not in cache:
				cache[key] = type(func(item))
				print(f"{func.__name__}({key}: {cache.get(key)})")
		cache.clear()  # Очистка кэша для чистой работы с теми же аргументами в будущем

	return wrapper


@type_logger
def calc_cube(x):
	return x ** 3


a = calc_cube(5)
b = calc_cube(5, 4, 3)


