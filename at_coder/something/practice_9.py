# 正規表現短い速い最強

import sys

def text_match_word(text, words):
    for word in words:
        if word == text[:len(word)]:
            return word

words_next = (("dream", "er"), ("erase", "r"))
words_next_dict = dict(words_next)

s = input()

before_match_word = ""
while "" != s:
    search_words = list(words_next_dict.keys())
    if before_match_word in words_next_dict:
        search_words.append(words_next_dict[before_match_word])
    match_word = text_match_word(s, search_words)
    if match_word != None:
        s = s[len(match_word):]
    else:
        print("NO")
        sys.exit()
    before_match_word = match_word

print("YES")
    

# import sys
# # import re

# # if re.match("(dream|dreamer|erase|eraser)*$", input()):
# #     print("YES")
# # else:
# #     print("NO")

# sys.setrecursionlimit(10000)

# def text_match_words(text, words):
#     match_words = []
#     for word in words:
#         if word == text[:len(word)]:
#             match_words.append(word)
#     return match_words

# def is_match_for(text, words):
#     if "" == text: 
#         return True
#     else:
#         match_words = text_match_words(text, words)
#         if [] == match_words:
#             return False
#         else:
#             return any([is_match_for(text[len(match_word):], words) for match_word in match_words])

# words = ("dream", "dreamer", "erase", "eraser")

# s = input()

# if is_match_for(s, words):
#     print("YES")
# else:
#     print("NO")