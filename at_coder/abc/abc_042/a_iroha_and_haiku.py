abc = list(map(int, input().split(" ")))

print("YES" if sorted(abc) == [5, 5, 7] else "NO")