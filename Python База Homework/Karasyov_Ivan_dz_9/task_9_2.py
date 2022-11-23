class Road:
	def __init__(self, length, width):
		self._length = length
		self._width = width

	def asphalt(self):
		return self._length*self._width*25*5


a = Road(10, 20)
print(a._length)
print(a._width)
print(a.asphalt())
