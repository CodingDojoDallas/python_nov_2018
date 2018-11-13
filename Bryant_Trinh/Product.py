class shoes:
	def __init__(self,price,name,weight,brand,status):
		self.price=price
		self.name=name
		self.weight=weight
		self.brand=brand
		self.status=status

	def sell(self):
		self.status="Sold"
		return self

	def addtax(self):
		tax=.1
		self.price+=(price*tax)
		return self

	def returnitem(self,reason):
		if reason == "defective":
			self.price=0
			self.status="Defective"
		if reason == "like_new":
			self.status="For Sale"
		if reason == "opened":
			self.status="Used"
			self.price*=.8
		return self

	def displayinfo(self):
		print("$"+self.price)
		print(self.brand +" "+ self.name)
		print(self.weight + "lbs")
		print(self.status)

shoe1 = Shoe(180, "nmd", 1.2, "adidas", "For sale")
shoe2 = Shoe(50, "freerun", 1.1, "nike", "For sale")
shoe3 = Shoe(100, "wingtip", 2, "aldo", "For sale")
		
shoe1.displayinfo()
shoe2.addtax().sell().displayinfo()
shoe3.returnitem("opened").displayinfo()