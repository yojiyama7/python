chars = "abcdefghijklmnopqrstuvwxyz"

if len(S) == 26:
    
else:
    for c in chars:
        if c not in S:
            t = S + c
            break
    print(t)

################################

# S = input()

# chars = "abcdefghijklmnopqrstuvwxyz"

# if len(S) == 26:
    
#     # if S[0] == "z":
#     #     print(-1)
#     # else:
#     #     for i in range(len(S)):
#     #         m = set(chars[chars.index(S[i]):]) - set(S[:i])
#     #         if len(m):
#     #             S[S.index(chars[i])], S[S.index(chars[i])]
#     #             break
# else:
#     for c in chars:
#         if c not in S:
#             t = S + c
#             break
#     print(t)