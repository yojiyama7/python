t = int(input())
s = [input() for _ in range(t)]

for s_i in s:
	count = 0
	j = 0
	while j < len(s_i)-5+1:
		if not (s_i[j:j+5] in ["tokyo", "kyoto"]):
			j += 1
			continue
		count += 1
		j += 5
	print(count)

################################

# t = int(input())
# s = [input() for _ in range(t)]

# for s_i in s:
# 	count = 0
# 	j = 0

# 	while j < len(s_i)-5+1:
# 		if s_i[j:j+5] in ["tokyo", "kyoto"]:
# 			count += 1	
# 			j += 5
# 			continue
# 		j += 1

# 	print(count)

################################

# import re

# t = int(input())
# s = [input() for _ in range(t)]

# for s_i in s:
# 	print(len(re.findall("(tokyo|kyoto)", s_i)))