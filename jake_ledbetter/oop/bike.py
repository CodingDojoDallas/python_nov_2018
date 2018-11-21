class Bike:
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print("price - " + str(self.price) + " max_speed - " + str(self.max_speed) + " miles - " + str(self.miles))
		return self
	def ride(self):
		print("Riding")
		self.miles += 10
		return self
	def reverse(self):
		print("Reversing")
		if self.miles > 4:
			self.miles -= 5
		return self
bike1 = Bike(100, 30)
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike(300, 35)
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(150, 18)
bike3.ride().ride().ride().displayInfo()
