import re

with open("input.txt", "r") as file:
	l1 = []
	l2 = {}
	for line in file:
		x = re.findall("\d+", line)
		l1.append(int(x[0]))
		l2[int(x[1])] = l2[int(x[1])] + 1 if l2.get(int(x[1])) else 1
	print(sum(l * l2[l] if l2.get(l) else 0 for l in l1))