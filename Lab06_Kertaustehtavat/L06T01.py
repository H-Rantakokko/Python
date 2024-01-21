import datetime

#L06T01
def showtime(a):
    seconds = round(a % (24 * 3600),2)
    hour = round(a // 3600, 2)
    a %= round(3600, 2)
    minutes = round(a // 60, 2)
    a %= round(60, 2)

    return "%d:%02d:%02d" % (hour, minutes, seconds)
    

print(showtime(500))
print(showtime(10000))
print(showtime(121000))