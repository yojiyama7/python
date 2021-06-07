from pyxel import *

W, H = 240, 135
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_W = 16
PLAYER_H = 16
PLAYER_VY = 0
JUMP_REMAIN = 1
GRAVITY = 0.2
def constrain(a, x, b):
	return min(max(a, x), b)

init(W, H, fps=60)

rects = []

def update():
	global PLAYER_X
	global PLAYER_Y
	global PLAYER_VY
	global JUMP_REMAIN
	global rects
	rects_next = []
	for i, (x, y, w, h, col) in enumerate(rects):
		if w >= PLAYER_W+4 or h >= PLAYER_H+4:
			continue
		else:
			rects_next.append([x-1, y-1, w+2, h+2, col])
	rects = rects_next
	if btn(KEY_A):
		PLAYER_X -= 2
	if btn(KEY_D):
		PLAYER_X += 2
	if btnp(KEY_SPACE) and JUMP_REMAIN:
		PLAYER_VY = -4.8
		rects.append([
			PLAYER_X+PLAYER_H//4,
			PLAYER_Y+PLAYER_H//4,
			PLAYER_W-PLAYER_W//4*2,
			PLAYER_H-PLAYER_H//4*2,
			9
		])
		JUMP_REMAIN -= 1
	if PLAYER_Y >= H-1-PLAYER_H:
		JUMP_REMAIN = 1
	PLAYER_VY = min(PLAYER_VY + GRAVITY, 8)
	PLAYER_Y += PLAYER_VY
	# if btn(KEY_DOWN):
	# 	PLAYER_Y += 1
	PLAYER_X = constrain(0, PLAYER_X, W-1-PLAYER_W)
	PLAYER_Y = constrain(0, PLAYER_Y, H-1-PLAYER_H)

	# NEW
	# for obj in objs:
	# 	obj.update()

def draw():
	cls(0)
	rect(int(PLAYER_X), int(PLAYER_Y), PLAYER_W, PLAYER_H, 7)
	for status in rects:
		rectb(*status)

	# NEW
	# cls(0)
	# for obj in objs:
	# 	obj.draw()

run(update, draw)