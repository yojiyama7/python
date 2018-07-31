a, b = [int(input()) for i in range(2)]

print(min(abs(a-b), 10-abs(a-b)))