import random
import numpy as np

# Define grid size
GRID_SIZE = 10  # Example 5x5 grid

# Define building types
BUILDINGS = ['R', 'P', 'S']  # R = Residential, P = Park, S = Service

# Define population base values and boosts
BASE_POPULATION = {'R': 100, 'P': 0, 'S': 0}
BOOSTS = {'P': 1.2, 'S': 1.5}  # Parks and Services boost adjacent residentials

# Generate random city layout
def random_layout():
    return [[random.choice(BUILDINGS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Evaluate population score
def evaluate_layout(layout):
    total_population = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if layout[i][j] == 'R':
                boost_factor = 1
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                        if layout[ni][nj] in BOOSTS:
                            boost_factor *= BOOSTS[layout[ni][nj]]
                total_population += BASE_POPULATION['R'] * boost_factor
    return total_population

def generate_population(size):
    return [random_layout() for _ in range(size)]

def select_best(population, num_best):
    return sorted(population, key=evaluate_layout, reverse=True)[:num_best]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, GRID_SIZE - 1)
    child = [row[:] for row in parent1]
    for i in range(crossover_point, GRID_SIZE):
        child[i] = parent2[i]
    return child

def mutate(layout):
    i, j = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    layout[i][j] = random.choice(BUILDINGS)
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
    return select_best(population, 1)[0]

# Run the algorithm
best_layout = genetic_algorithm()
for row in best_layout:
    print(row)
print("Max Population:", evaluate_layout(best_layout))
