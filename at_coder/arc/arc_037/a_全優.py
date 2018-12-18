N = int(input())
M = list(map(int, input().split(" ")))

print(sum(map(lambda x: max(0, 80-x), M)))