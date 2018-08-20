w = input()
print("No" if sum(w.count(c) % 2 for c in set(w)) else "Yes")

# w=input();print("YNeos"[sum(w.count(c)%2for c in w)!=0::2])