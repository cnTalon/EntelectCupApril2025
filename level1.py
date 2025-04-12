from zoo import Zoo
from drone import Drone
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
                
zoo = Zoo(size, depot, storages, enclosures, deadzones)
drone = Drone(depot, capacity)
def find_closest_storage(storages, depot, food_type):
    """
    Finds the closest storage of a specified food type to the depot, ignoring height (z-coordinate).

    :param storages: List of storages, where each storage is [x, y, z, food_type].
    :param depot: List representing the depot coordinates [x, y, z].
    :param food_type: The food type to search for (e.g., 'h', 'c', 'o').
    :return: The closest storage as a list [x, y, z, food_type], or None if no storage matches the food type.
    """
    closest_storage = None
    min_distance = float('inf')

    for storage in storages:
        if storage[3] == food_type:  # Check if the food type matches
            # Calculate 2D Euclidean distance (ignoring height)
            distance = ((int(storage[0]) - int(depot[0])) ** 2 + (int(storage[1]) - int(depot[1])) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_storage = storage

    return closest_storage
# carnivores first
_ = find_closest_storage(storages, depot, "c")
drone.location = f"({_[0]},{_[1]})"
drone_run = [f"({depot[0]},{depot[1]}),{drone.location}"]


# omnivores second
_ = find_closest_storage(storages, depot,"o")

