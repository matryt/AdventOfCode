# I haven't finisged this one yet, I currently search all the paths and not only the loop ones

pipes = []


class Pipe:
    def __init__(self, name, i, j):
        self.name = name
        self.i = i
        self.j = j
        self.neighbours = []
        self.neighboursPositions = []
        self.processNeighbourPositions()

    def add_neighbour(self, neighbour) -> None:
        self.neighbours.append(neighbour)

    def explore_neighbours(self) -> None:
        for neighbour in self.neighbours:
            neighbour.explore_neighbours()
            print(f"Exploring node of position ({neighbour.i}, {neighbour.j})")

    def processNeighbourPositions(self):
        match self.name:
            case ".":
                pass
            case "|":
                self.neighboursPositions = [(self.i-1, self.j), (self.i+1, self.j)]
            case "-":
                self.neighboursPositions = [(self.i, self.j-1), (self.i, self.j+1)]
            case "L":
                self.neighboursPositions = [(self.i-1, self.j), (self.i, self.j+1)]
            case "J":
                self.neighboursPositions = [(self.i-1, self.j), (self.i, self.j-1)]
            case "7":
                self.neighboursPositions = [(self.i+1, self.j), (self.i, self.j - 1)]

    def __repr__(self):
        return f"Pipe {self.name} at position ({self.i}, {self.j})"

def is_valid_position(i, j, maxI, maxJ):
    return 0 <= i < maxI and 0 <= j < maxJ


def process_data():
    with open("data10.txt") as file:
        data = file.readlines()
    for line in data:
        processedLine = []
        for i in range(len(line)):
            char = line[i]
            processedLine.append(Pipe(char, len(pipes), i))
        pipes.append(processedLine)
    for j in range(len(pipes)):
        for i in range(len(pipes[j])):
            for position in pipes[j][i].neighboursPositions:
                if is_valid_position(position[0], position[1], len(pipes), len(pipes[j])):
                    pipes[j][i].add_neighbour(pipes[position[0]][position[1]])

def get_start():
    for line in pipes:
        for pipe in line:
            if pipe.name == "S":
                return pipe

def add_start_neighbours(startPipe):
    for line in pipes:
        for pipe in line:
            if (startPipe.i, startPipe.j) in pipe.neighboursPositions:
                startPipe.add_neighbour(pipe)
    return startPipe
    position = "("
    while position != "q":
        position = input("Position : ")
        if position == "q":
            break
        position = tuple(map(int, position.split(",")))
        startPipe.add_neighbour(pipes[position[0]][position[1]])

def explore(pipe: Pipe, start: tuple, number: int, previous: Pipe = None):
    if len(pipe.neighboursPositions) == 0:
        return number
    if pipe.neighboursPositions == [start] and number != 0:
        return number
    for neighbour in pipe.neighbours:
        if neighbour != previous and neighbour != start:
            number = max(number, explore(neighbour, start, number+1, pipe))
    return number

def find_max(start: Pipe):
    return max(
        explore(neighbour, (start.i, start.j), 0)
        for neighbour in start.neighbours
    )

process_data()
start = get_start()
start = add_start_neighbours(start)
print(find_max(start))