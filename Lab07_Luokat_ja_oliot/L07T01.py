#L07T01
import random

class pelikortti:
    
    def __str__(self):
        return self.maa + " " + str(self.arvo)
    def __init__(self, maa, arvo):
        maa = ["Pata","Hertta","Ruutu","Risti"]
        self.maa = random.choice(maa)
        self.arvo = random.randint(1,14)

kortti1 = pelikortti(" ",0)
kortti2 = pelikortti(" ",0)
kortti3 = pelikortti(" ",0)
kortti4 = pelikortti(" ",0)
kortti5 = pelikortti(" ",0)

print(kortti1)
print(kortti2)
print(kortti3)
print(kortti4)
print(kortti5)