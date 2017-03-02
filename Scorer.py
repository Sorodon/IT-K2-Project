def scorer(world):
	for row in world:
		counter = 0
		for element in row:
			counter = counter + element
#			check every row if full
		if counter == 10:
			score += 1
			for x in range(0, row):
				world[row - x] == world[row - x - 1]
# 				drop every row above by one
				world[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#				add new clean line
