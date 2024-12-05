from enum import Enum


def read_file(path):
    try:
        with open(path) as f:
            return "\n".join(f.readlines())
    except FileNotFoundError:
        print(f"Error: The file at {path} does not exist.")
        return ""
    except Exception as e:
        print(f"Error reading the file: {e}")
        return ""


class ProblemType(Enum):
    EXAMPLE = 1
    REAL_DATA = 2


class Solution:
    def __init__(self, example_data, real_input_file):
        self.EXAMPLE_DATA = example_data
        self.INPUT_FILE = real_input_file

    def get_data(self, data_type: ProblemType):
        if data_type == ProblemType.EXAMPLE:
            return self.EXAMPLE_DATA
        if data_type == ProblemType.REAL_DATA:
            return read_file(self.INPUT_FILE)
        raise ValueError("Invalid data type provided")

    def run_solution(self, step, data_type: ProblemType):
        data = self.get_data(data_type)
        if step == 1:
            print(self.solve_part1(data))
        elif step == 2:
            print(self.solve_part2(data))
        else:
            print("Invalid step provided")

    def solve_part1(self, data):
        raise NotImplementedError("Part 1 solution is not implemented yet.")

    def solve_part2(self, data):
        raise NotImplementedError("Part 2 solution is not implemented yet.")
