from datetime import date, timedelta

Y, M, D = map(int, input().split("/"))

t = date(Y, M, D)
while True:
    y, m, d = t.year, t.month, t.day
    if y/m/d%1 == 0:
        print("{0}/{1:0>2}/{2:0>2}".format(y, m, d))
        exit()
    t += timedelta(1)