# n = int(input())

# print("Yes" if n % sum([int(m) for m in str(n)]) == 0 else "No")

# n=int(input());print("Yes"if n%sum([int(m)for m in str(n)])==0 else"No")
# n=int(input());print("No"if n%sum(map(int,str(n))) else"Yes")
# s=input();print("YNeos"[bool(int(s)%sum(map(int,s)))::2])
# s=input();print("No"if int(s)%sum(map(int,s))else"Yes")
s=input();print("YNeos"[int(s)%sum(map(int,s))!=0::2])