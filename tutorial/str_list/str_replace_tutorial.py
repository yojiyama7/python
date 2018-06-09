str_list = ["apple_pen", "pineapple_pen", "pen_pineapple/apple_pen"]

for i, s in enumerate(str_list):
    str_list[i] = s.replace("_", " ")

print(str_list)
