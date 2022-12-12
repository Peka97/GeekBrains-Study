from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
	@abstractmethod
	def consuption(self):
		pass


class Clothing(MyAbstractClass):

	def __init__(self, name, cloth_type, V, H):
		self.name = name
		self.cloth_type = cloth_type
		self.V = V
		self.H = H

	@property
	def consuption(self):
		if self.cloth_type == "пальто":
			return round(self.V / 6.5 + 0.5, 2)
		elif self.cloth_type == "костюм":
			return round(self.V / 6.5 + 0.5, 2)


a = Clothing("Gucci", "пальто", 160, 50)
b = Clothing("Prada", "костюм", 150, 55)

print(a.consuption)
print(b.consuption)
print(a.consuption + b.consuption)
