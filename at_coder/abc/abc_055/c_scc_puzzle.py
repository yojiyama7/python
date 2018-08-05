n, m = map(int, input().split(" "))

first = min(n, m//2)
second = max(0, m-2*first)//4
print(first + second)