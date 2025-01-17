import sys

def build_order(raw_order):
	map = {}
	orderings = raw_order.split("\n")
	for ordering in orderings:
		first, second = ordering.split("|")
		first = int(first)
		second = int(second)
		if not map.get(first):
			map[first] = set()
		map[first].add(second)
	return map

def is_correct(update, order):
	for i in range(len(update)):
		for j in range(i-1, -1, -1):
			if not update[i] in order:
				continue
			if update[j] in order[update[i]]:
				return False
	return True

def fix_order(update, order):
	for i in range(len(update)):
		for j in range(i-1, -1, -1):
			if not update[i] in order:
				continue
			if update[j] in order[update[i]]:
				#print(update[j], order[update[i]])
				#print("before:", update)
				temp = update[j]
				update[j] = update[i]
				update[i] = temp
				#print("after:", update)
				update = fix_order(update, order)
				return update
	return update

with open(sys.argv[1], "r") as file:
	raw_order = ""
	updates = ""
	reading_order = True
	for line in file:
		if line == "\n":
			reading_order = False
		elif reading_order:
			raw_order += line
		else:
			updates += line
	order = build_order(raw_order.strip())
	sum = 0
	for raw_update in updates.split("\n"):
		update = [int(value) for value in raw_update.split(",")]
		if not is_correct(update, order):
			new_update = fix_order(update, order)
			#print(new_update)
			sum += new_update[int(len(new_update) / 2)]
	print(sum)