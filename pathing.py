import math
from typing import Tuple

# distance formula for path calculation
def distance (p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def paths(zoo, capacity):
    paths = []
    currentPath = []
    remaining = zoo.capacity
    fed = set()

    #start at depot
    depot = zoo.depot[:2]
    takeoffCost = 50 - zoo.depot[2]
    currentPath.append(depot)
    remaining -= takeoffCost

    # sort by diet
    for diet in ['c', 'o', 'h']:
        enclosures = [enc for enc in zoo.enclosures if enc[4] == diet and (enc[0], enc[1], enc[2]) not in fed]
        enclosures.sort(key = lambda e: (-e[3], distance(zoo.depot[:2], e[:2])))

        if not enclosures:
            continue

        nearestSource = min((fs for fs in zoo.storages if fs[3] == diet), key=lambda fs: distance(currentPath[-1], fs[:2]))
        
        fsXY, fsZ = nearestSource[:2], nearestSource[2]

        if currentPath[-1] != fsXY:
            moveCost = (distance(currentPath[-1], fsXY) + (50 - fsZ)) * 2 #ladning + takeoff
            if remaining < moveCost:
                returnDepot = distance(currentPath[-1], depot) + takeoffCost
                currentPath.append(depot)
                paths.append(currentPath)
                currentPath = [depot]
                remaining = capacity - takeoffCost
            currentPath.append(fsXY)
            remaining -= moveCost

        for enc in enclosures:
            encXY, encZ = enc[:2], enc[2]
            moveCost = (distance(currentPath[-1], encXY) + (50 - encZ) *2)

            if remaining < moveCost:
                returnCost = distance(currentPath[-1], depot) + takeoffCost
                currentPath.append(depot)
                paths.append(currentPath)
                currentPath = [depot]
                remaining = capacity - takeoffCost

                fsMoveCost = (distance(depot, fsXY) + (50 - fsZ) * 2)
                currentPath.append(fsXY)
                remaining -= fsMoveCost

            currentPath.append(encXY)
            remaining -= moveCost
            fed.add((enc[0], enc[1], enc[2]))   # adds to list of fed spots
    
    if len(currentPath) > 1 and currentPath[-1] != depot:
        returnCost = distance(currentPath[-1], depot) + takeoffCost
        if remaining >= returnCost:
            currentPath.append(depot)
        else:
            paths.append(currentPath)
            currentPath = [depot, depot]
        paths.append(currentPath)
    
    # sorts by priority, then distance if priority is the same
    #for enc in sorted(zoo.enclosures, key = lambda e: (-e[3], distance(zoo.depot[:2], e[:2]))):
    #    if (enc[0], enc[1], enc[2]) in fed:     # checks if enclosure is fed
    #        continue

    #    diet = enc[4]   #gets diet and checks for nearest food source
    #    nearestSource = min((fs for fs in zoo.storages if fs[3] == diet), key=lambda fs: distance(zoo.depot[:2], fs[:2]))

    # adds path to list [depot, food source, enclosure, depot]
    #paths.append([zoo.depot[:2], nearestSource[:2], enc[:2], zoo.depot[:2]])

    #fed.add((enc[0], enc[1], enc[2]))   # adds to list of fed spots

    return [paths]