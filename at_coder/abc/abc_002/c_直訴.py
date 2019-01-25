xa, ya, xb, yb, xc, yc = map(int, input().split(" "))

xa, xb = [x-xc for x in (xa, xb)]
ya, yb = [y-yc for y in (ya, yb)]

print(abs(xa*yb-xb*ya)/2)