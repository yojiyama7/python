s_abc = [input() for c in "abc"]

player = 0
while len(s_abc[player]) != 0:
	next_player = "abc".find(s_abc[player][0])
	s_abc[player] = s_abc[player][1:]
	player = next_player
print("ABC"[player])