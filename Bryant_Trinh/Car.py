class Car:
	def __init__(self,price,speed,fuel,mileage):
		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.mileage=mileage
		if price>10000:
			tax=.12
		else:
			tax=.15

	def displayall(self):
		print("Price: " +self.price)
		print("Speed: " + self.speed + "mph")
		print("Fuel: " + self.fuel)
		print("Mileage" + self.mileage + "mpg")
		print("Tax: " + self.tax)

car1 = Car(20000,80,"full",40)
car2 = Car(9000,50,"kind of full",15)
car3 = Car(5000,30,"half empty",35)
car4 = Car(30000,120,"kind of empty",20)
car5 = Car(15000,70,"half full",30)
car6 = Car(6000,40,"empty",10)


car1.displayall()
car2.displayall()
car3.displayall()
car4.displayall()
car5.displayall()
car6.displayall()
