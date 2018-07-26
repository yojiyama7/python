abc = [int(m) for m in input().split(" ")]
k = int(input())

print(max(abc)*2**k + sum(abc) - max(abc))