import re
import sys

with open(sys.argv[1], "r") as file:
	total = 0
	state = True
	for line in file:
		matches = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", line)
		for a, b, t1, t2 in matches:
			if t1 == 'do()':
				state = True
			if t2 == 'don\'t()':
				state = False
			if len(a) > 0 and len(b) > 0 and state:
				total += int(a) * int(b)
	print(total)