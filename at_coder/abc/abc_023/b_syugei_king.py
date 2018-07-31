n = int(input())
s = input()

acce = "b"
page = 0
while len(acce) < len(s):
    add_char = "acbcab"[page%3::3]
    acce = add_char[0] + acce + add_char[1]
    page += 1
print(page if acce == s else -1)