#L09T05
from random import randint


def Lotto():
    lottorivi = []
    rivi = 0
    while 7 >  rivi:
        numero = randint(1, 40)
        if numero not in lottorivi:
            rivi += 1
            lottorivi.append(numero)
    return lottorivi                    

rivit=int(input("Kuinka monta riviä? "))

filename="Lab09_tiedostot/lotto.txt"
file = open(filename, "w")
try:
    for x in range(rivit):
        lottorivi = str(Lotto())
        file.writelines(lottorivi)
        file.flush()
        print(lottorivi)

except FileNotFoundError:
    ("Tapahtui virhe")

file.close()