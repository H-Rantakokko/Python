#L08T02
lista2 =[]
while True:
    rekisterinumero = input("Anna rekisterinumero: ")
    lista2.append(rekisterinumero)
    if rekisterinumero.isspace():
        lista2.remove(rekisterinumero)
        break
    else:
        continue

lista2.sort()
print(lista2)