n = int(input())
t = list(map(int, input().split(" ")))
m = int(input())
p_x = [tuple(map(int, input().split(" "))) for i in range(m)]

for i in range(m):
    t_ = t[:p_x[i][0]-1] + [p_x[i][1]] + t[p_x[i][0]:]
    print(sum(t_))
