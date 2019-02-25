from itertools import product

N, *ABC = map(int, input().split(" "))
L = [int(input()) for _ in range(N)]

min_num = 10**18
for i in range(4**N):
    abcz = [[] for _ in range(4)]
    for j in range(N):
        abcz[i//(4**j)%4].append(L[j])
    if [] in abcz[:3]:
        continue
    # print(abcz)
    m = 0
    for l, x in zip(abcz, ABC): 
        m += 10*(len(l)-1) + abs(sum(l)-x)
    # if m < min_num:
    #     print(abcz, m)
    min_num = min(min_num, m)

print(min_num)

################################

# from itertools import combinations, permutations, accumulate
# from functools import lru_cache

# N, A, B, C = map(int, input().split(" "))
# L = [int(input()) for _ in range(N)]

# # O(1)
# def f(a):
#     s, l, x = a
#     return (l-1)*10+abs(s-x)

# min_num = 10**18
# # オーダー数: O(N! * (N C 3) * 3)
# for l in permutations(L):
#     # print(l)
#     m = [0] + list(accumulate(l))
#     # オーダー数: O((N C 3) * 1)
#     for j1, j2, j3 in combinations(range(N), 3):
#         # O(1)
#         sum_num = sum(map(f, [
#             (m[j2]-m[j1], j2-j1, A),
#             (m[j3]-m[j2], j3-j2, B),
#             (m[N]-m[j3], N-j3, C)
#         ]))
#         # if sum_num < min_num:
#             # print(l)
#         min_num = min(min_num, sum_num)
 
# print(min_num)

################################

# from itertools import combinations, permutations, accumulate
# from functools import lru_cache

# N, A, B, C = map(int, input().split(" "))
# L = [int(input()) for _ in range(N)]

# l = [0] + list(accumulate(L))
# print(l)

# # @lru_cache(maxsize=None)
# def f(s, l, x):
#     return (l-1)*10+abs(s-x)

# min_num = 10**18
# for l_i in permutations(L):
#     for i in range(N):
#         for j in range(i+1, N):
#             for k in range(j+1, N):
#                 print(i, j, k)
#                 m = [
#                     f(l[j]-l[i], j-i, A),
#                     f(l[k]-l[j], k-j, B),
#                     f(l[N]-l[k], N-k, C),
#                 ]
#                 print(m)
#                 min_num = min(min_num, sum(m))

# print(min_num)