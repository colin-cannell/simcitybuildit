import numpy as np
import random
import pygame as pg


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
size = 50
required = [city_storage, city_hall, clock_tower, town_hall, mayors_mansion]
stores = [building_supplies, hardware_store, farmers_market, furniture_store, gardening_supplies, donut_shop, fashion_store, fast_food, home_appliances, sports_shop, toy_shop, restoration_bureau, country_store, desert_shop]

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

def visualize_grid(grid, size):
    cell_size = 10

    pg.init()
    screen = pg.display.set_mode((size * cell_size, size * cell_size))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        screen.fill((255, 255, 255))  # Clear screen before drawing

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell is None:
                    color = (255, 255, 255)  # White for empty spaces
                elif isinstance(cell, Residential):
                    color = (100, 100, 100)  # Gray for Residential
                elif isinstance(cell, Road) or cell == "0":
                    color = (0, 0, 0)  # Black for Road
                elif isinstance(cell, Fire):
                    color = (255, 0, 0)  # Red for Fire Station
                elif isinstance(cell, Police):
                    color = (0, 0, 255)  # Blue for Police Station
                elif isinstance(cell, Health):
                    color = (0, 255, 0)  # Green for Health
                else:
                    color = (200, 200, 200)  # Default color for other buildings
                
                # Draw the cell
                pg.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

        # Draw grid lines
        for x in range(0, size * cell_size, cell_size):
            pg.draw.line(screen, (0, 0, 0), (x, 0), (x, size * cell_size))  # Vertical lines
        for y in range(0, size * cell_size, cell_size):
            pg.draw.line(screen, (0, 0, 0), (0, y), (size * cell_size, y))  # Horizontal lines

        pg.display.flip()



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
    total_residential_zones = 0
    for row in grid:
        for cell in row:
            # Check if the cell is an instance of Residential or if it equals '1'
            if isinstance(cell, Residential) or (isinstance(cell, str) and cell == '1'):
                total_residential_zones += 1
    
    # Each Residential building has a population of 1836
    total_residential = total_residential_zones * 1836
    return total_residential

def generate_population(size, population_size=10):
    return [create_random_layout(buildings, size) for _ in range(population_size)]

def select_best(population, num_best):
    return sorted(population, key=population_score, reverse=True)[:num_best]

# instead of cutting them in half and combining them 
# instead overlay them and find commonalities
def crossover(parent1, parent2):
    # Ensure both parents have the same grid size
    rows, cols = len(parent1), len(parent1[0])

    # Create an empty child grid
    child = [[None for _ in range(cols)] for _ in range(rows)]

    # Overlay the two parents and keep only matching buildings
    for i in range(rows):
        for j in range(cols):
            if parent1[i][j] == parent2[i][j]:  # Keep only if identical
                child[i][j] = parent1[i][j]

    return child


def mutate(layout):
    i, j = random.randint(0, len(layout) - 2), random.randint(0, len(layout[0]) - 2)  # Stay within 2x2 bounds

    #TODO: add more buildings to this
    # new_building = Residential("Residential Zone", 2, 2)
    new_building = random.choice([Residential("Residential Zone", 2, 2), Fire("Fire Station", 4, 2, (24, 24)), Police("Police Station", 4, 2, 0), Health("Health", 4, 2, (24, 24))])
    # Ensure the full 2x2 space is empty
    if all(layout[x][y] is None for x in range(i, i + 2) for y in range(j, j + 2)):
        for x in range(i, i + 2):
            for y in range(j, j + 2):
                layout[x][y] = new_building

    return layout


# Main genetic algorithm
def genetic_algorithm(generations=200, population_size=10, grid_size=50, mutation_rate=0.8):
    population = generate_population(grid_size, population_size)
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

# write a function to check if child is valid
# all buuldings are connected to road
# each police, fire, health must be in its 4, 2 block

# create a visualozation function for it

# Run the algorithm
if __name__ == "__main__":
    best_layout = genetic_algorithm()

    # Print the best layout
    for row in best_layout[0]:
        for cell in row:
            if cell is None:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print()  # Newline after each row

    # Calculate and print the population score
    max_population = population_score(best_layout[0])
    print("Max Population:", max_population)

    # Visualize the best layout
    visualize_grid(best_layout[0], 50)

# add functionality to add all the buildings to the grid
# all polution checking
# add chekcing if the building is connected to road
# add optimtimize roads
# add checking if building is in an area covered by police health and fire

# find best layout loop
# find best layout near mountains
# find best layout near beach

# combine beach and mountain layouts with the layout looop

# roads should be one width and be all inter connected



