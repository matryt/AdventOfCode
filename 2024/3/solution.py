from common import read_file

data = """
@~don't()mul(683,461) >,~select()what()};<mul(848,589)!#{$$:,#mul(597,936)]!how();)+mul(944,148)who()mul(84,922)what()(mul(95,23)
"""

INPUT_FILE = r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\3\input.txt"

import re

pattern1 = re.compile(r"mul\(([0-9]{1,3},[0-9]{1,3})\)", re.IGNORECASE)
pattern2 = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)")

def parse_lists(data):
    return [line for line in data.split('\n') if line]

def find_expressions_part1(l, pattern):
    matches = []
    for e in l:
        matches.extend(pattern.findall(e))
    return matches

def find_expressions_part2(l, pattern):
    matches = []
    enabled = True
    for e in l:
        for match in pattern.finditer(e):
            if match.group(1):  # Si on a capturé un groupe (c'est un mul)
                if enabled:
                    a, b = map(int, match.groups())
                    matches.append(a * b)
            elif "do()" in match.group():
                enabled = True
            elif "don't()" in match.group():
                enabled = False
    return matches

def calculate_mul(string) :
    a, b = string.split(',')
    return int(a)*int(b)

def find_total(l):
    return sum(calculate_mul(t) for t in l)

def main_step1():
    file_data = read_file(INPUT_FILE)
    lists = parse_lists(file_data)
    expressions = find_expressions_part1(lists, pattern1)
    print(find_total(expressions))

def main_step2():
    file_data = read_file(INPUT_FILE)
    lists = parse_lists(file_data)
    expressions = find_expressions_part2(lists, pattern2)
    print(sum(expressions))

main_step2()