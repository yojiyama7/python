ABCDE = [int(input()) for _ in range(5)]

ABCDE.sort(key=lambda x: (int(str(x)[-1])-1)%10)

print(ABCDE[0] + sum(-(-x//10)*10 for x in ABCDE[1:]))
