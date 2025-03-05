import numpy as np
import pygame
import sys

class Road:
  def __init__(self):
     pass

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

class Store(Building):
    def __init__(self, name, width, height):
        super().__init__(name, width, height)
    def __str__(self):
        return "S"


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
    def __init__(self, name, width, height, water):
        super().__init__(name, width, height)
        self.water = water

class Sewage(Building):
    def __init__(self, name, width, height, sewage, pollution):
        super().__init__(name, width, height)
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
    def __init__(self, name, width, height, boost, area):
        super().__init__(name, width, height)
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
    
# step 1 create a population of random city layouts
def random_layout():
    pass


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