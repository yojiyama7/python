n = int(input())
a, b = input().split(" ")
k = int(input())
p = input().split(" ")

citys = [a] + p + [b]
print("YES" if len(set(citys)) == len(citys) else "NO")