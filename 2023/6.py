data = """Time:        38947970
Distance:   241154910741091"""


def parse_data(data):
    lines = data.split("\n")
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))
    return times, distances


def mapTimeDistance(times, distances):
    return list(zip(times, distances))



def possibilites(temps, cible):
    return sum(i*(temps-i) > cible for i in range(temps))


def bestOptions(longueur):
    cpt = 1
    mappings = mapTimeDistance(*parse_data(data))
    print(mappings)
    for i in range(longueur):
        cpt *= possibilites(mappings[i][0], mappings[i][1])
    print(cpt)


# bestOptions(4)
print(possibilites(38947970, 241154910741091))