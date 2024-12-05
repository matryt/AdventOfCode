from typing import Dict
from common import read_file

data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

INPUT_FILE = r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\4\input.txt"

def does_a_letter_corresponds(tuple1, tuple2):
    return tuple1[1] == tuple2[1]

def find_any_matching(diag1, otherDiags):
    for diag2 in otherDiags:
        if does_a_letter_corresponds(diag1.coordList, diag2.coordList):
            return diag2
    return None

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Diag:
    def __init__(self, coordList):
        self.coordList = coordList

def is_distance_valid(coord1, coord2) -> bool:
    if abs(coord1.x - coord2.x) <= 1 and abs(coord1.y - coord2.y) <= 1:
        return True
    return False

def parse_lists(data):
    return [line for line in data.split('\n') if line]

def find_all_letters(inputData):
    d: Dict[str, list[Coord]] = {"X": [], "M": [], "S": [], "A": []}
    for y, line in enumerate(parse_lists(inputData)):
        for x, letter in enumerate(line):
            d[letter].append(Coord(x, y))
    return d

def line(x_coord, m_coord, a_coord, s_coord):
    if x_coord.y == m_coord.y == a_coord.y == s_coord.y:
        if x_coord.x + 1 == m_coord.x and m_coord.x + 1 == a_coord.x and a_coord.x + 1 == s_coord.x:
            return True
        if s_coord.x + 1 == a_coord.x and a_coord.x + 1 == m_coord.x and m_coord.x + 1 == x_coord.x:
            return True
    return False

def column(x_coord, m_coord, a_coord, s_coord):
    if x_coord.x == m_coord.x == a_coord.x == s_coord.x:
        if x_coord.y + 1 == m_coord.y and m_coord.y + 1 == a_coord.y and a_coord.y + 1 == s_coord.y:
            return True
        if s_coord.y + 1 == a_coord.y and a_coord.y + 1 == m_coord.y and m_coord.y + 1 == x_coord.y:
            return True
    return False

def diagonal(x_coord, m_coord, a_coord, s_coord):
    """Vérifie les quatre sens de la diagonale"""

    if x_coord.x + 1 == m_coord.x and m_coord.x + 1 == a_coord.x and a_coord.x + 1 == s_coord.x:
        if x_coord.y + 1 == m_coord.y and m_coord.y + 1 == a_coord.y and a_coord.y + 1 == s_coord.y or x_coord.y - 1 == m_coord.y and m_coord.y - 1 == a_coord.y and a_coord.y - 1 == s_coord.y:
            return True

    if s_coord.x + 1 == a_coord.x and a_coord.x + 1 == m_coord.x and m_coord.x + 1 == x_coord.x:
        if s_coord.y + 1 == a_coord.y and a_coord.y + 1 == m_coord.y and m_coord.y + 1 == x_coord.y or s_coord.y - 1 == a_coord.y and a_coord.y - 1 == m_coord.y and m_coord.y - 1 == x_coord.y:
            return True
    return False

def possible_part1(x_coord, m_coord, a_coord, s_coord):
    if line(x_coord, m_coord, a_coord, s_coord):
        return True
    if column(x_coord, m_coord, a_coord, s_coord):
        return True
    if diagonal(x_coord, m_coord, a_coord, s_coord):
        return True
    return False


def calculate_word_part1(d):
    counter = 0
    for x_coord in d["X"]:
        for m_coord in d["M"]:
            if not is_distance_valid(x_coord, m_coord):
                continue
            for a_coord in d["A"]:
                if not is_distance_valid(m_coord, a_coord):
                    continue
                for s_coord in d["S"]:
                    if is_distance_valid(a_coord, s_coord) and possible_part1(x_coord, m_coord, a_coord, s_coord):
                        counter += 1
    return counter

def mas_pattern(m_coord, a_coord, s_coord):
    # Renvoie le type de diagonale
    if m_coord.x == a_coord.x + 1 and a_coord.x == s_coord.x + 1:
        if m_coord.y == a_coord.y + 1 and a_coord.y == s_coord.y + 1:
            return True
        if m_coord.y == a_coord.y - 1 and a_coord.y == s_coord.y - 1:
            return True
    if m_coord.x == a_coord.x - 1 and a_coord.x == s_coord.x - 1:
        if m_coord.y == a_coord.y + 1 and a_coord.y == s_coord.y + 1:
            return True
        if m_coord.y == a_coord.y - 1 and a_coord.y == s_coord.y - 1:
            return True
    return False

def calculate_xmas_count(d):
    diags = []
    for m_coord in d["M"]:
        for a_coord in d["A"]:
            if is_distance_valid(m_coord, a_coord):
                for s_coord in d["S"]:
                    if is_distance_valid(a_coord, s_coord):
                        diagType = mas_pattern(m_coord, a_coord, s_coord)
                        if diagType:
                            diags.append(Diag([m_coord, a_coord, s_coord]))
    return find_number_matching(diags)

def find_number_matching(diagList):
    counter = 0
    for i in range(len(diagList)):
        diag = diagList[i]
        otherDiags = diagList[i+1:]
        if find_any_matching(diag, otherDiags):
            counter += 1
    return counter

def main(step, dataType):
    if dataType == "example":
        d = find_all_letters(data)
    else:
        d = find_all_letters(read_file(INPUT_FILE))
    if step == 1:
        print(calculate_word_part1(d))
    else:
        print(calculate_xmas_count(d))

main(2, "data")