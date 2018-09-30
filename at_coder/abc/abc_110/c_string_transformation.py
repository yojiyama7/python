s, t = input(), input()

print("Yes" if [t.find(t_i) for t_i in t] == [s.find(s_i) for s_i in s] else "No")
