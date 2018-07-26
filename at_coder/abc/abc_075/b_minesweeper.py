h, w = [int(m) for m in input().split(" ")]
s = [input() for i in range(h)]

s = [[{".": 0, "#": 10}[c] for c in line] for line in s]

for h_i in range(h):
    for w_i in range(w):
        if 10 <= s[h_i][w_i]:
            for y in range(h_i-1, h_i+2):
                for x in range(w_i-1, w_i+2):
                    if 0 <= y < h and 0 <= x < w:
                        s[y][x] += 1

print("\n".join(["".join(["#" if 10 <= c else str(c) for c in line]) for line in s]))