# 2進数にして、そこから、、、
# 純粋にやればこれでおkだけど　短くできるよなぁ
# まあ愚直な実装がわかりやすくて一番ではあるかも　

N = int(input())

N_len = len(bin(N))
m = 1
i = 0
while m <= N:
    m <<= 1
    if i%2 != N_len%2:
        m += 1
    i+=1
    # print(bin(m))

print(["Takahashi", "Aoki"][i%2])
    

################################
#-------------------------------
################################

# %2==0 -> "1"+"01"*a > N -> Aoki
# else ->  "1"+"10"*a > N -> Takahashi

################################
# 数学杉田玄白

# N = int(input())

# N_len = len(bin(N))-2
# m = 1
# if N_len%2 == 0:
#     for 
#     if int("1" + "01"*(N//2-1) + "0", 2) <= N:
#         print("Takahashi")
#     else:
#         print("Aoki")
# else:
#     if int("1" + "10"*(N//2-1), 2) <= N:
#         print("Aoki")
#     else:
#         print("Takahashi")