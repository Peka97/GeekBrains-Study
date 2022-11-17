class Car:
	def __init__(self, speed: str, color: str, name: str, is_police: bool):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		return "Машина поехала"

	def stop(self):
		return "Машина остановилась"

	def turn(self, side):
		return f"Машина повернула {side}"

	def show_speed(self):
		return self.speed


class TownCar(Car):
	def __init__(self, speed: str, color: str, name: str, is_police: bool):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if self.speed > 60:
			return "Превышение скорости!" if self.speed > 60 else self.speed


class SportCar(Car):
	def __init__(self, speed: str, color: str, name: str, is_police: bool):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		return self.speed


class WorkCar(Car):
	def __init__(self, speed: str, color: str, name: str, is_police: bool):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		return "Превышение скорости!" if self.speed > 40 else self.speed


class PoliceCar(Car):
	def __init__(self, speed: str, color: str, name: str, is_police: bool):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		return self.speed


car = Car(50, "Черный", "Lada", False)
print(car.go())
print(car.turn("направо"))
print(car.turn("налево"))
print(car.show_speed())
print(car.stop())
print()

town_car = TownCar(70, "Бежевый", "Nissan", False)
print(town_car.go())
print(town_car.turn("направо"))
print(town_car.turn("налево"))
print(town_car.show_speed())
print(town_car.stop())
print()

sport_car = SportCar(100, "Красный", "Audi", False)
print(sport_car.go())
print(sport_car.turn("направо"))
print(sport_car.turn("налево"))
print(sport_car.show_speed())
print(sport_car.stop())
print()

word_car = WorkCar(65, "Синий", "Kia", False)
print(word_car.go())
print(word_car.turn("направо"))
print(word_car.turn("налево"))
print(word_car.show_speed())
print(word_car.stop())
print()

police_car = PoliceCar(60, "LSPD", "Renult", True)
print(police_car.go())
print(police_car.turn("направо"))
print(police_car.turn("налево"))
print(police_car.show_speed())
print(police_car.stop())
print()
