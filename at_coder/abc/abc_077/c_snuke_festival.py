import bisect

n = int(input())
abc = [tuple(map(int, input().split(" "))) for i in range(3)]
# n = 100000
# abc = [tuple(range(n)) for i in range(3)]

a, b, c = [sorted(abc_i) for abc_i in abc]

print(sum(bisect.bisect_left(a, b_i) * (n-bisect.bisect_right(c, b_i)) for b_i in b))