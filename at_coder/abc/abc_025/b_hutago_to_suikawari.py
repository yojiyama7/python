n, a, b = map(int, input().split(" "))
sd = [input().split(" ") for i in range(n)]

pos = 0
for sd_i in sd:
    s, d = sd_i[0], int(sd_i[1])
    if d < a:
        walk_size = a
    elif d > b:
        walk_size = b
    else:
        walk_size = d
    pos += (1 if s == "East" else -1)*walk_size
if pos > 0:
    print("East", pos)
elif pos < 0:
    print("West", abs(pos))
else:
    print(0)