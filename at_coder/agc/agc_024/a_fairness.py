# 数学とかで証明できそうだが
# 現時点では何やってるかわからん
A, B, _, K = map(int, input().split(" "))

print((A-B)*(-1)**(K%2))