from datetime import datetime

S = input()

year, month, day = map(int, S.split("/"))

print(["TBD", "Heisei"][datetime(year, month, day)<=datetime(2019, 4, 30)])