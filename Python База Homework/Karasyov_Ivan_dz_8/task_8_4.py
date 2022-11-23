def val_checker(func):
	cache = {}

	# Тут должна быть маскировка, но я не разобрался в ней
	def wrapper(args):
		nonlocal cache

		if args > 0:
			key = str(args)
			if key not in cache:
				cache[key] = func(args)
			print(cache[key])
			cache.clear()
		else:
			msg = f"wrong val {args}"
			raise ValueError(msg)

	return wrapper


@val_checker
def calc_cube(x):
	return x ** 3


a = calc_cube(5)

b = calc_cube(-5)
