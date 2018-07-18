import sys
# n, m = map(int, input().split())
n, m = 5, 3
# x = [map(int, line.split()) for line in sys.stdin.readlines()]
# xyz_list = [[int(str_) for str_ in input().split(" ")] for i in range(n)]
xyz_list =[
	[3, 1, 4], # 8
	[1, 5, 9], # 15
	[2, 6, 5], # 13
	[3, 5, 8], # 15
	[9, 7, 9]  # 25
] # 56
x_list, y_list, z_list = zip(xyz_list)

# min: -14, max: 15, sa: 1
  1  -2   3 #  4  -2   2
 -4   5  -6 #  5 -10  -5 
  7  -8  -9 #  7 -17 -10 
-10  11 -12 # 11 -22 -11 
 13 -14  15 # 28 -14  14
# 54
