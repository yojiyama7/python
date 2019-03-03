from itertools import permutations as p

n = int(input())
k = int(input())
a = [int(input()) for _ in range(n)]

print(len(set(map(lambda x: "".join(map(str, x)), p(a, k)))))

################################

# from itertools import permutations

# n = int(input())
# k = int(input())
# cards = [input() for _ in range(n)]

# print(len(set("".join(p) for p in permutations(cards, k))))