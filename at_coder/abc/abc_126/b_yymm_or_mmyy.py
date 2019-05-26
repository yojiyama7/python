S = input()

a, b = S[:2], S[2:]

a_can_month = (1 <= int(a) <= 12)
b_can_month = (1 <= int(b) <= 12)

print([["NA", "YYMM"], ["MMYY", "AMBIGUOUS"]][a_can_month][b_can_month])