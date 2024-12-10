from typing import List

from common import Solution, ProblemType

example = '2333133121414131402'


class Block:
	def __init__(self, id_block):
		self.id = id_block

	def __repr__(self):
		return f'[id={self.id}]'


def parse_data(data):
	blocks = []
	counter = 0
	for i in range(0, len(data), 2):
		try:
			blocks.extend([Block(counter)] * int(data[i]))
			counter += 1
			blocks.extend([None] * int(data[i + 1]))
		except:
			pass
	return blocks


def find_first_none(blocks_list):
	try:
		return blocks_list.index(None)
	except ValueError:
		return -1

def find_group_indexes(blocks_list: List[Block|None], id_group):
	return [i for i, val in enumerate(blocks_list) if val and val.id == id_group]


def find_none_blocks(blocks_list, size) -> int:
	counter = 0
	for i, val in enumerate(blocks_list):
		if val is None:
			counter += 1
			if counter == size:
				return i - size + 1
		else:
			counter = 0
	return -1


def shift_blocks_by_group(blocks_list: List[Block | None]):
	i = len(blocks_list) - 1
	while i >= 0:
		if blocks_list[i]:
			group_indexes = find_group_indexes(blocks_list, blocks_list[i].id)
			none_indexes = find_none_blocks(blocks_list, len(group_indexes))
			if none_indexes > group_indexes[-1]:
				i -= 1
				continue
			if none_indexes != -1:
				for j in range(len(group_indexes)):
					blocks_list[none_indexes + j] = blocks_list[group_indexes[j]]
					blocks_list[group_indexes[j]] = None
		i -= 1
	return blocks_list


def shift_blocks(blocks_list):
	i = len(blocks_list) - 1
	while i >= 0:
		if blocks_list[i]:
			none_index = find_first_none(blocks_list)
			if none_index >= i:
				break
			blocks_list[none_index] = blocks_list[i]
			blocks_list[i] = None
		i -= 1
	return blocks_list


def count_values(blocks_list, exitWhenNone=True):
	counter = 0
	for i, val in enumerate(blocks_list):
		if val is None:
			if exitWhenNone:
				return counter
			else:
				continue
		counter += i * val.id
	return counter


class Day9(Solution):
	def __init__(self):
		super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\9\input.txt")

	def solve_part1(self, data):
		blocks = parse_data(data)
		blocks = shift_blocks(blocks)
		return count_values(blocks)

	def solve_part2(self, data):
		blocks = parse_data(data)
		blocks = shift_blocks_by_group(blocks)
		return count_values(blocks, False)


Day9().run_solution(2, ProblemType.REAL_DATA)
