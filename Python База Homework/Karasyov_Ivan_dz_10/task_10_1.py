import numpy as np


class Matrix:

	def __init__(self, array):
		self.array = array

	def __str__(self):
		result = ""
		for el in self.array:
			result += f'{el}\n'
		return result

	def __add__(self, other):
		return Matrix(np.array(self.array) + np.array(other.array))


a = Matrix([[1, 2, 3, 4, 5], [5, 2, 1, 3, 1]])
b = Matrix([[5, 2, 1, 5, 3], [1, 4, 1, 4, 5]])

print(a.array)
print(b.array)
print()
print(a)
print(b)
print()
print(a + b)

