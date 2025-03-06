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
    
    def __repr__(self) -> str:
       return "1"

class Store(Building):
    def __init__(self, name, width, height):
        super().__init__(name, width, height)

    def __str__(self):
        return "S"
    
    def __repr__(self) -> str:
       return "S"
    

class Factory(Building):
    def __init__(self, name, width, height, pollution):
        super().__init__(name, width, height)
        self.pollution = pollution

    def __str__(self):
        return "f"
    
    def __repr__(self) -> str:
         return "f"

class Power(Building):
    def __init__(self, name, width, height, power, pollution):
        super().__init__(name, width, height)
        self.power = power
        self.pollution = pollution

    def __str__(self):
        return "P"
    
    def __repr__(self) -> str:
         return "P"

class Water(Building):
    def __init__(self, name, width, height, water):
        super().__init__(name, width, height)
        self.water = water
    
    def __str__(self):
        return "W"
    
    def __repr__(self) -> str:
        return "W"

class Sewage(Building):
    def __init__(self, name, width, height, sewage, pollution):
        super().__init__(name, width, height)
        self.sewage = sewage
        self.pollution = pollution

    def __str__(self):
        return "s"
    
    def __repr__(self) -> str:
        return "s"

class Waste(Building):
    def __init__(self, name, width, height, waste, pollution):
      super().__init__(name, width, height)
      self.waste = waste
      self.pollution = pollution
    
    def __str__(self):
        return "w"
    
    def __repr__(self) -> str:
        return "w"


class Fire(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "F"
    
    def __repr__(self) -> str:
        return "F"

class Police(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "P"
    
    def __repr__(self) -> str:
        return "P"

class Health(Building):
    def __init__(self, name, width, height, area):
      super().__init__(name, width, height)
      self.area = area

    def __str__(self):
        return "H"
    
    def __repr__(self) -> str:
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

def print_grid(grid):
    """Prints the grid with proper character representations."""
    for row in grid:
        for cell in row:
            if cell is None:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print()  # Newline after each row


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

def generate_population(size):
    return [create_random_layout(buildings, size) for _ in range(size)]

def select_best(population, num_best):
    return sorted(population, key=population_score, reverse=True)[:num_best]

def crossover(parent1, parent2):
    # Ensure both parents are of the same grid size
    rows = len(parent1)
    cols = len(parent1[0])

    # Randomly select a crossover point
    crossover_point = random.randint(1, rows - 1)  # Ensures the split doesn't happen at the very start or end
    
    # Initialize the child layout as a copy of parent1
    child = [row[:] for row in parent1]
    
    # Swap part of the grid from parent2
    for i in range(crossover_point, rows):
        child[i] = parent2[i]
    
    # Return the child layout
    return child

def mutate(layout):
    i, j = random.randint(0, len(layout) - 1), random.randint(0, len(layout[0]) - 1)  # Ensure i and j are within bounds
    # Randomly choose a building type to place (ensure that it's valid)
    new_building = random.choice([Residential("Residential Zone", 2, 2)]) 
    layout[i][j] = new_building
    return layout

# Main genetic algorithm
def genetic_algorithm(generations=100, population_size=10, mutation_rate=0.2):
    population = generate_population(population_size)
    for _ in range(generations):
        population = select_best(population, population_size // 2)
        new_population = population[:]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        population = new_population
    return select_best(population, 1)

# Run the algorithm
best_layout = genetic_algorithm()

for row in best_layout[0]:
    for cell in row:
        if cell is None:
            print(".", end=" ")
        else:
            print(cell, end=" ")
    print()  # Newline after each row
    
print("Max Population:", population_score(best_layout))

# write a function to check if child is valid
# all buuldings are connected to road
# police, fire, health must be all in the same block

def is_valid_child(layout):
    pass