a, b, c, x, y = map(int, input().split(" "))

print(min(a*x + b*y - (((a+b)-c*2)*min(x, y) if c*2 < a+b else 0), 2*c*max(x,y)))
