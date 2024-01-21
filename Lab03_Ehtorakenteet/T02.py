#LO3T02
c = int(input("Anna kokonaisluku: "))
d = int(input("Anna toinen kokonaisluku: "))
e = int(input("Anna kolmas kokonaisluku: "))
if c < d and  d > e:
    print(f"Suurin: {d}")
elif d < c and c > e:
    print(f"Suurin: {c}")
elif c < e and e > d:
    print(f"Suurin: {e}")
else:
    print("Virhe!")
