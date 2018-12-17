day = input()

if day[0] == "S":
    print(0)
else:
    print(["Fri", "Thurs", "Wednes", "Tues", "Mon"].index(day[:-3])+1)