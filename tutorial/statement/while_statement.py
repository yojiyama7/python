char_list = ["a", "b", "", "d", "", "", "g"]

while "" in char_list:
	char_list.remove("")

print(char_list) # >>> ['a', 'b', 'd', 'g']