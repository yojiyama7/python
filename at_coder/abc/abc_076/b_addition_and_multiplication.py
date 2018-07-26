n = int(input())
k = int(input())

int_1 = 1
for i in range(n):
    if int_1 < k:
        int_1 *= 2
    else:
        int_1 += k
print(int_1)