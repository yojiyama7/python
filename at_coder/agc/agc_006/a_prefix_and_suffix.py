N = int(input())
S = input()
T = input()

for i in range(N, -1, -1):
    if S[::-1][:i][::-1] == T[:i]:
        print(N*2-i)
        exit()