#L10T05
try:
    filename = "C/käyttäjä/omistaja/ttc2030/Lab09_tiedostot/ayho.txt"
    file=open(filename, "w")
    file.writeline("Testi")
    file.flush()
    file.close()
except FileNotFoundError:
    print("Tapahtui virhe!")
