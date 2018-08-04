n = int(input())
a = input().split(" ")

print(" ".join((a[1::2][::-1] + a[::2])[::1 if len(a)%2==0 else -1]))
