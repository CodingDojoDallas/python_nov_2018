# define class User
class Bike:
    # this method to run every time a new object is instantiated
    def __init__(self, price, max_speed):
	# instance attributes 
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # login method changes the logged status for a single instance (the instance calling the method)
    def displayInfo(self):
        print(self.max_speed)
        print(self.price)
        print(self.miles)
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def ride(self):
        print("Riding")
        self.miles = self.miles + 10
        return self
    # print name and email of the calling instance
    def reverse(self):
        if (self.miles > 5):
            self.miles = self.miles-5
        print("Reversing")
        return self

bike1 = Bike("10", "20")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike("15", "30")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike("25", "50")
bike3.reverse().reverse().reverse().displayInfo()