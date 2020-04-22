#!/usr/bin/python
import random
import math

def generate_population(size, x_boundaries, y_boundaries):
    lower_x_boundary, upper_x_boundary = x_boundaries
    lower_y_boundary, upper_y_boundary = y_boundaries

    population = []
    for i in range(size):
        individual = {
            "w1": random.uniform(lower_x_boundary, upper_x_boundary),
            "w2": random.uniform(lower_y_boundary, upper_y_boundary),
            "w3": random.uniform(lower_y_boundary, upper_y_boundary),
            "w4": random.uniform(lower_y_boundary, upper_y_boundary),
            "w5": random.uniform(lower_y_boundary, upper_y_boundary),
        }
        population.append(individual)

    return population

def apply_function(individual):
    x1 = 20
    x2 = 45
    x3 = 72
    x4 = 1
    x5 = 59
    alfa = 5
    w1 = individual["w1"]
    w2 = individual["w2"]
    w3 = individual["w3"]
    w4 = individual["w4"]
    w5 = individual["w5"]
    function_result = ((w1 + w2 + w3 + w4 + w5)/())
    return 

def choice_by_roulette(sorted_population, fitness_sum):
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = apply_function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = apply_function(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual

def sort_population_by_fitness(population):
    return sorted(population, key=apply_function)


def crossover(individual_a, individual_b):
    xa = individual_a["x"]
    ya = individual_a["y"]

    xb = individual_b["x"]
    yb = individual_b["y"]

    return {"x": (xa + xb) / 2, "y": (ya + yb) / 2}


def mutate(individual):
    next_x = individual["x"] + random.uniform(-0.05, 0.05)
    next_y = individual["y"] + random.uniform(-0.05, 0.05)

    lower_boundary, upper_boundary = (-4, 4)

    # Guarantee we keep inside boundaries
    next_x = min(max(next_x, lower_boundary), upper_boundary)
    next_y = min(max(next_y, lower_boundary), upper_boundary)

    return {"x": next_x, "y": next_y}


def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(apply_function(individual) for individual in previous_population)

    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        second_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation

def main():
    generations = 100
    population = generate_population(size=10, x_boundaries=(-4, 4), y_boundaries=(-4, 4))

    i = 1
    while True:
        # print(f"🧬 GENERATION {i}")

        # for individual in population:
        #     print(individual, apply_function(individual))

        if i == generations:
            break

        i += 1

        population = make_next_generation(population)

    best_individual = sort_population_by_fitness(population)[-1]
    # print("\n🔬 FINAL RESULT")
    print(best_individual, apply_function(best_individual))

if __name__ == "__main__":
    main()

