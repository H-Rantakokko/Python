#L04T02
päivät = 7 
sademäärä = 0
for z in range(päivät):
    tulos = int(input("Anna sademäärä: "))
    z +=1
    if tulos > -1:
        sademäärä += tulos  
print(sademäärä)
