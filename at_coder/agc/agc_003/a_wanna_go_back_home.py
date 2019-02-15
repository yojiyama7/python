S = input()

S = set(S)
if 1 not in [len(S&set(t)) for t in ["NS", "WE"]]:
    print("Yes")
else:
    print("No")

################################

# # s=set(input());print("YNeos"[1 in[(len(s&set(t)))for t in["NS","WE"]]::2])
# # s=set;print("NYoe s"[s(input())in map(s,["NS","EW","NSEW"])::2])
# print("NYoe s"[set(input())in map(set,["NS","EW","NSEW"])::2])