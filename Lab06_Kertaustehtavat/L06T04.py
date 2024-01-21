#L06T04
list=[ ]
sum=0
for x in range(5):
    arvosana=int(input("Hypyn pisteet: "))
    sum += int(arvosana)
    list.append(arvosana)
    tulos = sum-max(list)-min(list)

print("Pisteet yhteensä: ",tulos)
