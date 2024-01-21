#L08T03
lista3 =[]
määrä=0
while True:
    try:
        arvosana = int(input("Anna arvosana: "))
        if arvosana == 5 or arvosana == 0 or arvosana > 0 and arvosana < 5:
            lista3.append(arvosana)
            määrä+=1
            continue
        else:
            print("Virhe, arvosanan on oltava väliltä 0-5")

    except ValueError:
            break
    

keskiarvo= sum(lista3)/len(lista3)
print(määrä)
print(keskiarvo)