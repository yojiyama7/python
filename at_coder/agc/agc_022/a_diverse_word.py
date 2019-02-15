S = input()

chars = "abcdefghijklmnopqrstuvwxyz"
char_set = set(chars)

if len(S) == 26:
    for i in range(len(S)-1, -1, -1):
        x = chars.index(S[i])
        y = sorted(set(chars[x+1:])-set(S[:i]))
        # print(i, y)
        if len(y):
            print(S[:i]+y[0])
            exit()
else:
    t = sorted(set(chars)-set(S))[0]
    print(S+t)
    exit()
print(-1)

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