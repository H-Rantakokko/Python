#L08T05
from random import randint

def Lotto():
    lottorivi = []
    rivi = 0
    while 7 >  rivi:
        numero = randint(1, 40)
        if numero not in lottorivi:
            rivi += 1
            lottorivi.append(numero)
    return str(lottorivi)

print(Lotto())