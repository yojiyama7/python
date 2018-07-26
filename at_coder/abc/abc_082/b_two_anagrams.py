import sys
from itertools import zip_longest

s = input()
t = input()

s_ = sorted(list(s))
t_ = sorted(list(t))
st_ = sorted([s_, t_])

if s_ == t_:
    print("No")
elif st_[0] == s_:
    print("Yes")
else:
    print("No")