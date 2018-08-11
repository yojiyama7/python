def hangman(word):
	word = list(word)
	board = ["_"]*len(word)
	wrong = 0
	picture = [
		"-------     ",
		"|     |     ",
		"|     o     ",
		"|    /|\    ",
		"|     |     ",
		"|    / \    ",
		"|           "
	]
	while any([char != "$" for char in word]):
		print("\n現在の状態: " + "".join(board))

		char = ""
		while char == "":
			char = input("文字を入力してください\n(2文字目以降は無視されます)")
		char = char[0]
		
		if char in word:
			find_index = word.index(char)
			board[find_index] = char
			word[find_index] = "$"
		else:
			wrong += 1
		
		print("\n".join(picture[:wrong]))
		if wrong >= 7:
			print("lose ...")
			return None
			 
	print("complate!")

if __name__ == "__main__":
	hangman("cat")