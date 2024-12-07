import timeit

from common import Solution, ProblemType

example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

OPERATORS = {
	1: "+*",
	2: "|+*"
}

def make_operation(n1,n2,op):
	match op:
			case '+':
				return n1+n2
			case '*':
				return n1*n2
			case '|':
				return int(str(n1)+str(n2))

def find_possibilities(target, numbers, operations, step=1):
	possible = False
	operators = OPERATORS[step]
	if len(numbers) == 1:
		return numbers[0] == target
	for op in operations:
		result = make_operation(numbers[0],numbers[1],op)
		if result <= target:
					possible = possible or find_possibilities(target, [result]+numbers[2:],operators)
	return possible
					
		

def process_data(data :str, step=1):
	operators = OPERATORS[step]
	result = 0
	for line in data.split('\n'):
		if not line:
			continue
		target, numbers = line.split(':')
		target = int(target)
		numbers = numbers.strip()
		if find_possibilities(target, list(map(int, numbers.split(' '))), operators, step):
			result += target
	return result

class Day7(Solution):
	def __init__(self):
		super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\7\input.txt")

	def solve_part1(self, data):
		return process_data(data, 1)

	def solve_part2(self, data):
		return process_data(data, 2)

start_time = timeit.default_timer()
Day7().run_solution(2, ProblemType.REAL_DATA)
print(timeit.default_timer() - start_time)
