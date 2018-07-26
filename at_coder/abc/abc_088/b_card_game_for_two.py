n = int(input())
a = [int(m) for m in input().split(" ")]

a.sort(reverse=True)
print(sum(a[::2]) - sum(a[1::2]))