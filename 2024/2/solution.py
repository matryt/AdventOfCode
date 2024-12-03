from common import read_file

data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

INPUT_FILE = r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\2\input.txt"

def parse_lists(data : str):
	return [[int(e) for e in s.split(' ')] for s in data.split('\n') if s]

def verify_safe(l):
	sign = 1 if l[1] > l[0] else -1
	for i in range(len(l)-1):
		step = sign * (l[i+1]-l[i])
		if step < 1 or step > 3:
			return False
	return True


def main_step1():
	file_data = read_file(INPUT_FILE)
	lists = parse_lists(file_data)
	print(sum(verify_safe(l) for l in lists))

def slice_list(l, i):
	return l[i:] + l[i+1:]

def main_step2():
	file_data = read_file(INPUT_FILE)
	lists = parse_lists(file_data)
	number = 0
	for i in range(len(lists)):
		for j in range(len(lists[i])):
			if verify_safe(slice_list(lists[i], j)):
				number+=1
				break
	print(number)

main_step1()