with open("1.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
    storages = []
    enclosures = []
    deadzones = []

    # Parse dimensions
    size = lines[0].strip()[1:-1].split(",")

    # Parse drone depot
    depot = lines[1].strip()[1:-1].split(",")

    # Parse battery capacity
    capacity = int(lines[2].strip()[1:-1])

    # Parse food storages
    storage = lines[3].strip()[1:-1]
    if storage:
        for fs in storage.split('),'):
            clean = fs.strip()[1:].replace(')', '')
            if clean:
                fs = clean.split(',')
                storages.append(fs)

    # Parse enclosures
    enclosure = lines[4].strip()[1:-1]
    if enclosure:
        for enc in enclosure.split('),'):
            clean = enc.strip()[1:].replace(')', '')
            if clean:
                enc = clean.split(',')
                enclosures.append(enc)

    # Parse deadzones
    deadzone = lines[5].strip()[1:-1]
    if deadzone:
        for dz in deadzone.split('),'):
            clean = dz.strip()[1:].replace(')', '')
            if clean:
                dz = clean.split(',')
                deadzones.append(dz)