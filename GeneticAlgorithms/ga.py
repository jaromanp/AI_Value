#!/usr/bin/python
import random
import math

def generate_population(size, w1_boundaries, w2_boundaries, w3_boundaries, w4_boundaries, w5_boundaries,
w6_boundaries, w7_boundaries, w8_boundaries):
    lower_w1_boundary, upper_w1_boundary = w1_boundaries
    lower_w2_boundary, upper_w2_boundary = w2_boundaries
    lower_w3_boundary, upper_w3_boundary = w3_boundaries
    lower_w4_boundary, upper_w4_boundary = w4_boundaries
    lower_w5_boundary, upper_w5_boundary = w5_boundaries
    lower_w6_boundary, upper_w6_boundary = w6_boundaries
    lower_w7_boundary, upper_w7_boundary = w7_boundaries
    lower_w8_boundary, upper_w8_boundary = w8_boundaries

    population = []
    for i in range(size):
        individual = {
            "w1": random.uniform(lower_w1_boundary, upper_w1_boundary),
            "w2": random.uniform(lower_w2_boundary, upper_w2_boundary),
            "w3": random.uniform(lower_w3_boundary, upper_w3_boundary),
            "w4": random.uniform(lower_w4_boundary, upper_w4_boundary),
            "w5": random.uniform(lower_w5_boundary, upper_w5_boundary),
            "w6": random.uniform(lower_w3_boundary, upper_w3_boundary),
            "w7": random.uniform(lower_w4_boundary, upper_w4_boundary),
            "w8": random.uniform(lower_w5_boundary, upper_w5_boundary),
        }
        population.append(individual)

    return population

def apply_function(individual):
    x1 = -0.3352
    x2 = 1.2386
    x3 = 0.6935
    x4 = -0.205
    x5 = -0.0174
    x6 = 0.4339
    x7 = -0.21
    x8 = 0.0636    
    alfa_1 = -5143.9736
    alfa_2 = 50229.0441
    w1_i = 1661333
    w2_i = 543588.624
    w3_i = 306677.854
    w4_i = 23471.7706
    w5_i = 901510.1974
    w6_i = 295234.827
    w7_i = 137285.752
    w8_i = 635649.436
    w1 = individual["w1"]
    w2 = individual["w2"]
    w3 = individual["w3"]
    w4 = individual["w4"]
    w5 = individual["w5"]
    w6 = individual["w6"]
    w7 = individual["w7"]
    w8 = individual["w8"]
    numerator_i = (alfa_1 + (w1_i*x1) + (w2_i*x2) + (w3_i*x3) + (w4_i*x4))
    denominator_i = (alfa_2 + (w5_i*x5) + (w6_i*x6) + (w7_i*x7) + (w8_i*x8))
    numerator = (alfa_1 + (w1*x1) + (w2*x2) + (w3*x3) + (w4*x4))
    denominator = (alfa_2 + (w5*x5) + (w6*x6) + (w7*x7) + (w8*x8))
    function_costo1 = numerator_i/denominator_i
    #print(function_costo1)
    function_costo2 = numerator/denominator
    #print(function_costo2)
    function_result = (function_costo2 - function_costo1)/function_costo1
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
    w6a = individual_a["w6"]
    w7a = individual_a["w7"]
    w8a = individual_a["w8"]

    w1b = individual_b["w1"]
    w2b = individual_b["w2"]
    w3b = individual_b["w3"]
    w4b = individual_b["w4"]
    w5b = individual_b["w5"]
    w6b = individual_b["w6"]
    w7b = individual_b["w7"]
    w8b = individual_b["w8"]

    result_crossover = {"w1": (w1a + w1b) / 2, "w2": (w2a + w2b) / 2, "w3": (w3a + w3b) / 2, "w4": (w4a + w4b) / 2, 
    "w5": (w5a + w5b) / 2, "w6": (w6a + w6b) / 2, "w7": (w7a + w7b) / 2, "w8": (w8a + w8b) / 2}
    return result_crossover


def mutate(individual):
    min_value = -0.05
    max_value = 0.05
    next_w1 = individual["w1"] + random.uniform(min_value, max_value)
    next_w2 = individual["w2"] + random.uniform(min_value, max_value)
    next_w3 = individual["w3"] + random.uniform(min_value, max_value)
    next_w4 = individual["w4"] + random.uniform(min_value, max_value)
    next_w5 = individual["w5"] + random.uniform(min_value, max_value)
    next_w6 = individual["w6"] + random.uniform(min_value, max_value)
    next_w7 = individual["w7"] + random.uniform(min_value, max_value)
    next_w8 = individual["w8"] + random.uniform(min_value, max_value)

    #lower_boundary, upper_boundary = (0, 1)

    # Guarantee we keep inside boundaries
    next_w1 = min(max(next_w1, 0.0002), 405424332.26)
    next_w2 = min(max(next_w2, 0.00019), 131706692)
    next_w3 = min(max(next_w3, 0.00082), 55436546)
    next_w4 = min(max(next_w4, 0), 11049981)
    next_w5 = min(max(next_w5, 0), 244756190.2)
    next_w6 = min(max(next_w6, 0), 85395371.6)
    next_w7 = min(max(next_w7, 0.00057), 34517447.3)
    next_w8 = min(max(next_w8, 0), 291192077)

    result_mutation = {"w1": next_w1, "w2": next_w2, "w3": next_w3, "w4": next_w4, "w5": next_w5,
    "w6": next_w6, "w7": next_w7, "w8": next_w8}
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
    generations = 2000
    #min_value = 0
    #max_value = 0.85
    population = generate_population(size=10, w1_boundaries=(0.0002, 405424332.26), w2_boundaries=(0.00019, 131706692),
    w3_boundaries=(0.00082, 55436546), w4_boundaries=(0, 11049981), w5_boundaries=(0, 244756190.2),
    w6_boundaries=(0, 85395371.6), w7_boundaries=(0.00057, 34517447.3), w8_boundaries=(0, 291192077))

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
    print(best_individual, (apply_function(best_individual)*100), "%")

if __name__ == "__main__":
    main()

