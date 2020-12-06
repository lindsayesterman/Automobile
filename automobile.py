class Automobile():
	autocount = 0
	def __init__(self, auto_name = "", speed = 0):
		self.auto_name = auto_name
		self.speed = speed
		autocount += 1
	def __str__(self):
		return ("Automobile has a self.auto_name = " + str(self.auto_name) + " and a self.speed = " + str(self.speed))
	def speed_up():
		self.speed += 1
        return self.speed
    def slow_down():
    	self.speed -= 1
    	return self.speed

class Hummer(Automobile):
	def __init__(self, auto_name, speed, auto_ID):
		Automobile.__init__(self, auto_name, speed)
		self.auto_ID = auto_ID
	def __str__(self):
		return ("auto_ID = " + str(self.auto_ID) +  " " + Automobile.__str__(self))
	def quick_break():
		self.speed -= 10
		return self.speed
