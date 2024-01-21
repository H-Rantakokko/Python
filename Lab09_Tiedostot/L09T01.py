#L09T01

filename="Lab09_Tiedostot/nimet.txt"
file = open(filename, "w")
try:
    while True:
        nimi = input("Anna nimi: ")
        if nimi.isspace():
            break
        else :
            file.writelines(nimi+"\n")
            file.flush()
    file.close()
except FileNotFoundError:
    print("Tapahtui virhe")
