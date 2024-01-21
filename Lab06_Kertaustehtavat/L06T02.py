#L06T02
def celToFah(celsius):
    return celsius*1.8+32

def fahToCel(farenheit):
    return round((farenheit-32)/1.8, 1)


print(celToFah(10.0))
print(fahToCel(38.0))
