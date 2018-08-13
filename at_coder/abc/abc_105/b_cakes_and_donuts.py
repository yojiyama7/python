n = int(input())

while 0 <= n:
    if n%4 == 0:
        print("Yes")
        exit()
    else:
        n -= 7
print("No")