from copy import copy


class Cell:

	def __init__(self, amount):
		self.amount = amount

	def __add__(self, other):
		return self.amount + other.amount

	def __sub__(self, other):
		return self.amount - other.amount if self.amount - other.amount > 0 else "Разность меньше 0"

	def __mul__(self, other):
		return self.amount * other.amount

	def __truediv__(self, other):
		return round(self.amount / other.amount)

	def make_order(self, num):
		result = ''
		cells = copy(self.amount)
		for _ in range(cells // num):
			result += f"{'*' * num}\n"
			cells -= num
		result += f"{'*' * cells}"
		return result


a = Cell(15)
b = Cell(12)
c = Cell(22)
print(a + b)
print()
print(a - b)
print(a - c)
print()
print(a * b)
print()
print(a / b)
print()
print(b.make_order(5))
print()
print(a.make_order(5))




