x, y = map(int, input().split(" "))

a = [y-x, y-(-x)+1, (-y)-x+1, (-y)-(-x)+2]
a = list(filter(lambda x: x >= 0, a))
print(min(a))

################################

# x,y=map(int,input().split());print(min(list(lambda x:x>=0,filter([y-x,x+y+1,1-y-x,2+x-y]))))
# x,y=map(int,input().split());print(min(a for a in[y-x,x+y+1,1-y-x,2+x-y]if a>=0))