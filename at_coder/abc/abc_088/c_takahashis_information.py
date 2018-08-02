c = [tuple(map(int, input().split(" "))) for i in range(3)]

c_rotated = zip(*c)
c_rotated = [[n-min(v_line) for n in v_line] for v_line in c_rotated]
c = zip(*c_rotated[::-1])
c = [[n-min(line) for n in line] for line in c]
print("No" if any([any(c_i) for c_i in c]) else "Yes")