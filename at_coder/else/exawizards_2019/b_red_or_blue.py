N = int(input())
S = input()

r = S.count("R")
b = N-r
print(["No", "Yes"][b < r])