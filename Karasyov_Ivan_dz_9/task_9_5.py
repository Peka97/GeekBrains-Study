class Stationery:
	def __init__(self, title):
		self.title = title

	def draw(self):
		print("Запуск отрисовки")


class Pen(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f"Запуск отрисовки c помощью инструмента \"{self.title}\"")


class Pencil(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f"Запуск отрисовки c помощью инструмента \"{self.title}\"")


class Handle(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f"Запуск отрисовки c помощью инструмента \"{self.title}\"")


a = Stationery("Краски")
a.draw()
pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
