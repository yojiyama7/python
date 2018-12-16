# 純粋な貪欲法

N = int(input())
NG = [int(input()) for _ in range(3)]

if N in NG:
    print("NO")
    exit()

for i in range(100):
    m = max([0, 1, 2, 3], key=lambda x: [(N-x) not in NG, x])
    if m == 0:
        break
    N -= m
    # print(m, N)
    if N <= 0:
        print("YES")
        exit()
print("NO")