import sys

def parse_to_list(row):
	return list(map(int, row.strip().split(' ')))

def safe(data, removed = False):
	direction = 0
	for i in range(1, len(data)):
		mag = data[i] - data[i-1]
		if mag > 0 and direction < 0 or \
			mag < 0 and direction > 0 or \
			abs(mag) > 3 or \
			mag == 0:
				if removed:
					return 0
				else:
					result = 0
					for s in range(0, len(data)):
						result = result or safe(data[:s] + data[s+1:], True)
					return result
		direction = mag 
	return 1

with open(sys.argv[1], "r") as file:
	print(sum(safe(parse_to_list(line)) for line in file))