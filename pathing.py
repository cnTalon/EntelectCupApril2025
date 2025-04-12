import math
from typing import Tuple

# distance formula for path calculation
def distance (p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def paths(zoo):
    paths = []
    fed = set()

    # sort by diet
    for diet in ['c', 'o', 'h']:
        enclosures = [enc for enc in zoo.enclosures if enc[4] == diet and (enc[0], enc[1], enc[2]) not in fed]
        enclosures.sort(key = lambda e: (-e[3], distance(zoo.depot[:2], e[:2])))

        if not enclosures:
            continue

        nearestSource = min((fs for fs in zoo.storages if fs[3] == diet), key=lambda fs: distance(zoo.depot[:2], fs[:2]))

        for enc in enclosures:
            paths.append([zoo.depot[:2], nearestSource[:2], enc[:2], zoo.depot[:2]])
            fed.add((enc[0], enc[1], enc[2]))   # adds to list of fed spots

    # sorts by priority, then distance if priority is the same
    #for enc in sorted(zoo.enclosures, key = lambda e: (-e[3], distance(zoo.depot[:2], e[:2]))):
    #    if (enc[0], enc[1], enc[2]) in fed:     # checks if enclosure is fed
    #        continue

    #    diet = enc[4]   #gets diet and checks for nearest food source
    #    nearestSource = min((fs for fs in zoo.storages if fs[3] == diet), key=lambda fs: distance(zoo.depot[:2], fs[:2]))

    # adds path to list [depot, food source, enclosure, depot]
    #paths.append([zoo.depot[:2], nearestSource[:2], enc[:2], zoo.depot[:2]])

    #fed.add((enc[0], enc[1], enc[2]))   # adds to list of fed spots

    return paths