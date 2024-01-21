#L08T04

car = {
    "ABC-987":"Chervolet",
    "MNK-456": "Ford",
    "GHJ-753": "Oldsmobile",
    "UIO-852": "Dodge",
    "QWE- 951": "Audi",
    "GHK-842": "Land Rover",
    "LKJ-963": "Volvo",
    "RTY-862": "Mini",
    "JHG-159": "Peugeot",
    "OKN-654": "Mitsubishi",
}
keys=car.keys()
sorted_cars = sorted(car)
sorted_cars = {key:car[key] for key in sorted_cars}
print(sorted_cars)

