#L09T02 
r = " "
filename = "Lab09_Tiedostot/nimet.txt"
try:
    with open(filename, "r") as rivit:
        for line in sorted(rivit):
            print(line, end = " ")
            rivit.close()
except FileNotFoundError:
    print("Tapahtui virhe")