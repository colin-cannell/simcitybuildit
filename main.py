class Road:
    def __init__(self):
        self.width = 1
        self.height = 1
        self.name = "Road"
        self.id = 0


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
        # Check if the building fits within the grid boundaries
        if x + building.width > self.width or y + building.height > self.length:
            return False

        # Check if the space is already occupied
        for i in range(x, x + building.width):
            for j in range(y, y + building.height):
                if i < 0 or i >= self.length or j < 0 or j >= self.width:
                    return False
                if self.grid[i][j] is not None:
                    return False

        # Additional checks only for residential buildings
        if isinstance(building, Residential):
            if not self.is_within_service_radius(x, y, building.width, building.height):
                return False
            if self.is_in_pollution_area(x, y, building.width, building.height):
                return False
            if not self.is_connected_to_road(x, y, building.width, building.height):
                return False

        return True

    def is_within_service_radius(self, x, y, width, height):
        # Check if there are any service buildings in the grid
        has_service_buildings = False
        for i in range(self.length):
            for j in range(self.width):
                if isinstance(self.grid[i][j], (Fire, Police, Health)):
                    has_service_buildings = True
                    break
            if has_service_buildings:
                break

        # If there are no service buildings, allow placement
        if not has_service_buildings:
            return True

        service_radius = 5
        for i in range(self.length):
            for j in range(self.width):
                if isinstance(self.grid[i][j], (Fire, Police, Health)):
                    if (
                        x < i + service_radius
                        and x + width > i - service_radius
                        and y < j + service_radius
                        and y + height > j - service_radius
                    ):
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
        pollution_radius = 3
        for i in range(
            max(0, x - pollution_radius), min(self.length, x + width + pollution_radius)
        ):
            for j in range(
                max(0, y - pollution_radius),
                min(self.width, y + height + pollution_radius),
            ):
                cell = self.grid[i][j]
                if cell is not None and hasattr(cell, "pollution") and cell.pollution:
                    return True
        return False

    def is_connected_to_road(self, x, y, width, height):
        # Check if there are any roads in the grid
        has_roads = False
        for i in range(self.length):
            for j in range(self.width):
                if isinstance(self.grid[i][j], Road):
                    has_roads = True
                    break
            if has_roads:
                break

        # If there are no roads, allow placement
        if not has_roads:
            return True

        # Check if the building is adjacent to a road
        for i in range(max(0, x - 1), min(self.length, x + width + 1)):
            for j in range(max(0, y - 1), min(self.width, y + height + 1)):
                if (
                    i < x or i >= x + width or j < y or j >= y + height
                ):  # Only check adjacent cells
                    if (
                        i < self.length
                        and j < self.width
                        and isinstance(self.grid[i][j], Road)
                    ):
                        return True
        return False


# step 1 create a population of random city layouts
def random_layout():
    pass


# step 2 sort population of layouts by fitness score
def population_score(layout):
    total_residential = 0
    for i in range(layout.length):
        for j in range(layout.width):
            if layout[i][j] == 1:
                total_residential += 1
    population = (total_residential // 4) * 1836
    return population


# apply a cross over function
def crossover():
    pass


# apply a mutuation function
def mutation():
    pass


# create a main genetic algorithm
def genetic_algorithm():
    pass
