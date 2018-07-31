n = int(input())
a = [int(input()) for i in range(n)]

print(sorted(list(set(a)), reverse=True)[1])