N = int(input())
ABCDE = [list(map(int, input().split(" "))) for _ in range(N)]

print(max(map(lambda x: sum(x[:4])+(x[4]*(110/900)), ABCDE)))