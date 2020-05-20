#!/usr/bin/python
import random
import math
import pandas as pd

def read_csv():
    #Leyendo archivo
    df = pd.read_csv('InterpolatedWithCAPEX2.csv')
    df_N = pd.read_csv('InterpolatedNum.csv')
    max_D = {'D REVENUE':df['D REVENUE'].max(), 'U CR':df['U CR'].max(), 'D OE':df['D OE'].max(), 
       'D NOI':df['D NOI'].max(),'U CAPEX':df['U CAPEX'].max(), 'U CWK':df['U CWK'].max()} 
    min_D = {'D REVENUE':df['D REVENUE'].min(), 'U CR':df['U CR'].min(), 'D OE':df['D OE'].min(), 
       'D NOI':df['D NOI'].min(),'U CAPEX':df['U CAPEX'].min(), 'U CWK':df['U CWK'].min()}
    max_N = {'U REVENUE':df_N['U REVENUE'].max(), 'D CR':df_N['D CR'].max(), 'U OE':df_N['U OE'].max(), 
       'U NOI':df_N['U NOI'].max(),'D CAPEX':df_N['D CAPEX'].max(), 'D CWK':df_N['D CWK'].max()} 
    min_N = {'U REVENUE':df_N['U REVENUE'].min(), 'D CR':df_N['D CR'].min(), 'U OE':df_N['U OE'].min(), 
       'U NOI':df_N['U NOI'].min(),'D CAPEX':df_N['D CAPEX'].min(), 'D CWK':df_N['D CWK'].min()}
    
    # min_D['D REVENUE'] = lower_w1_boundary
    # max_D['D REVENUE'] = upper_w1_boundary
    # min_D['U CR'] = lower_w2_boundary
    # max_D['U CR'] = upper_w2_boundary
    # min_D['D OE'] = lower_w3_boundary
    # max_D['D OE'] = upper_w3_boundary
    # min_D['D NOI'] = lower_w4_boundary
    # max_D['D NOI'] = upper_w4_boundary
    # min_D['U CAPEX'] = lower_w5_boundary 
    # max_D['U CAPEX'] = upper_w5_boundary
    # min_D['U CWK'] = lower_w6_boundary
    # max_D['U CWK'] = upper_w6_boundary
    # min_N['U REVENUE'] = lower_w7_boundary 
    # max_N['U REVENUE'] = upper_w7_boundary
    # min_N['D CR'] = lower_w8_boundary
    # max_N['D CR'] = upper_w8_boundary
    # min_N['U OE'] = lower_w9_boundary
    # max_N['U OE'] = upper_w9_boundary
    # min_N['U NOI'] = lower_w10_boundary
    # max_N['U NOI'] = upper_w10_boundary
    # min_N['D CAPEX'] = lower_w11_boundary
    # max_N['D CAPEX'] = upper_w11_boundary
    # min_N['D CWK'] = lower_w12_boundary
    # max_N['D CWK'] = upper_w12_boundary
    filas_d, columnas_d = df.count()-1, len(df.columns)-1
    dataset_D = df.values
    #Variables a pasar a la funcion generate_population
    d_fcf = dataset_D[filas_d, columnas_d][1]
    filas_n, columnas_n = df_N.count()-1, len(df_N.columns)-1
    dataset_N = df_N.values
    u_fcf = dataset_N[filas_d, columnas_d][1]
    return min_D, min_N, max_N, max_D, u_fcf, d_fcf

def generate_population(min_D):
    population = []
    for i in range(size):
        individual = {
            "w1": random.uniform(min_D['D REVENUE'], upper_w1_boundary),
            "w2": random.uniform(lower_w2_boundary, upper_w2_boundary),
            "w3": random.uniform(lower_w3_boundary, upper_w3_boundary),
            "w4": random.uniform(lower_w4_boundary, upper_w4_boundary),
            "w5": random.uniform(lower_w5_boundary, upper_w5_boundary),
            "w6": random.uniform(lower_w6_boundary, upper_w6_boundary),
            "w7": random.uniform(lower_w7_boundary, upper_w7_boundary),
            "w8": random.uniform(lower_w8_boundary, upper_w8_boundary),
            "w9": random.uniform(lower_w9_boundary, upper_w9_boundary),
            "w10": random.uniform(lower_w10_boundary, upper_w10_boundary),
            "w11": random.uniform(lower_w11_boundary, upper_w11_boundary),
            "w12": random.uniform(lower_w12_boundary, upper_w12_boundary),
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
    x9 = -0.205
    x10 = -0.0174
    x11 = 0.4339
    x12 = -0.21    
    w1_i = 1661333
    w2_i = 543588.624
    w3_i = 306677.854
    w4_i = 23471.7706
    w5_i = 901510.1974
    w6_i = 295234.827
    w7_i = 137285.752
    w8_i = 635649.436
    w9_i = 901510.1974
    w10_i = 295234.827
    w11_i = 137285.752
    w12_i = 635649.436
    w1 = individual["w1"]
    w2 = individual["w2"]
    w3 = individual["w3"]
    w4 = individual["w4"]
    w5 = individual["w5"]
    w6 = individual["w6"]
    w7 = individual["w7"]
    w8 = individual["w8"]
    w9 = individual["w9"]
    w10 = individual["w10"]
    w11 = individual["w11"]
    w12 = individual["w12"]
    numerator_i = ((w1_i*x1) + (w2_i*x2) + (w3_i*x3) + (w4_i*x4))
    denominator_i = ((w5_i*x5) + (w6_i*x6) + (w7_i*x7) + (w8_i*x8))
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
    population = generate_population(size=10)

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

