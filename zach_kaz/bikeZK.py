class Bike:
    def __init__(self,price,max_speed,miles):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
    def displayInfo(self):
        print("Bike specs:"+" $"+str(self.price)+", "+str(self.max_speed)+"mph, "+str(self.miles)+"miles")
        return self
    def ride(self):
        print("Riding")
        self.miles+=10
        return self
    def reverse(self):
        print("Reversing")
        self.miles-=5

ZachBike=Bike(1000,100,0)
JohnBike=Bike(5,10,100)
BobBike=Bike(55,55,55)
ZachBike.ride()
ZachBike.ride()
ZachBike.ride()
ZachBike.reverse()
ZachBike.displayInfo()
JohnBike.ride()
JohnBike.ride()
JohnBike.reverse()
JohnBike.reverse()
JohnBike.displayInfo()
BobBike.reverse()
BobBike.reverse()
BobBike.reverse()
BobBike.displayInfo()