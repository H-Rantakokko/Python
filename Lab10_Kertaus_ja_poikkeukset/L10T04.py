#L10T04
try: 
    lista = [ "Omena", "Päärynä", "Persikka", "Mango"]
    lista[4] = "Mustikka"
except IndexError:
    print("Tapahtui virhe")