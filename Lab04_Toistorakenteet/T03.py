#L04T03
lukujenmäärä=0
lukujensumma=0
while True:
    try:
        annettu_luku = int(input("Anna luku: "))
        lukujensumma += annettu_luku
        lukujenmäärä += 1
        continue
    except ValueError:
        break

print("Lukuja ennettu :", lukujenmäärä)
print("Lukujen summa: ", lukujensumma)
