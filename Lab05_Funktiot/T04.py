#L05T04
def get_fuel(f, g):
  return "{:.1f}".format(g*f/100)
print(str(get_fuel(100, 7.5))+ " ltr")
print(str(get_fuel(220, 6.9))+" ltr")