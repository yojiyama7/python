N, L = map(int, input().split(" "))
A = [input() for _ in range(L)]
Y = input()

x = (Y.find("o"))//2
for y in range(L-1, -1, -1):
    line = A[y]
    if x > 0 and line[x*2-1] == "-":
        x -= 1
    elif x < N-1 and line[x*2+1] == "-":
        x += 1

print(x+1)