from copy import deepcopy

ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

A = [list(input()) for _ in range(10)]

def is_one_island(t, this_pos):
    b = deepcopy(t)
    b[this_pos[1]][this_pos[0]] = "o"
    dfs(b, this_pos)
    for line in b:
        if "o" in line:
            return False
    return True

def dfs(t, this_pos):
    this_x, this_y = this_pos
    t[this_y][this_x] = "x"
    for ad_x, ad_y in ADS:
        pos = x, y = this_x+ad_x, this_y+ad_y
        if not (0<=x<10 and 0<=y<10):
            continue
        if t[y][x] == "x":
            continue
        dfs(t, pos)

for y in range(10):
    for x in range(10):
        if is_one_island(A, (x, y)):
            print("YES")
            exit()
print("NO")