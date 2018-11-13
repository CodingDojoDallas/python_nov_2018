class Product:
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def tax(self):
        self.price = self.price + self.price*.08
        return self

    def return_item(self,reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price = price - price*.20
        return self

    def display_all(self):
        print("Price: " + str(self.price))
        print("Item Name: " + str(self.item_name))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Status: " + str(self.status))
        return self

product1 = Product(1, "apple", 5, "dole", "for sale")
product1.display_all()
product1.tax().display_all()