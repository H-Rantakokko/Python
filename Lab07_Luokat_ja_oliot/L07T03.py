#LO7T03
class Cat:
    name=" "
    color=" "
    def __str__(self):
        return self.name + " " + "color: " + self.color

    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    
    def meoow(name):
        text = name +" says "+"Meooooow!"
        return text


kissa1=Cat("Kit", "black")
print(kissa1)

kissa2=Cat("Kat", "white")
print(kissa2)

print(Cat.meoow("Kit"))
print(Cat.meoow("Kat"))