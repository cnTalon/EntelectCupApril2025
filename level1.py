with open("1.txt", "r") as file:
    size = file.readline().strip()
    depot = file.readline().strip()
    capacity = file.readline().strip()
    storages = file.readline().strip()
    enclosures = file.readline().strip()
    deadzones = file.readline().strip()