# a, b, c, d = map(int, input().split(" "))

# if b/a > d/c:
# 	print("TAKAHASHI")
# elif b/a < d/c:
# 	print("AOKI")
# else:
# 	print("DRAW")

a,b,c,d=map(int,input().split());print([["DRAW","AOKI"][b/a<d/c],"TAKAHASHI"][b/a>d/c])