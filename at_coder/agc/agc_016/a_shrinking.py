S = input()

min_cost = 10**18
for c in set(S):
    cost = max(map(len, S.split(c)))
    min_cost = min(min_cost, cost)

print(min_cost)