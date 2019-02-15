# N, M = map(int, input().split(" "))

# if N*2 <= M <= N*4:
#     d = {2: 0, 3: 0, 4: 0}
#     a = -(-M//N)
#     d[a] = (M-1)%N+1
#     d[a-1] = N-d[a]
#     # print(a, d)
#     print("{} {} {}".format(d[2], d[3], d[4]))
# else:
#     print("-1 -1 -1")