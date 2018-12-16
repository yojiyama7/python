# 最小の方が重要?な気がする

N = int(input())
D = [int(input()) for _ in range(N)]

if N==1:
    print(D[0])
    print(D[0])
    exit()

d_sum = sum(D)

print(d_sum)
print(max(0, 2*max(D)-d_sum))