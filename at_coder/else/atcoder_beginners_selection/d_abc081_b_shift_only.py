# def count_two(x):
#     c = 0
#     while x%2 == 0:
#         x //= 2
#         c += 1
#     return c
count_two = lambda x: bin(x)[::-1].find("1")

N = int(input())
A = list(map(int, input().split(" ")))

print(min(map(count_two, A)))