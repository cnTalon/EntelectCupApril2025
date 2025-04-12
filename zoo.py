class Zoo:
    def __init__(self,size,depot,storages,enclosures,deadzones):
        self.size = size
        self.depot = depot
        self.storages = storages
        self.enclosures = enclosures
        self.deadzones = deadzones
        
        # Initialize the grid with zeros
        self.grid = [[[0 for _ in range(size[2])]
                      for _ in range(size[1])]
                     for _ in range(size[0])]
        
        # plot coordinates
        self.grid[depot[0]][depot[1]][depot[2]] = 1
        
        for storage in storages:
            self.grid[storage[0]][storage[1]][storage[2]] = storage[3] + 'S'
            
        for enclosure in enclosures:
            self.grid[enclosure[0]][enclosure[1]][enclosure[2]] = enclosure[4]
            
        # deadzones