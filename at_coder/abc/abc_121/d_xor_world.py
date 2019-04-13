A, B = map(int, input().split(" "))
 
print([0, A-1, 1, (A-1)^1][A%4]^[0, B, 1, B^1][(B+1)%4])

################################

# # AC

# A, B = map(int, input().split(" "))

# print(
#     [0,   A  -1,  1, (  A  -1)^1][  A  %4]
#     ^
#     [0, (B+1)-1,  1, ((B+1)-1)^1][(B+1)%4]
# )

################################

# A, B = map(int, input().split(" "))

# print(B-A+1, bin(B-A+1))

# t = ""
# for i in range(40):
#     m = 2**i
#     a, b = A%(m*2), B%(m*2)
#     c = (a//m)*(a%m)
#     d = (b//m)*(b%m+1)
#     print(a, c, b, d)
#     t += str((d-c)%2)

# t = t[::-1]
# print(t)

# print(int(t, 2))