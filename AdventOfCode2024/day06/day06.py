import sys

class Guard:
	def __init__(self, i, j, vi, vj):
		self.i = i
		self.j = j
		self.vi = vi
		self.vj = vj

def print_grid(grid):
	print("-"*len(grid))
	print()
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print(grid[i][j], end='')
		print()	
	print()
	print("-"*len(grid))

def rotate(guard):
	temp = guard.vi
	guard.vi = guard.vj
	guard.vj = -temp

def in_bounds(i, j, grid):
	return i >= 0 and i < len(grid) and j >= 0 and j < len(grid)

def move(grid, guard):
	count = 0
	while in_bounds(guard.i + guard.vi, guard.j + guard.vj, grid) and \
	grid[guard.i + guard.vi][guard.j + guard.vj] != '#':
		if grid[guard.i][guard.j] != 'X':
			count += 1
			grid[guard.i][guard.j] = 'X'
		guard.i = guard.i + guard.vi
		guard.j = guard.j + guard.vj
		if not in_bounds(guard.i, guard.j, grid):
			return 
	if not in_bounds(guard.i + guard.vi, guard.j + guard.vj, grid):
		return 
	rotate(guard)	
	return 

def simulate(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == '^':
				guard = Guard(i, j, -1, 0)
				grid[i][j] = 'X'
	while in_bounds(guard.i, guard.j, grid):
		move(grid, guard)
		if not in_bounds(guard.i + guard.vi, guard.j + guard.vj, grid):			
			grid[guard.i][guard.j] = 'X'
			count = 0
			for i in range(len(grid)):
				for j in range(len(grid)):
					if grid[i][j] == 'X':
						count += 1
			print(count)
			return

with open(sys.argv[1], "r") as file:
	grid = []
	for line in file:
		grid.append([v for v in line.strip()])
	simulate(grid)