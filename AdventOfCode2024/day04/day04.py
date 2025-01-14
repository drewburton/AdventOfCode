import sys

word = "XMAS"

def search(grid, i, j, vector, matchdex):
	if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(grid) or j + 1 >= len(grid):
		return 0
	if grid[i - 1][j - 1] == 'M' and \
		grid[i + 1][j + 1] == 'S' or \
		grid[i - 1][j - 1] == 'S' and \
		grid[i + 1][j + 1] == 'M':
		if grid[i - 1][j + 1] == 'M' and \
			grid[i + 1][j - 1] == 'S' or \
			grid[i - 1][j + 1] == 'S' and \
			grid[i + 1][j - 1] == 'M':
			return 1
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
			if grid[i][j] == 'A':
				count += search(grid, i, j, None, 0)
	print(count)