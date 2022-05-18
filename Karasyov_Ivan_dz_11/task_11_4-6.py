class WarehouseOfficeEquipment:
	warehouse = []


class OfficeEquipment(WarehouseOfficeEquipment):
	def __init__(self, name, amount):
		if isinstance(name, str) and isinstance(amount, int):
			self.name = name
			self.amount = int(amount)
			self.warehouse.append({self.name: self.amount})
		else:
			print("Некорректный ввод данных")

	def to_warehouse(self, x):
		for i in self.warehouse:
			if i.get(self.name):
				i[self.name] = i.get(self.name) + x
				print(f"Доставлен на склад {self.name} в количестве {x}")

	def to_office(self, x):
		for i in self.warehouse:
			if i.get(self.name):
				i[self.name] = i.get(self.name) - x
				print(f"Доставлен в офис {self.name} в количестве {x}")


class Printer(OfficeEquipment):
	def __init__(self, name, amount, print_speed):
		super().__init__(name, amount)
		self.print_speed = print_speed


class Scaner(OfficeEquipment):
	def __init__(self, name, amount, max_format):
		super().__init__(name, amount)
		self.max_format = max_format


class Xerox(OfficeEquipment):
	def __init__(self, name, amount, speed):
		super().__init__(name, amount)
		self.speed = speed


wh = WarehouseOfficeEquipment()
a = Printer("HP-Printer", 10, 30)
b = Scaner("Canon-Scaner", 5, 10)
c = Xerox("HP-Xerox", 7, 20)
print(f"Изначальное состояние склада:\n\t{wh.warehouse}")
a.to_office(2)
b.to_office(3)
print(f"Состояние склада после перемещения:\n\t{wh.warehouse}")
b.to_warehouse(1)
print(f"Состояние склада после перемещения:\n\t{wh.warehouse}")

d = Scaner("Canon-Scaner", "пять", 10)  # Проверка валидизации данных
