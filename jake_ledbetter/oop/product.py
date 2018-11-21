class Product:
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self
	def addTax(self, tax):
		self.price = self.price + (self.price * tax)
		return self
	def return_item(self, reason_for_return):
		if reason_for_return == "defective":
			self.status = "defective"
			self.price = 0
		elif reason_for_return == "like new":
			self.status = "for sale"
		elif reason_for_return == "opened":
			self.status = "used"
			self.price = self.price * .8
		return self
	def displayInfo(self):
		print("Item_name: " + self.item_name)
		print("Item price: " + str(self.price))
		print("Item weight: " + str(self.weight))
		print("Item brand: " + self.brand)
		print("Item status: " + self.status)
		print(" ")

candy = Product(10, "candy" , 5, "hershey")
candy.addTax(.08).sell().displayInfo()
candy.return_item("opened").displayInfo()
