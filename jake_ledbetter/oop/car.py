class Car:
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		if price > 10000:
			self.tax = 15
		else:
			self.tax = 12
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.displayInfo()
	def displayInfo(self):
		print("Price: " + str(self.price))
		print("Speed: " + str(self.speed))
		print("full: " + self.fuel)
		print("Mileage: " + str(self.mileage))
		print("Tax: " + str(self.tax))
		print(" ")
car1 = Car(1000,90,"full",15)
car2 = Car(500, 70, "empty", 18)
car3 = Car(50000, 130, "half-full", 34)
car4 = Car(3000, 100, "full", 20)
car5 = Car(10020,110,"empty",30)
car6 = Car(4000, 70, "half-empty",20)