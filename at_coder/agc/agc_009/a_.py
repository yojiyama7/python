# from fractions import gcd

N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]

round_up = lambda a, b: -(-a//b)

c = 0
for a, b in AB[::-1]:
    # print(a, b)
    # lcm_ab = a*b//gcd(a, b)
    # print(round_up(a+c, lcm_ab), lcm_ab, a+c)
    r = round_up(a+c, b)*b - (a+c)
    # print(r)
    c += r

print(c)