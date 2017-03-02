#will control the the falling Brick (= moving it down one by one)

def fall(ymin, xmin, currbrickstate):
#arguments: 
#	ymin, xmin: the coordinates of the upper corner of the Brickfield.
#	curbrickstate: the rotation state of the brick that is used right now.

	for y in range(1, 5):
		for x in range(1, 5):
    			world2[ymin + y][xmin + x] = currbrickstate[y][x]
#	replaces the current brickfield with the brickfield given with curbrickstate first horizontally, then vertically
	for number in range(0, 4):
		world2[ymin][xmin + number] = 0
	
	ymin += 1
