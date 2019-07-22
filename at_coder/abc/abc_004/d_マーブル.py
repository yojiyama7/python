R, G, B = map(int, input().split(" "))

def sum_1_to_a(a):
    return int((a+1)*(a/2))

def solve_cost(num, center):
    return sum_1_to_a(center) + sum_1_to_a(num-center-1)

min_cost = 10**18
for r_i in range(R+300):
    for g_i in range(G):
        for b_i in range(B+300):
            if -100+(R-r_i-1) < 0-g_i and G-g_i-1 < 100-r_i:
                min_cost = min(
                    min_cost,
                    solve_cost(R, r_i)+solve_cost(G, g_i)+solve_cost(B, b_i)
                )
                # print(r_i, g_i, b_i, min_cost)

print(min_cost)