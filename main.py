import numpy as np
import random

class Road:
  def __init__(self):
     pass
  
  def __str__(self):
      return "0"

class Building:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.connected_to_road = False

class Residential(Building):
    def __init__(self, name, width, height, population=1836):
        super().__init__(name, width, height)
        self.population = population
        self.fire = False
        self.police = False
        self.health = False
        self.pollution = False

    def __str__(self):
        return "1"

class Store(Building):
    def __init__(self, name, width, height):
        super().__init__(name, width, height)
    def __str__(self):
        return "S"

class Factory(Building):
    def __init__(self, name, width, height, pollution):
        super().__init__(name, width, height)
        self.pollution = pollution

    def __str__(self):
        return "f"

class Power(Building):
    def __init__(self, name, width, height, power, pollution):
        super().__init__(name, width, height)
        self.power = power
        self.pollution = pollution

    def __str__(self):
        return "P"

class Water(Building):
    def __init__(self, name, width, height, water):
        super().__init__(name, width, height)
        self.water = water
    
    def __str__(self):
        return "W"

class Sewage(Building):
    def __init__(self, name, width, height, sewage, pollution):
        super().__init__(name, width, height)
        self.sewage = sewage
        self.pollution = pollution

    def __str__(self):
        return "s"

class Waste(Building):
    def __init__(self, name, width, height, waste, pollution):
      super().__init__(name, width, height)
      self.waste = waste
      self.pollution = pollution
    
    def __str__(self):
        return "w"

class Fire(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "F"

class Police(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "P"

class Health(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "H"

class Specialization(Building):
    def __init__(self, name, width, height, boost, area):
        super().__init__(name, width, height)
        self.boost = boost
        self.area = area

residential = Residential("Residential Zone", 2, 2, 1836)

building_supplies = Store("Building Supplies", 2, 2)
hardware_store = Store("Hardware Store", 2, 2)
farmers_market = Store("Farmers Market", 2, 2)
furniture_store = Store("Furniture Store", 2, 2)
gardening_supplies = Store("Gardening Supplies", 2, 2)
donut_shop = Store("Donut Shop", 2, 2)
fashion_store = Store("Fashion Store", 2, 2)
fast_food = Store("Fast Food Restaurant", 2, 2)
home_appliances = Store("Home Appliances", 2, 2)
sports_shop = Store("Sports Shop", 2, 2)
toy_shop = Store("Toy Shop", 2, 2)
restoration_bureau = Store("Bureau of Restoration", 2, 2)
country_store = Store("Country Store", 2, 2)
desert_shop = Store("Desert Shop", 2, 2)


high_tech_factory = Factory("High Tech Factory", 2, 2, (6, 6))

nuclear_plant = Power("Nuclear Power Plant", 4, 3, 60, (12, 12))
water_station = Water("Water Pumping Station", 2, 2, 55)
sewage_plant = Sewage("Deluxe Sewage Plant", 3, 2, 55, (0, 0))
recycling_center = Waste("Recycling Center", 3, 2, 50, (0, 0))

fire_station = Fire("Deluxe Fire Station", 4, 2, (22, 22))
police_station = Police("Police Precinct", 4, 2, (22, 22))
hospital = Health("Hospital", 4, 2, (24, 24))

city_storage = Building("City Storage", 3, 2)
city_hall = Building("City Hall", 3, 2)
clock_tower = Building("Clock Tower", 2, 2)
town_hall = Building("Town Hall", 3, 2)
mayors_mansion = Building("Mayor's Mansion", 3, 3)

# Parks
jogging_path = Specialization("Jogging Path", 2, 2, 30, 8)
university_cafe = Specialization("University Park Cafeteria", 2, 2, 25, 10)
reflection_pool = Specialization("Reflection Pool Park", 2, 1, 20, 8)
peaceful_park = Specialization("Peaceful Park", 2, 1, 25, 10)
urban_plaza = Specialization("Urban Plaza", 2, 1, 20, 8)
sculpture_garden = Specialization("Sculpture Garden", 2, 1, 30, 8)
tree_row = Specialization("Row of Trees", 2, 1, 30, 12)
casino_park = Specialization("Casino City Park", 2, 2, 15, 10)
soccer_field = Specialization("Soccer Field", 2, 2, 25, 8)
baseball_field = Specialization("Baseball Field", 2, 2, 25, 8)
swimming_pool = Specialization("Swimming Pool", 4, 2, 15, 14)
golf_course = Specialization("Golf Course", 4, 6, 15, 16)

# specialization
surfer_beach = Specialization("Surfer Beach", 2, 1, 10, 12)
cozy_cottages = Specialization("Cozy Cottages", 2, 1, 20, 12)

# entertainment
entertainment_hq = Specialization("Entertainment HQ", 2, 2, 20, 8)

# Gambling
gambling_hq = Specialization("Gambling HQ", 2, 2, 20, 8)


# step 1 create a population of random city layout
grid = 24
buildings = [fire_station, police_station, hospital]

def create_random_layout(buildings, size):
    """Generates a city layout with buildings first, then adds roads to connect them."""

    # Initialize empty grid
    grid = [[None for _ in range(size)] for _ in range(size)]

    # Place buildings randomly, ensuring no overlap
    for building in buildings:
        placed = False
        attempts = 0
        while not placed and attempts < 100:  # Avoid infinite loops
            x, y = random.randint(0, size - building.width), random.randint(0, size - building.height)

            # Check if space is empty for the entire building footprint
            if all(grid[x + i][y + j] is None for i in range(building.width) for j in range(building.height)):
                # Place building
                for i in range(building.width):
                    for j in range(building.height):
                        grid[x + i][y + j] = building
                placed = True
            attempts += 1

    # Add roads to connect buildings
    grid = add_roads(grid, size)

    # Now place residential buildings one by one and connect them to roads
    residential_count = 0  # Track the number of residential buildings placed
    while residential_count < 10:  # You can change this number based on your desired number of residential buildings
        residential_building = Residential(name="Residential Zone", width=2, height=2)  # Create a new residential building (e.g., 2x2 size)
        placed = False
        attempts = 0
        while not placed and attempts < 100:  # Avoid infinite loops
            x, y = random.randint(0, size - residential_building.width), random.randint(0, size - residential_building.height)

            # Check if space is empty for the entire building footprint
            if all(grid[x + i][y + j] is None for i in range(residential_building.width) for j in range(residential_building.height)):
                # Place residential building
                for i in range(residential_building.width):
                    for j in range(residential_building.height):
                        grid[x + i][y + j] = residential_building
                # Connect the residential building to roads
                grid = add_roads(grid, size)
                residential_count += 1
                placed = True
            attempts += 1

    # Add roads to connect all buildings (make sure everything is connected to roads)
    grid = add_roads(grid, size)

    return grid

def add_roads(grid, size):
    """Adds roads by ensuring each building is connected to the road network."""
    road_positions = set()

    def find_nearest_road(x, y):
        """Finds the nearest road and returns its coordinates."""
        queue = [(x, y)]
        visited = set()
        while queue:
            cx, cy = queue.pop(0)
            if (cx, cy) in road_positions:
                return cx, cy
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        return None  # Shouldn't happen

    # Start with an initial road in the center
    center_x, center_y = size // 2, size // 2
    grid[center_x][center_y] = Road()
    road_positions.add((center_x, center_y))

    # Connect each building to the nearest road
    for x in range(size):
        for y in range(size):
            if isinstance(grid[x][y], Building):
                nearest_road = find_nearest_road(x, y)
                if nearest_road:
                    road_x, road_y = nearest_road
                    # Create a path from (x, y) to (road_x, road_y)
                    cx, cy = x, y
                    while (cx, cy) != (road_x, road_y):
                        if cx < road_x:
                            cx += 1
                        elif cx > road_x:
                            cx -= 1
                        elif cy < road_y:
                            cy += 1
                        elif cy > road_y:
                            cy -= 1
                        if grid[cx][cy] is None:
                            grid[cx][cy] = Road()
                            road_positions.add((cx, cy))

    return grid

def print_grid(grid):
    """Prints the grid with proper character representations."""
    for row in grid:
        for cell in row:
            if cell is None:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print()  # Newline after each row

layout = create_random_layout(buildings, grid)

print_grid(layout)

# step 2 sort population of layouts by fitness score
def population_score(layout):
    total_residential = 0
    for i in range(layout.length):
        for j in range(layout.width):
            if layout[i][j] == 1:
                total_residential += 1
    population = (total_residential // 4) * 1836
    return population

def sort_layouts(layouts):
    return sorted(layouts)

# apply a cross over function
def crossover():
    pass

# apply a mutuation function
def mutation():
    pass

# create a main genetic algorithm 
def genetic_algorithm():
    pass