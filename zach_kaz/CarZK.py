class Car:
    def __init__(self,price, speed, fuel, mileage):
        self.Price=price
        self.Speed=speed
        self.Fuel=fuel
        self.Mileage=mileage
        if price>10000:
            self.tax=(.15)
        else:
            self.tax=(.12)
    def display_all(self):
        print("Price: $"+(str(self.Price)))
        print("Speed: "+str(self.Speed)+"mph")
        print("Fuel: "+self.Fuel)
        print("Mileage: "+str(self.Mileage)+"mpg")
        print("Tax: "+str(self.tax))

Corvette=Car(1000000,1000,'full',23)
Corvette.display_all()
Lemon=Car(150000,3,"none",6)
Lemon.display_all()
Escalade=Car(80000,60,"none",1)
Escalade.display_all()
Tesla=Car(300000,120,"electric","infinite")
Tesla.display_all()
Civic=Car(20000,80,"half",37)
Civic.display_all()
Bike=Car(500,20,"did you eat lunch?","infinite")
Bike.display_all()
