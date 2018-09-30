# n = int(input())
# s = input()

# acce = "b"
# page = 0
# while len(acce) < len(s):
#     add_char = "acbcab"[page%3::3]
#     acce = add_char[0] + acce + add_char[1]
#     page += 1
# print(page if acce == s else -1)

# n=int(input());s=input();print([-1,n//2][n%2*all(set(a)in[{"a","c"},{"b"}]for a in zip(s,s[::-1]))])

# n=int(input());s=input();print(s[::3],s[1::3],s[2::3])
n=int(input());s=input();print([-1,n//2][n%2*all(s[i]=="bca"[(n//2+i)%3]for i in range(n))])
# atcoderだとエラー
# n=int(input());s=input();print([-1,n//2][n%2*all({*a}in[{"a","c"},{"b"}]for a in zip(s,s[::-1]))])
