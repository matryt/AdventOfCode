## Unfinished

testData = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

galaxies = []

class Galaxy:
    count = 0

    def __init__(self, i, j):
        self.id = Galaxy.count
        Galaxy.count += 1
        self.visited = []
        self.i = i
        self.j = j
    
    def add_visited(self, id):
        self.visited.append(id)
    
    def is_visited(self, id):
        return id in self.visited
    
    def __repr__(self):
        return f"Galaxy {str(self.id)}"

def get_input(test = False):
    if test:
        return testData.split("\n")
    with open("data11.txt") as file:
        data = file.readlines()
    return data

def process_input(data):
    processedData = []
    for i, line in enumerate(data):
        processedLine = []
        for index, char in enumerate(line):
            if char == "#":
                processedLine.append(Galaxy(i, index))
            else:
                processedLine.append("")
        processedData.append(processedLine)
    return processedData

def euclidian_distance(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

def get_shortest_distance(data, galaxy1, galaxy2):
    i1 = galaxy1.i
    j1 = galaxy1.j
    i2 = galaxy2.i
    j2 = galaxy2.j
    point = data[i1][j1]

    while point != galaxy2:
        pass