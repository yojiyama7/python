A, B = map(int, input().split(" "))

f = lambda x: int("".join(x))

a = list(str(A))
for i in range(3):
    if a[i] != "9":
        a[i] = "9"
        break
a = f(a)

b = list(str(B))
if b[0] != "1":
    b[0] = "1"
else:
    for i in range(1,3):
        if b[i] != "0":
            b[i] = "0"
            break
b = f(b)

if (a-A) > (B-b):
    print(a-B)
else:
    print(A-b)