import datetime as dt


class Data:
	def __init__(self, day, month, year):
		self.date = f'{day}-{month}-{year}'

	@classmethod
	def date_to_int(cls, day, month, year):
		return int(day), int(month), int(year)

	@staticmethod
	def is_valid(day, month, year):
		return True if 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999 else False


a = Data("12", "2", "2020")
print(a.date)
print()
print(Data.date_to_int("14", "03", "2021"))
for el in Data.date_to_int("14", "03", "2021"):
	print(type(el))
print()
print(Data.is_valid(5, 12, 2064))
print(Data.is_valid(0, 0, 1235466))
