N = int(input())
V, C = [list(map(int, input().split(" "))) for _ in range(2)]

print(sum([max(0, v-c) for v, c in zip(V, C)]))