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
size = 24
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

    placed_residential = True  # Start by assuming we can place residential buildings
    while placed_residential:
        placed_residential = False  # Reset flag
        residential_building = Residential(name="Residential Zone", width=2, height=2)  # Create a new residential building (e.g., 2x2 size)
        attempts = 0

        while attempts < 100:  # Avoid infinite loops
            x, y = random.randint(0, size - residential_building.width), random.randint(0, size - residential_building.height)

            # Check if space is empty for the entire building footprint
            if all(grid[x + i][y + j] is None for i in range(residential_building.width) for j in range(residential_building.height)):
                # Place residential building
                for i in range(residential_building.width):
                    for j in range(residential_building.height):
                        grid[x + i][y + j] = residential_building
                # Connect the residential building to roads
                grid = connect_to_roads(grid, x, y, residential_building.width, residential_building.height, size)
                placed_residential = True  # Successfully placed a residential building
                break  # Exit while loop and try to place another residential building
            attempts += 1

    # Add roads to connect all buildings (make sure everything is connected to roads)
    grid = add_roads(grid, size)

    return grid

def add_roads(grid, size):
    """Simple road placement logic."""
    for i in range(size):
        for j in range(size):
            if grid[i][j] is not None:
                # Check if adjacent space is empty to add a road
                if i > 0 and grid[i-1][j] is None:  # If space above is empty
                    grid[i-1][j] = "0"
                if j > 0 and grid[i][j-1] is None:  # If space to the left is empty
                    grid[i][j-1] = "0"
    return grid

def connect_to_roads(grid, x, y, width, height, size):
    """Connect the given building to roads."""
    # Look for any empty spaces around the building and place roads there
    for i in range(x, x + width):
        for j in range(y, y + height):
            # If the building cell is placed, try to add roads to adjacent cells
            if grid[i][j] is not None:
                # Check all four sides for empty space
                if i > 0 and grid[i - 1][j] is None:  # Space above
                    grid[i - 1][j] = "0"
                if i < size - 1 and grid[i + 1][j] is None:  # Space below
                    grid[i + 1][j] = "0"
                if j > 0 and grid[i][j - 1] is None:  # Space left
                    grid[i][j - 1] = "0"
                if j < size - 1 and grid[i][j + 1] is None:  # Space right
                    grid[i][j + 1] = "0"
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

layout = create_random_layout(buildings, size)

print_grid(layout)


# step 2 sort population of layouts by fitness score
def population_score(grid):
    """Calculates the total population of the city based on residential buildings."""
    total_residential_zones = 0
    for row in grid:
        for cell in row:
            if isinstance(cell, Residential):
                total_residential_zones += 1
    
    total_residential = (total_residential_zones//4) * 1836
    return total_residential

print(population_score(layout))

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

# pj
# jeff
# colin
# logan 
# karan
# joe

