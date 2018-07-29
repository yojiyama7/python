hw1, hw2 = [tuple(map(int, input().split(" "))) for i in range(2)]

print("YES" if 0 < len(set(hw1) & set(hw2)) else "NO")