r_str, g_str, b_str = input().split(" ")

print("YES" if int(g_str+b_str)%4 == 0 else "NO")