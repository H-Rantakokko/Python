#L07T04
class Mobile:
    brand = " "
    model = " "
    price = 0
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)

    def __init__(self, brand, model, price ):
        self.brand = brand
        self.model = model
        self.price = price

phone1 = Mobile("Samsung", "Galaxy", 349) 
print(phone1)  

phone2 = Mobile("Apple", "Iphone 12", 899)
print(phone2)