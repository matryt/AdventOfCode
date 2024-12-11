import time
from common import Solution, ProblemType

example = "125 17"

def parse_data(data):
    return [int(x) for x in data.split()]

def blink(l):
    result = []
    for num in l:
        if num == 0:
            result.append(1)
        else:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                half = len(str_num) // 2
                first_half = int(str_num[:half])
                second_half = int(str_num[half:])
                result.extend([first_half, second_half])
            else:
                result.append(num * 2024)
    return result

def blink_many_times(l, times):
    for i in range(times):
        l = blink(l)
        print(i+1)
    return l

class Day11(Solution):
    def __init__(self):
        super().__init__(example, r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\11\input.txt")

    def solve_part1(self, data):
        chainedList = parse_data(data)
        return len(blink_many_times(chainedList, 75))

Day11().run_solution(1, ProblemType.REAL_DATA)