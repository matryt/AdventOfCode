formatted_data = []

def process_data(data):
    for line in data:
        formatted_data.append(line.split(" "))
    for line in formatted_data:
        for number in line:
            line[line.index(number)] = int(number)

def verify_line(line):
    return all((line[i] == 0 for i in range(len(line))))

def step(line):
    if verify_line(line):
        return False
    processedLine = []
    for i in range(len(line) - 1):
        processedLine.append(line[i+1]-line[i])
    return processedLine

def get_data():
    with open("data9.txt") as file:
        data = file.readlines()
    return data

def process_line(line):
    appendElement = -1 if LEVEL == 1 else 0
    sign = 1 if LEVEL == 1 else -1
    processedLine = [line]
    i = 0
    while not verify_line(processedLine[i]):
        stepLine = step(processedLine[i])
        processedLine.append(stepLine)
        i+=1
    processedLine[-1] = [0] + processedLine[-1]
    for i in range(len(processedLine)-2, -1, -1):
        processedLine[i] = insertElement(processedLine[i], sign * processedLine[i+1][appendElement] + processedLine[i][appendElement])
    return processedLine

def insertElement(line: list, element):
    position = -1 if LEVEL == 1 else 0
    line.insert(position, element)
    return line

def process_all(data):
    result = []
    for i in range(len(data)):
        result.append(process_line(data[i]))
    return result

def finalResult(data):
    appendElement = -1 if LEVEL == 1 else 0
    result = 0
    for set in data:
        result += set[0][appendElement]
    return result


testData = [[10, 13, 16, 21, 30, 45]]

LEVEL = input("Level : ")
process_data(get_data())
finalData = process_all(formatted_data)
print(finalResult(finalData))