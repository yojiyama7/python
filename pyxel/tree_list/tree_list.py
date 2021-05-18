from typing import Iterable
from pyxel import *

INDENT = 16
CHAR_HEIGHT = 5
BETWEEN = 2
CHAR_COLOR = 7

class TreeList:
	def __init__(self, x, y, l):
		self.x = x
		self.y = y
		self.l = l

	def update(self):
		pass

	def draw_inner(self, x, y, l):
		# print(x, y, l)
		for l_i in l:
			if type(l_i) in {list, tuple, set}:
				y = self.draw_inner(x+INDENT, y, l_i)
			else:
				text(x, y, l_i, CHAR_COLOR)
				y += CHAR_HEIGHT
			y += BETWEEN
		return y

	def draw(self):
		self.draw_inner(self.x, self.y, self.l)

tree_list = TreeList(4, 4, [
	"mouse",
	[
		"sensitivity:  [----|-----------]",
		"x-inv:                        []",
		"y-inv:                        []",
	],
	"keyboard",
	[
		"key-bindings",
		[
			"forward:               [ ? ]",
			"backward:              [ ? ]",
			"left:                  [ ? ]",
			"right:                 [ ? ]",
		],
	],
])

init(240, 135, fps=60)
mouse(True)

def update():
	pass

def draw():
	cls(0)
	tree_list.draw()

run(update, draw)
