# 0-Bまでの範囲 - 0-Aまでの範囲 というやり方はあり。
# 特定の整数範囲で求められた場合この方法が応用が利きそう

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

A, B, C, D = map(int, input().split(" "))

c_count = (B//C)-(-(-A//C))+1
# print(c_count)

d_count = (B//D)-(-(-A//D))+1
# print(d_count)

cd_lcm = lcm(C, D)
# print(cd_lcm)
cd_count = (B//cd_lcm)-(-(-A//cd_lcm))+1
# print((B//cd_lcm), (-(-A//cd_lcm)))


print(B-A+1 - c_count - d_count + cd_count)