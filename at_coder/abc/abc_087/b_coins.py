a, b, c, x = [int(input()) for i in range(4)]

same_count = 0
for a_i in range(a+1):
    for b_i in range(b+1):
        for c_i in range(c+1):
            if 500*a_i + 100*b_i + 50*c_i == x:
                same_count += 1

print(same_count)