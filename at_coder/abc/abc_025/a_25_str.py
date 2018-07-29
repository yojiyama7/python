s = input()
n = int(input())

s = sorted(s)
print(s[(n-1)//5] + s[(n-1)%5])