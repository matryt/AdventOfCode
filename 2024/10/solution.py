from typing import List, Tuple

from common import Solution, ProblemType

example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def parse_data(data):
	zeroes = []
	maphills = []
	for y, line in enumerate(data.split('\n')):
		if line:
			numbers=[]
			for x, number in enumerate(map(int, line)):
				if number == 0:
					zeroes.append((y, x))
				numbers.append(number)
			maphills.append(numbers)
	return zeroes, maphills

def find_around_coords(x: int, y: int, width: int, height: int):
	coords = []
	if x > 0:
		coords.append((x-1, y))
	if x < width - 1:
		coords.append((x+1, y))
	if y > 0:
		coords.append((x, y-1))
	if y < height - 1:
		coords.append((x, y+1))
	return coords

def find_size(maphills: List[List[int]]):
	return len(maphills), len(maphills[0])

def explore_map(maphills: List[List[int]], zeroes, width, height):
	counter = 0
	for coord in zeroes:
		y, x = coord
		number = find_next_value(maphills, x, y, width, height, 1)
		counter += number
	return counter


def find_next_value(maphills: List[List[int]], x: int, y: int, width: int, height: int, val_to_search: int = 1) -> int:
	if val_to_search == 10:
		return 1
	directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # droite, bas, haut, gauche
	counter = 0
	for dx, dy in directions:
		nx, ny = x + dx, y + dy

		if (0 <= nx < width) and (0 <= ny < height):
			if maphills[ny][nx] == val_to_search:
				counter += find_next_value(maphills, nx, ny, width, height, val_to_search + 1)

	return counter

class Day10(Solution):
	def __init__(self):
		super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\10\input.txt")

	def solve_part1(self, data):
		zeroes, maps = parse_data(data)
		width, height = find_size(maps)
		return explore_map(maps, zeroes, width, height)

Day10().run_solution(1, ProblemType.EXAMPLE)