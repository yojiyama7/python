import sys

# posがリストの範囲内なら、posの位置にある要素を返す。
# 範囲外の場合 None を返す。
def get_value_by_lists(values_list, pos):
    height, width = len(values_list), len(values_list[0])
    if 0 <= pos[1] < height and 0 <= pos[0] < width:
        return values_list[pos[1]][pos[0]]
    else:
        return None

# 上下左右いずれかに黒があるか を真偽値として返す。
def is_black_in_four_dir(cells_list, pos):
    for x_adjust, y_adjust in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if get_value_by_lists(cells_list, (pos[0] + x_adjust, pos[1] + y_adjust)) == "#":
            return True
    return False

h, w = map(lambda x: int(x), input().split(" "))
cells_list = [input() for _ in range(h)]

for y, cells in enumerate(cells_list):
    for x, cell in enumerate(cells):
        if cell == "#" and not (is_black_in_four_dir(cells_list, (x, y))):
            print("No")
            sys.exit()
print("Yes")