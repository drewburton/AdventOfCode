import sys

word = "XMAS"

def search(grid, i, j, vector, matchdex):
	if i >= len(grid) or i < 0 or j >= len(grid) or j < 0:
		return 0
	if grid[i][j] == word[matchdex]:
		matchdex += 1
		if matchdex == len(word):
			return 1
		matches = 0
		if vector:
			i2, j2 = vector
			matches += search(grid, i + i2, j + j2, vector, matchdex)
		else:
			for i2 in range(i - 1, i + 2):
				for j2 in range(j - 1, j + 2):
					if i2 == i and j2 == j:
						continue
					matches += search(grid, i2, j2, (i2-i,j2-j), matchdex)
		return matches
	return 0

with open(sys.argv[1], "r") as file:
	grid = []
	for line in file:
		grid.append([])
		for char in line.strip():
			grid[len(grid) - 1].append(char)

	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == word[0]:
				count += search(grid, i, j, None, 0)
	print(count)