n = int(input())

center = int(n**(1/2))

for i in range(center+1):
    if n % (center - i) == 0:
        print(len(str(n // (center - i))))
        exit()