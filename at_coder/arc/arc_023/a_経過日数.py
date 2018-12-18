# こうなるよなぁ
from datetime import date

Y, M, D = [int(input()) for _ in range(3)]

print((date(2014, 5, 17)-date(Y, M, D)).days)