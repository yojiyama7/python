a, b = input().split(" ")

c_n = {"H":1, "D":-1}
print("H" if 0 < c_n[a] * c_n[b] else "D")