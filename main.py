import numpy as np
import random

class Road:
  def __init__(self):
     pass

class Building:
    def __init__(self, name, id, width, height):
        self.name = name
        self.id = id
        self.width = width
        self.height = height
        self.connected_to_road = False

class Residential(Building):
    def __init__(self, name, id, width, height, population):
        super().__init__(name, id, width, height)
        self.population = population
        self.fire = False
        self.police = False
        self.health = False
        self.pollution = False

class Store(Building):
    def __init__(self, name, id, width, height):
        super().__init__(name, id, width, height)

class Factory(Building):
   def __init__(self, name, id, width, height, pollution):
        super().__init__(name, id, width, height)
        self.pollution = pollution

class Power(Building):
   def __init__(self, name, id, width, height, power, pollution):
        super().__init__(name, id, width, height)
        self.power = power
        self.pollution = pollution

class Water(Building):
    def __init__(self, name, id, width, height, water):
        super().__init__(name, id, width, height)
        self.water = water

class Sewage(Building):
    def __init__(self, name, id, width, height, sewage, pollution):
        super().__init__(name, id, width, height)
        self.sewage = sewage
        self.pollution = pollution

class Waste(Building):
   def __init__(self, name, id, width, height, waste, pollution):
      super().__init__(name, id, width, height)
      self.waste = waste
      self.pollution = pollution

class Fire(Building):
   def __init__(self, name, id, width, height, area):
      super().__init__(name, id, width, height)
      self.area = area

class Police(Building):
   def __init__(self, name, id, width, height, area):
      super().__init__(name, id, width, height)
      self.area = area

class Health(Building):
   def __init__(self, name, id, width, height, area):
      super().__init__(name, id, width, height)
      self.area = area

class Specialization(Building):
    def __init__(self, name, id, width, height, boost, area):
        super().__init__(name, id, width, height)
        self.boost = boost
        self.area = area

class Grid:
    def __init__(self, length=50, width=68):
        self.length = length
        self.width = width
        self.grid = [[None for _ in range(width)] for _ in range(length)]

    def can_place_building(self, building, x, y):
        if x + building.width > self.width or y + building.height > self.length:
            return False
        
        for i in range(x, x + building.width):
            for j in range(y, y + building.height):
                if i < 0 or i >= self.length or j < 0 or j >= self.width:
                    return False
                if self.grid[i][j] is not None:
                    return False
        
        if isinstance(building, Residential):
            if not self.is_within_service_radius(x, y, building.width, building.height):
                return False
            if self.is_in_pollution_area(x, y, building.width, building.height):
                return False
            if not self.is_connected_to_road(x, y, building.width, building.height):
                return False
        
        return True

    def is_within_service_radius(self, x, y, width, height):
        service_radius = 5 
        for i in range(self.length):
            for j in range(self.width):
                if isinstance(self.grid[i][j], (Fire, Police, Health)):
                    if (x < i + service_radius and x + width > i - service_radius and
                        y < j + service_radius and y + height > j - service_radius):
                        return True
        return False
    
    def place_building(self, building, x, y):
        if self.can_place_building(building, x, y):
            for i in range(x, x + building.width):
                for j in range(y, y + building.height):
                    self.grid[i][j] = building
            return True
        else:
            return False
        
    def is_in_pollution_area(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                if isinstance(self.grid[i][j], (Factory, Power, Sewage, Waste)):
                    return True
        return False

    def is_connected_to_road(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                if (i > 0 and isinstance(self.grid[i - 1][j], Road)) or \
                   (i < self.length - 1 and isinstance(self.grid[i + 1][j], Road)) or \
                   (j > 0 and isinstance(self.grid[i][j - 1], Road)) or \
                   (j < self.width - 1 and isinstance(self.grid[i][j + 1], Road)):
                    return True
        return False
    
residential = Residential("Residential Zone", 1, 2, 2, 1836)

building_supplies = Store("Building Supplies", 2, 2, 2)
hardware_store = Store("Hardware Store", 3, 2, 2)
farmers_market = Store("Farmers Market", 4, 2, 2)
furniture_store = Store("Furniture Store", 5, 2, 2)
gardening_supplies = Store("Gardening Supplies", 6, 2, 2)
donut_shop = Store("Donut Shop", 7, 2, 2)
fashion_store = Store("Fashion Store", 8, 2, 2)
fast_food = Store("Fast Food Restaurant", 9, 2, 2)
home_appliances = Store("Home Appliances", 10, 2, 2)
sports_shop = Store("Sports Shop", 11, 2, 2)
toy_shop = Store("Toy Shop", 12, 2, 2)
restoration_bureau = Store("Bureau of Restoration", 13, 2, 2)
country_store = Store("Country Store", 14, 2, 2)
desert_shop = Store("Desert Shop", 15, 2, 2)


high_tech_factory = Factory("High Tech Factory", 16, 2, 2, (6, 6))

nuclear_plant = Power("Nuclear Power Plant", 17, 4, 3, 60, (12, 12))
water_station = Water("Water Pumping Station", 18, 2, 2, 55)
sewage_plant = Sewage("Deluxe Sewage Plant", 19, 3, 2, 55, (0, 0))
recycling_center = Waste("Recycling Center", 20, 3, 2, 50, (0, 0))

fire_station = Fire("Deluxe Fire Station", 21, 4, 2, (22, 22))
police_station = Police("Police Precinct", 22, 4, 2, (22, 22))
hospital = Health("Hospital", 23, 4, 2, (24, 24))

city_storage = Building("City Storage", 24, 3, 2)
city_hall = Building("City Hall", 25, 3, 2)
clock_tower = Building("Clock Tower", 26, 2, 2)
town_hall = Building("Town Hall", 27, 3, 2)
mayors_mansion = Building("Mayor's Mansion", 28, 3, 3)

# Parks
jogging_path = Specialization("Jogging Path", 29, 2, 2, 30, 8)
university_cafe = Specialization("University Park Cafeteria", 30, 2, 2, 25, 10)
reflection_pool = Specialization("Reflection Pool Park", 31, 2, 1, 20, 8)
peaceful_park = Specialization("Peaceful Park", 32, 2, 1, 25, 10)
urban_plaza = Specialization("Urban Plaza", 33, 2, 1, 20, 8)
sculpture_garden = Specialization("Sculpture Garden", 34, 2, 1, 30, 8)
tree_row = Specialization("Row of Trees", 35, 2, 1, 30, 12)
casino_park = Specialization("Casino City Park", 36, 2, 2, 15, 10)
soccer_field = Specialization("Soccer Field", 37, 2, 2, 25, 8)
baseball_field = Specialization("Baseball Field", 38, 2, 2, 25, 8)
swimming_pool = Specialization("Swimming Pool", 39, 4, 2, 15, 14)
golf_course = Specialization("Golf Course", 40, 4, 6, 15, 16)

# specialization
surfer_beach = Specialization("Surfer Beach", 42, 2, 1, 10, 12)
cozy_cottages = Specialization("Cozy Cottages", 44, 2, 1, 20, 12)

# entertainment
entertainment_hq = Specialization("Entertainment HQ", 43, 2, 2, 20, 8)

# Gambling
gambling_hq = Specialization("Gambling HQ", 45, 2, 2, 20, 8)


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


layout = create_random_layout(buildings, grid)

for i in range(grid):
    for j in range(grid):
       print(layout[i][j], end=" ")
    print()


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