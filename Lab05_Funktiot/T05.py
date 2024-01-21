#L05T05
def get_cost(h, i, j):
  return "{:.2f}".format(h*i/100*j)
print(str(get_cost(100, 7.5, 1.88 ))+ " €")
print(str(get_cost(220, 6.9, 1.88 ))+ " €")
