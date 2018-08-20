import math

# n = int(input())
# a = list(map(int, input().split(" ")))

# while 0 in a:
#     a.remove(0)
# print(math.ceil((sum(a))/len(a)))

# input()
# a=list(map(int,input().split()))
# while 0 in a:a.remove(0)
# print(math.ceil(sum(a)/len(a)))

# input()
# a=list(map(int,input().split()))
# print(math.ceil(sum(a)/(len(a)-a.count(0))))

n=int(input())
a=input()
print(~-eval(a.replace(" ","+"))//(n-eval("["+a.replace(" ",",")+"]").count(0))+1)