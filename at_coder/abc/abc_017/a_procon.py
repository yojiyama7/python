se = [tuple(map(int, input().split(" "))) for i in range(3)]

print(sum([s_i*e_i for s_i, e_i in se])//10)