class Automobile():
	autocount = 0
	def __init__(self, auto_name = "", speed = 0):
		self.auto_name = auto_name
		self.speed = speed
		#autocount += 1
	def __str__(self):
		return ("Automobile has a self.auto_name = " + str(self.auto_name) + " and a self.speed = " + str(self.speed))
	def speed_up(self, inc):
		self.speed += inc
		return self.speed
	def slow_down(self, dec):
		self.speed -= dec
		return self.speed

class Hummer(Automobile):
	def __init__(self, auto_name, speed, auto_ID):
		Automobile.__init__(self, auto_name, speed)
		self.auto_ID = auto_ID
	def __str__(self):
		return (Automobile.__str__(self) + " auto_ID = " + str(self.auto_ID))
	def quick_break(self):
		self.speed -= 10
		return self.speed

def main():
	car_list = []
	print(Automobile("Red Audi", 0))
	print(Hummer("Blue Hummer", 0, " H3"))
	car_list.append(Automobile("Red Audi", 0))
	car_list.append(Hummer("Blue Hummer", 0, " H3"))
	for c in car_list:
		print(c)
		print(c.speed_up(10))
		if isinstance(c, Hummer):
			print(c.quick_break())
main()

