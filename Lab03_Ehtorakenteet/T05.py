#LO3T05
y = 1
vastaus = 0
while y < 6:
    x = int(input("Anna " + str(y) +". luku: "))
    y += 1
    if x > 0:
        vastaus += x 
    else:
        continue

print("Lukujen summa on: ", vastaus)
