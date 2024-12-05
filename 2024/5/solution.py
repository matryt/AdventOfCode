from common import Solution, ProblemType

example = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''

def put_into(d, key, value):
	if d.get(key):
		d[key].append(value)
	else:
		d[key] = [value]

def parse_data(data):
	reqs = {}
	first, second = data.split('\n\n\n')
	for reqLine in first.split('\n'):
		if not reqLine:
			continue
		n1, n2 = reqLine.split('|')
		put_into(reqs,int(n1),int(n2))
	return reqs, [[int(n) for n in line.split(',')] for line in second.split('\n') if line]

def verify_line(line, d):
	for i in range(len(line) - 1):
		first = line[i]
		second = line[i + 1]
		if d.get(second) and first in d[second]:
			return False
	return True

def verify_or_modify_line(line, d):
	i = 0
	while i < len(line) - 1:
		first = line[i]
		second = line[i + 1]
		if d.get(second) and first in d[second]:
			line[i], line[i + 1] = line[i + 1], line[i]  # Échange les deux
			i = max(i - 1, 0)  # Reviens d'une position pour revérifier
		else:
			i += 1  # Continue seulement si aucun échange
	return line

def find_list_middle(l):
	return l[len(l) // 2]

def verify_all(dic, lines):
	counter_sum = 0
	for line in lines:
		if verify_line(line, dic):
			counter_sum += find_list_middle(line)
	return counter_sum

def modify_all(dic, lines):
	counter_sum = 0
	i = 0
	while i < len(lines):
		if not verify_line(lines[i], dic):
			lines[i] = verify_or_modify_line(lines[i], dic)
			counter_sum += find_list_middle(lines[i])
		i += 1
	return counter_sum

class Day5(Solution):
	def __init__(self):
		super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\5\input.txt")

	def solve_part1(self, data):
		dico, solvingData = parse_data(data)
		return verify_all(dico, solvingData)

	def solve_part2(self, data):
		dico, solvingData = parse_data(data)
		return modify_all(dico, solvingData)

d = Day5()
d.run_solution(2, ProblemType.REAL_DATA)