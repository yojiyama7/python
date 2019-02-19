N = int(input())
A = list(map(int, input().split(" ")))

print(["YES","NO"][sum(A)%2])