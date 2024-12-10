from itertools import combinations
from typing import List, Dict, Tuple

from common import Solution, ProblemType

example = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

class Antenna:
	def __init__(self, x, y, symbol):
		self.x = x
		self.y = y
		self.symbol = symbol

	def find_antinodes_positions(self, other, WIDTH, HEIGHT):
		l = set()
		delta_x = self.x - other.x
		delta_y = self.y - other.y
		for p in (-1, 1):
			first = (self.x + p * delta_x, self.y + p * delta_y)
			second = (other.x + p * delta_x, other.y + p*delta_y)
			if validate_coords(first, WIDTH, HEIGHT):
				l.add(first)
			if validate_coords(second, WIDTH, HEIGHT):
				l.add(second)
		return list(l - {(self.x, self.y), (other.x, other.y)})

	def __repr__(self):
		return f"{self.x, self.y}"

def parse_data(data):
	antennas = {}
	WIDTH = len(data.split('\n')[2])
	HEIGHT = len(data.split('\n'))
	y = 0
	for line in data.split('\n'):
		if line:
			for x, char in enumerate(line):
				if char.isalnum():
					ant = Antenna(x, y, char)
					if antennas.get(char):
						antennas[char].append(ant)
					else:
						antennas[char] = [ant]
			y += 1
	for key in antennas:
		print(f"{key} : {antennas[key]}")
	return antennas, WIDTH, HEIGHT

def validate_coords(coords: Tuple[int, int], WIDTH: int, HEIGHT: int):
	x, y = coords
	return 0 <= x < WIDTH and 0 <= y < HEIGHT

def find_antinodes(antennas: Dict[str, List[Antenna]], WIDTH, HEIGHT):
	all_antinodes = set()
	for key, values in antennas.items():
		for this, other in combinations(values, 2):
			antinodes = this.find_antinodes_positions(other, WIDTH, HEIGHT)
			for a in antinodes:
				if a not in all_antinodes:
					all_antinodes.add(tuple(map(int, a)))
	return all_antinodes


class Day8(Solution):
	def __init__(self):
		super().__init__(example, r'C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\8\input.txt')

	def solve_part1(self, data: str):
		dt, width, height = parse_data(data)
		return len(find_antinodes(dt, width, height))


Day8().run_solution(1, ProblemType.REAL_DATA)