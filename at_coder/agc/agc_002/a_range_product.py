A, B = map(int, input().split(" "))

if A <= 0 <= B:
    print("Zero")
elif B < 0 and (B-A+1)%2==1:
    print("Negative")
else: 
    print("Positive")

################################

# A, B = map(int, input().split(" "))

# if A <= 0 <= B:
#     print("Zero")
# elif 0 < A: 
#     print("Positive")
# else:
#     num = B-A+1
#     if num%2==0:
#         print("Positive")
#     else:
#         print("Negative")