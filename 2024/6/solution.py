from enum import Enum
from typing import List, Tuple

from common import Solution, ProblemType

example = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class PositionType(Enum):
    EMPTY = 0
    OBSTACLE = 1
    CURRENT = 2

direction = (0, -1)


class Tile:
    def __init__(self, symbol: str, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = symbol == '^'
        match symbol:
            case '.':
                self.type = PositionType.EMPTY
            case '#':
                self.type = PositionType.OBSTACLE
            case '^':
                self.type = PositionType.CURRENT
            case _:
                raise Exception("Invalid symbol")

    def __repr__(self):
        return f"Tile({self.x},{self.y},{self.type})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def convert_to_tiles(data: str):
    tiles: List[List[Tile]] = []
    y = 0
    for block in data.split('\n\n'):
        block = block.strip()
        if not block:
            continue
        for line in block.split('\n'):
            line = line.strip()
            if not line:
                continue
            inside = []
            for x, symbol in enumerate(line):
                inside.append(Tile(symbol, x, y))
            tiles.append(inside)
            y += 1
    return tiles

def find_current(tiles: List[List[Tile]]):
    for i in tiles:
        for t in i:
            if t.type == PositionType.CURRENT:
                return t
    return None


def find_next_coordinates(tiles: List[List[Tile]], current: Tile, width: int, height: int) -> Tuple[int, int]:
    global direction
    x_final = current.x + direction[0]
    y_final = current.y + direction[1]

    if x_final < 0 or x_final >= width or y_final < 0 or y_final >= height:
        return -1, -1

    tile = tiles[y_final][x_final]

    if tile.type == PositionType.OBSTACLE:
        for _ in range(4):
            direction = get_next_direction(direction)
            x_final = current.x + direction[0]
            y_final = current.y + direction[1]

            if 0 <= x_final < width and 0 <= y_final < height:
                tile = tiles[y_final][x_final]
                if tile.type != PositionType.OBSTACLE:
                    break
        else:
            return -1, -1

    return x_final, y_final


def substitute(tiles: List[List[Tile]], x, y):
    global direction
    direction = (0, -1)

    if tiles[y][x].type in [PositionType.OBSTACLE, PositionType.CURRENT]:
        return False
    original_tile_type = tiles[y][x].type

    tiles[y][x].type = PositionType.OBSTACLE
    result = travel(tiles, 2)

    tiles[y][x].type = original_tile_type
    return result

def all_substitutions(tiles):
    counter = 0
    for y in range(len(tiles)):
        for x in range(len(tiles[0])):
            if substitute(tiles, x, y):
                counter += 1
    return counter


def travel(tiles: List[List[Tile]], step: int = 1):
    current = find_current(tiles)
    if not current:
        raise ValueError("Il n'y a pas de position courante !")

    width = len(tiles[0])
    height = len(tiles)
    step2 = step == 2
    already_visited: set = set()
    while True:
        x, y = find_next_coordinates(tiles, current, width, height)
        if (x, y) == (-1, -1):
            return False if step2 else tiles
        if step2:
            state = (x, y, direction)
            if state in already_visited:
                return True
            already_visited.add(state)
        current = tiles[y][x]
        if not step2:
            current.visited = True


def count_number(tiles: List[List[Tile]]):
    counter = 0
    for l in tiles:
        for t in l:
            if t.visited:
                counter+=1
    return counter

def get_next_direction(dir: Tuple[int, int]):
    match dir:
        case (0, -1):
            return 1, 0
        case (1, 0):
            return 0, 1
        case (0, 1):
            return -1, 0
        case (-1, 0):
            return 0, -1

class Day6(Solution):
    def __init__(self):
        super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\6\input.txt")

    def solve_part1(self, data):
        tiles = convert_to_tiles(data)
        tiles = travel(tiles)
        return count_number(tiles)

    def solve_part2(self, data):
        tiles = convert_to_tiles(data)
        return all_substitutions(tiles)

Day6().run_solution(2, ProblemType.REAL_DATA)