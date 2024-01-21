#L10T01
saldo = 2000

print("Bank account balance: ", saldo)
saldo += int(input("How many euros will be added to the balance? "))
desimaalit = float(input("How many sents will be added to the balance? "))
vastaus=(desimaalit/100)
saldo += vastaus
print("Bank account balance: ", saldo)