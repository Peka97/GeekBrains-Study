class ComplexNumber:
	def __init__(self, num):
		self.num = num

	def __add__(self, other):
		temp = []
		for i, j in zip(self.num, other.num):
			if i.isdigit() and i != 'i':
				temp.append(int(i) + int(j))
		return f"{temp[0]} + {temp[1]}*i"

	def __mul__(self, other):
		temp = []
		for i, j in zip(self.num, other.num):
			if i.isdigit() and i != 'i':
				temp.append(int(i) * int(j))
		return f"{temp[0]} + {temp[1]}*i"


a = ComplexNumber("2+7*i")
b = ComplexNumber("1+4*i")
print(a + b)
print(a * b)
