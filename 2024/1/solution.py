## ---------------------------------²
## Common
import timeit

from common import read_file

data = """
14739   72645
58352   89405
"""

INPUT_FILE = r"C:\Users\mathi\OneDrive\Documents\code\python\AdventOfCode\2024\1\input.txt"

def parse_lists(data : str):
    l1 = []
    l2 = []
    for line in data.split('\n'):
        if len(line) < 1: continue
        n1, n2 = line.split('   ')
        l1.append(int(n1))
        l2.append(int(n2))
    return l1, l2

## ---------------------------------
## Step 1

def find_max_index(l):
    return l.index(max(l))

def one_step(l1, l2):
    n1 = l1.pop(find_max_index(l1))
    n2 = l2.pop(find_max_index(l2))
    return abs(n1-n2)

def process_lists(l1,l2):
    return sum(one_step(l1,l2) for _ in range(len(l1)))

def main_step1():
    file_data = read_file(INPUT_FILE)
    l1, l2 = parse_lists(file_data)
    process_lists(l1,l2)
    
## ---------------------------------
## Step 2
    
def create_dic_occurrences(l):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    return d

def process_similarities(l1, dic):

    total = 0
    for i in l1:
        if dic.get(i):
            total += dic.get(i) * i
    return total

def main_step2():
    file_data = read_file(INPUT_FILE)
    l1, l2 = parse_lists(file_data)
    d = create_dic_occurrences(l2)
    total = process_similarities(l1, d)
    #print(total)

exec_time = timeit.timeit(main_step2, number=3000)
print(f"Execution time: {exec_time}")