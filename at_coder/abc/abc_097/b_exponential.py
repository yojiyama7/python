x = int(input())

for x_i in range(x, 0, -1):
    for j in range(2, max(3, x_i)):
        n = 0
        while n**j < x_i:
            n += 1
        if n**j == x_i:
            print(x_i)
            exit()