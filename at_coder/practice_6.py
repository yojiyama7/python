n = int(input())
a = [int(n) for n in input().split(" ")]

a.sort()

print(sum(a[::-2]) - sum(a[-2::-2]))