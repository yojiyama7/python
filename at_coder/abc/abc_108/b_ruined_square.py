x1, y1, x2, y2 = map(int, input().split(" "))

x_dif = x2 - x1
y_dif = y2 - y1
print(x2-y_dif, y2+x_dif, x1-y_dif, y1+x_dif)

# print(x2-y2-y1, y2+x2-x1, x1-y2-y1, y1+x2-x1)