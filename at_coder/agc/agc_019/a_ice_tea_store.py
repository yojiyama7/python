Q, H, S, D = map(int, input().split(" "))
N = int(input())

one = min(Q*4, H*2, S)
two = min(one*2, D)

print(two*(N//2)+one*(N%2))