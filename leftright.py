#leftright.py
#Functions to move the Brick (or rather its field) left and right.

def left(ymin, xmin, currbrickstate):
	for y in range(0, 4):
		for x in range(0, 4):
			world2[ymin + y][xmin + (x - 1)] = currbrickstate[y][x]
		
def right(ymin, xmin, currbrickstate):
	for y in range(0, 4):
		for x in range(0, 4):
			world2[ymin + y][xmin + (x + 1)] = currbrickstate[y][x]
