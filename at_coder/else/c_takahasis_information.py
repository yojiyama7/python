grid_data = [[int(j) for j in input().split(" ")] for i in range(3)]

for i, c_list in enumerate(grid_data):
    grid_data[i] = [c - max(grid_data[i]) for c in c_list]

if all([True if grid_data[0] == c_list else False for c_list in grid_data]):
    print("Yes")
else:
    print("No")