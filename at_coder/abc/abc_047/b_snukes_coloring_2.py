w, h, n = map(int, input().split(" "))
x_y_a = [tuple(map(int, input().split(" "))) for i in range(n)]

min_x, max_x, min_y, max_y = 0, w, 0, h
for x_y_a_i in x_y_a:
    x, y, a = x_y_a_i
    if a == 1:
        min_x = max(min_x, x)
    elif a == 2:
        max_x = min(max_x, x)
    elif a == 3:
        min_y = max(min_y, y)
    elif a == 4:
        max_y = min(max_y, y)

print(0 if min_x > max_x or min_y > max_y else (max_x-min_x) * (max_y-min_y))
print(max(0, max_x-min_x) * max(0, max_y-min_y))