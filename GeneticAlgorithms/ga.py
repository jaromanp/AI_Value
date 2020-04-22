#!/usr/bin/python
import random
import math

def generate_population(size, w1_boundaries, w2_boundaries, w3_boundaries, w4_boundaries, w5_boundaries):
    lower_w1_boundary, upper_w1_boundary = w1_boundaries
    lower_w2_boundary, upper_w2_boundary = w2_boundaries
    lower_w3_boundary, upper_w3_boundary = w3_boundaries
    lower_w4_boundary, upper_w4_boundary = w4_boundaries
    lower_w5_boundary, upper_w5_boundary = w5_boundaries

    population = []
    for i in range(size):
        individual = {
            "w1": random.uniform(lower_w1_boundary, upper_w1_boundary),
            "w2": random.uniform(lower_w2_boundary, upper_w2_boundary),
            "w3": random.uniform(lower_w3_boundary, upper_w3_boundary),
            "w4": random.uniform(lower_w4_boundary, upper_w4_boundary),
            "w5": random.uniform(lower_w5_boundary, upper_w5_boundary),
        }
        population.append(individual)

    return population

def apply_function(individual):
    x1 = 700000
    x2 = 1000000
    x3 = 800000
    x4 = 1000000
    x5 = 600000
    alfa = 500
    w1 = individual["w1"]
    w2 = individual["w2"]
    w3 = individual["w3"]
    w4 = individual["w4"]
    w5 = individual["w5"]
    numerator = (w1 + w2 + w3 + w4 + w5)
    if numerator == 1:
        function_result = (((numerator/(alfa + (w1*x1) + (w2*x2) + (w3*x3) + (w4*x4) + (w5*x5))))/1)
    else:
        penalty = ((999999)*((1-numerator)**2))
        function_result = ((((numerator/(alfa + (w1*x1) + (w2*x2) + (w3*x3) + (w4*x4) + (w5*x5)))-(penalty)))/1)
    return function_result

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
    w1a = individual_a["w1"]
    w2a = individual_a["w2"]
    w3a = individual_a["w3"]
    w4a = individual_a["w4"]
    w5a = individual_a["w5"]

    w1b = individual_b["w1"]
    w2b = individual_b["w2"]
    w3b = individual_b["w3"]
    w4b = individual_b["w4"]
    w5b = individual_b["w5"]

    result_crossover = {"w1": (w1a + w1b) / 2, "w2": (w2a + w2b) / 2, "w3": (w3a + w3b) / 2, "w4": (w4a + w4b) / 2, "w5": (w5a + w5b) / 2}
    return result_crossover


def mutate(individual):
    min_value = -0.00025
    max_value = 0.00025
    next_w1 = individual["w1"] + random.uniform(min_value, max_value)
    next_w2 = individual["w2"] + random.uniform(min_value, max_value)
    next_w3 = individual["w3"] + random.uniform(min_value, max_value)
    next_w4 = individual["w4"] + random.uniform(min_value, max_value)
    next_w5 = individual["w5"] + random.uniform(min_value, max_value)

    lower_boundary, upper_boundary = (0, 1)

    # Guarantee we keep inside boundaries
    next_w1 = min(max(next_w1, lower_boundary), upper_boundary)
    next_w2 = min(max(next_w2, lower_boundary), upper_boundary)
    next_w3 = min(max(next_w3, lower_boundary), upper_boundary)
    next_w4 = min(max(next_w4, lower_boundary), upper_boundary)
    next_w5 = min(max(next_w5, lower_boundary), upper_boundary)

    result_mutation = {"w1": next_w1, "w2": next_w2, "w3": next_w3, "w4": next_w4, "w5": next_w5}
    return result_mutation


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
    generations = 5000
    min_value = 0
    max_value = 0.85
    population = generate_population(size=10, w1_boundaries=(min_value, max_value), w2_boundaries=(min_value, max_value), w3_boundaries=(min_value, max_value), w4_boundaries=(min_value, max_value), w5_boundaries=(min_value, max_value))

    i = 1
    while True:
        #print(f"🧬 GENERATION {i}")

        #for individual in population:
        #    print(individual, apply_function(individual))

        if i == generations:
            break

        i += 1

        population = make_next_generation(population)

    best_individual = sort_population_by_fitness(population)[-1]
    print("\n🔬 FINAL RESULT")
    print(best_individual, apply_function(best_individual))

if __name__ == "__main__":
    main()

