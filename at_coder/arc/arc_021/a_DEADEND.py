A = [list(map(int, input().split(" "))) for _ in range(4)]

for _ in range(2):
    for a in A:
        for i in range(3):
            if a[i] == a[i+1]:
                print("CONTINUE")
                exit()
    A = zip(*A)
print("GAMEOVER")