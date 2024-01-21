#L09T03
määrä = 0
filename="Lab09_tiedostot/luvut.txt"
file=open(filename, "w")
try:
    while True:
        try: 
            luku = int(input("Anna luku: ")) 
            luku1 = str(luku)
            file.writelines(luku1)
            määrä += 1
            file.flush()
            continue
        except ValueError:
            break
except FileNotFoundError:
    print("Tapahtui virhe")

print("Lukuja annettu: ", määrä)
kokonaismäärä = str(määrä)
file.writelines(kokonaismäärä)

file.close()
