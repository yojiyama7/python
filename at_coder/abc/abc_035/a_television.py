w, h = map(int, input().split(" "))

print("16:9" if w/h == 16/9 else "4:3")