#L07T05
class Car:
    def __str__(self):
        return "auto: " + self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def yhteensä(price1, price2, price3):
        yhteensä = price1 + price2 + price3
        return "Autojen hinta yhteensä: " + str(yhteensä)

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)
yhteensä=Car.yhteensä(3000, 4000, 5000)       

print(car1)
print(car2)
print(car3)
print(yhteensä)
