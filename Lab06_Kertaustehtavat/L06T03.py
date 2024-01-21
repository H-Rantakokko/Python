#L06T03
namelist= [ ]
nimimäärä = 0
nimi = ""
while True:
    nimi = input("Anna oppilaan nimi: ")
    if nimi.isspace():
        break
    
    else:
        namelist.append(nimi)
        nimimäärä +=1
           
print(namelist)
print("Oppilaita on ", nimimäärä)
    

