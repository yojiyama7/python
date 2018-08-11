import random

class Card:
	marks = ["spades", "hearts", "diamonds", "clubs"]
	nums = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

	def __init__(self, mark, num):
		self.mark = mark
		self.num = num
	
	def __repr__(self):
		return "{} of {}".format(self.nums[self.num], self.marks[self.mark])

	def __lt__(self, other):
		if self.num < other.num:
			return True
		elif self.num == other.num and self.mark < other.mark:
			return True
		return False
	def __gt__(self, other):
		if self.num > other.num:
			return True
		elif self.num == other.num and self.mark > other.mark:
			return True
		return False

class Deck:
	def __init__(self):
		self.cards = []
		for mark_i in range(0, 4):
			for num_i in range(2, 15):
				self.cards.append(Card(mark_i, num_i))
		random.shuffle(self.cards)

	def pick_card(self):
		return self.cards.pop()

class Player:
	def __init__(self, name):
		self.name = name
		self.card = None
		self.win_count = 0
	def set_card(self, card):
		self.card = card
	def win(self):
		self.win_count += 1

	def __str__(self):
		return "{}: {}".format(self.name, self.card)
	def __repr__(self):
		return "{}: {}".format(self.name, self.card)

class WarGame:
	def __init__(self, player_names):
		self.players = [Player(name) for name in player_names]
		self.deck = Deck()

	def game(self):
		while len(self.deck.cards) >= len(self.players):
			response = input("qで強制終了、それ以外で実行: ")
			if response == "q":
				return "中断"
			for player in self.players:
				player.set_card(self.deck.pick_card())
			print(", ".join(map(str, self.players)))
			max_player = max(self.players, key=lambda x:x.card)
			max_player.win()
		print("勝者: {}".format(self.winner().name))

	def winner(self):
		return max(self.players, key=lambda x:x.win_count)

if __name__ == "__main__":
	war = WarGame(["yayo", "kidai"])
	war.game()