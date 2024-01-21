import sys
from collections import Counter
#L09T04
#Ladattu tiedosto names.txt nimellä koska aiemmassa tehtävässä luotu nimi.txt
count = 0
nimet ={}
args: list[str] = sys.argv
filename="Lab09_tiedostot/names.txt"
try: 
    file=open(filename, "r")
    for line in file:
        nimi = line.strip()
        count=count+1
        if nimi in nimet:
            nimet[nimi]=nimet[nimi]+1
        else:
            nimet[nimi]=1

except FileNotFoundError:
    print("Tapahtui virhe")

for nimi, y in nimet.items():
    print("Nimi: ", nimi, " esiintyy", y, " kertaa")

file.close()

