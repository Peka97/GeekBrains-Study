import time


class TrafficColor:
	__color = ""

	def running(self):
		while True:
			self.__color = "redlight"
			print(self.__color)
			time.sleep(7)
			self.__color = "yellowligth"
			print(self.__color)
			time.sleep(2)
			self.__color = "greenligth"
			print(self.__color)
			time.sleep(5)
			self.__color = "yellowligth"
			print(self.__color)
			time.sleep(2)


a = TrafficColor()
a.running()
