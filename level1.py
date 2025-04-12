from zoo import Zoo
from pathing import *
with open("1.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
    storages = []
    enclosures = []
    deadzones = []

    # Parse dimensions
    size = list(map(int, lines[0].strip()[1:-1].split(",")))

    # Parse drone depot
    depot = list(map(int,lines[1].strip()[1:-1].split(",")))

    # Parse battery capacity
    capacity = int(lines[2].strip())

    # Parse food storages
    storage = lines[3].strip()[1:-1]
    if storage:
        for fs in storage.split('),'):
            clean = fs.strip()[1:].replace(')', '')
            if clean:
                fs = clean.split(',')
                storages.append([int(fs[0]), int(fs[1]), int(fs[2]), fs[3]])

    # Parse enclosures
    enclosure = lines[4].strip()[1:-1]
    if enclosure:
        for enc in enclosure.split('),'):
            clean = enc.strip()[1:].replace(')', '')
            if clean:
                enc = clean.split(',')
                enclosures.append([int(enc[0]), int(enc[1]), int(enc[2]), float(enc[3]), enc[4]])

    # Parse deadzones
    deadzone = lines[5].strip()[1:-1]
    if deadzone:
        for dz in deadzone.split('),'):
            clean = dz.strip()[1:].replace(')', '')
            if clean:
                dz = clean.split(',')
                deadzones.append([int(dz[0]), int(dz[1]), int(dz[2])])
                
zoo = Zoo(size, depot, storages, enclosures, deadzones)
path = paths(zoo)
with open('submission.txt','w') as f:
    f.write(path.__str__()[1:-1])