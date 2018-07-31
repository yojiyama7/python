n = int(input())
r = sorted([int(input()) for i in range(n)], reverse=True)

red_radius = r[::2]
whilte_radius = r[1::2]+[0]
square_area = sum([r**2 - w**2 for r, w in zip(red_radius, whilte_radius)])

print(square_area * 3.14159)