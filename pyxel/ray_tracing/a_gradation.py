from pyxel import *

W, H = 240, 135
X, Y = 0, 0

init(W, H,
	palette=[
		16*i + (16*i<<8) + (16*i<<16) for i in range(16)
	]
)

def update():
	pass

def draw():
	cls(15)
	for y in range(H):
		for x in range(W):
			pset(x, y, x*16//W)

run(update, draw)
