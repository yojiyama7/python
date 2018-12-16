N = int(input())

v = 2025-N
for i in range(1, 10):
    if v%i == 0 and v//i <= 9:
        print(i, "x", v//i)

    