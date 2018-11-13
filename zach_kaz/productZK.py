class product:
    def __init__(self,price,item_name,weight,brand):
        self.price=price
        self.name=item_name
        self.weight=weight
        self.brand=brand
        self.status="for sale"
    def sell(self):
        self.status="sold"
        return self
    def addtax(self,tax):
        self.price*=(1+tax)
        return self.price
    def return_item(self,reason_for_return):
        if reason_for_return=="defective":
            self.status="defective"
            self.price=0
            return self
        elif reason_for_return=="like_new":
            self.status="for sale"
            return self
        elif reaon_for_return=="opened":
            self.status="used"
            self.price*=.8
            return self
        else:
            print("This is against our return policy!")
            return self
    def displayInfo(self):
        print("Name: "+self.name)
        print("Price: $"+str(self.price))
        print("Weight: "+str(self.weight)+"lbs")
        print("Brand: "+self.brand)
        print("Item Status: "+self.status)
        return self

#print("ALL DONE")

        
        
