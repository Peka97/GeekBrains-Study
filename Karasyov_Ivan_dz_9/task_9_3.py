class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
	def __init__(self, name, surname, position, wage, bonus):
		super().__init__(name, surname, position, wage, bonus)

	def get_full_name(self):
		return self.name, self.surname

	def get_total_income(self):
		return sum(self._income.values())


a = Position("Ivan", "Karasyov", "Developer", 25000, 7000)
b = Position("Kirill", "Zaharenko", "TL", 30000, 10000)
print(a._income)  # Проверка ввода з/п и премии в виде словаря
print(a.get_full_name())  # Проверки работы методов
print(b.get_full_name())
print(a.get_total_income())
print(b.get_total_income())

