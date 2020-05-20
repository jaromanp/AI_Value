#!/usr/bin/python
import random
import math
import pandas as pd
import numpy as np

class Correlaciones:
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ufcf = np.empty(1)
    dfcf = np.empty(1)
    max_D = {} 
    min_D = {}
    max_N = {}
    min_N = {}


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
    
    filas_d, columnas_d = df.count()-1, len(df.columns)-1
    dataset_D = df.values
    #Variables a pasar a la funcion generate_population
    d_fcf = dataset_D[filas_d, columnas_d][1]
    filas_n, columnas_n = df_N.count()-1, len(df_N.columns)-1
    dataset_N = df_N.values
    u_fcf = dataset_N[filas_d, columnas_d][1]
    ##Falta idear una forma en la que se pueda pasar u_fcf y d_fcf a apply function que no se por parametro

    ##Calculo de las x
    x1 = df_N['U REVENUE'].corr(df_N['U FCF'])
    x2 = df_N['D CR'].corr(df_N['U FCF'])
    x3 = df_N['U OE'].corr(df_N['U FCF'])
    x4 = df_N['U NOI'].corr(df_N['U FCF'])
    x5 = df_N['D CAPEX'].corr(df_N['U FCF'])
    x6 = df_N['D CWK'].corr(df_N['U FCF'])
    x7 = df['D REVENUE'].corr(df['D FCF'])
    x8 = df['U CR'].corr(df['D FCF'])
    x9 = df['D OE'].corr(df['D FCF'])
    x10 = df['D NOI'].corr(df['D FCF'])
    x11 = df['U CAPEX'].corr(df['D FCF'])
    x12 = df['U CWK'].corr(df['D FCF'])

    correlaciones_x = Correlaciones()
    correlaciones_x.x1 = x1
    correlaciones_x.x2 = x2
    correlaciones_x.x3 = x3
    correlaciones_x.x4 = x4
    correlaciones_x.x5 = x5
    correlaciones_x.x6 = x6
    correlaciones_x.x7 = x7
    correlaciones_x.x8 = x8
    correlaciones_x.x9 = x9
    correlaciones_x.x10 = x10
    correlaciones_x.x11 = x11
    correlaciones_x.x12 = x12
    correlaciones_x.dfcf = d_fcf
    correlaciones_x.ufcf = u_fcf
    correlaciones_x.max_D = max_D
    correlaciones_x.min_D = min_D
    correlaciones_x.max_N = max_N
    correlaciones_x.min_N = min_N
    
    return correlaciones_x

def generate_population(correlaciones_x, size):
    population = []
    for i in range(size):
        individual = {
            "w1": random.uniform(correlaciones_x.min_N['U REVENUE'], correlaciones_x.max_N['U REVENUE']),
            "w2": random.uniform(correlaciones_x.min_N['D CR'], correlaciones_x.max_N['D CR']),
            "w3": random.uniform(correlaciones_x.min_N['U OE'], correlaciones_x.max_N['U OE']),
            "w4": random.uniform(correlaciones_x.min_N['U NOI'], correlaciones_x.max_N['U NOI']),
            "w5": random.uniform(correlaciones_x.min_N['D CAPEX'], correlaciones_x.max_N['D CAPEX']),
            "w6": random.uniform(correlaciones_x.min_N['D CWK'], correlaciones_x.max_N['D CWK']),
            "w7": random.uniform(correlaciones_x.min_D['D REVENUE'], correlaciones_x.max_D['D REVENUE']),
            "w8": random.uniform(correlaciones_x.min_D['U CR'], correlaciones_x.max_D['U CR']),
            "w9": random.uniform(correlaciones_x.min_D['D OE'], correlaciones_x.max_D['D OE']),
            "w10": random.uniform(correlaciones_x.min_D['D NOI'], correlaciones_x.max_D['D NOI']),
            "w11": random.uniform(correlaciones_x.min_D['U CAPEX'], correlaciones_x.max_D['U CAPEX']),
            "w12": random.uniform(correlaciones_x.min_D['U CWK'], correlaciones_x.max_D['U CWK']),
            "dfcf": correlaciones_x.dfcf,
            "ufcf": correlaciones_x.ufcf,
            "x1":correlaciones_x.x1,
            "x2":correlaciones_x.x2,
            "x3":correlaciones_x.x3,
            "x4":correlaciones_x.x4,
            "x5":correlaciones_x.x5,
            "x6":correlaciones_x.x6,
            "x7":correlaciones_x.x7,
            "x8":correlaciones_x.x8,
            "x9":correlaciones_x.x9,
            "x10":correlaciones_x.x10,
            "x11":correlaciones_x.x11,
            "x12":correlaciones_x.x12 
        }
        population.append(individual)
    return population

def apply_function(individual):
    ufcf = np.empty(1)
    dfcf = np.empty(1)
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
    ufcf = individual["ufcf"]
    dfcf = individual["dfcf"]
    x1 = individual["x1"]
    x2 = individual["x2"]
    x3 = individual["x3"]
    x4 = individual["x4"]
    x5 = individual["x5"]
    x6 = individual["x6"]
    x7 = individual["x7"]
    x8 = individual["x8"]
    x9 = individual["x9"]
    x10 = individual["x10"]
    x11 = individual["x11"]
    x12 = individual["x11"]
    numerator = ((w1*x1) + (w2*x2) + (w3*x3) + (w4*x4) + (w5*x5) + (w6*x6))
    denominator = ((w7*x7) + (w8*x8) + (w9*x9) + (w10*x10) + (w11*x11) + (w12*x12))
    function_costo1 = ufcf/dfcf
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
    w9a = individual_a["w9"]
    w10a = individual_a["w10"]
    w11a = individual_a["w11"]
    w12a = individual_a["w12"]
    

    w1b = individual_b["w1"]
    w2b = individual_b["w2"]
    w3b = individual_b["w3"]
    w4b = individual_b["w4"]
    w5b = individual_b["w5"]
    w6b = individual_b["w6"]
    w7b = individual_b["w7"]
    w8b = individual_b["w8"]
    w9b = individual_b["w9"]
    w10b = individual_b["w10"]
    w11b = individual_b["w11"]
    w12b = individual_b["w12"]

    result_crossover = {"w1": (w1a + w1b) / 2, "w2": (w2a + w2b) / 2, "w3": (w3a + w3b) / 2, "w4": (w4a + w4b) / 2, 
    "w5": (w5a + w5b) / 2, "w6": (w6a + w6b) / 2, "w7": (w7a + w7b) / 2, "w8": (w8a + w8b) / 2,
    "w9": (w9a + w9b) / 2, "w10": (w10a + w10b) / 2, "w11": (w11a + w11b) / 2, "w12": (w12a + w12b) / 2}
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
    next_w9 = individual["w9"] + random.uniform(min_value, max_value)
    next_w10 = individual["w10"] + random.uniform(min_value, max_value)
    next_w11 = individual["w11"] + random.uniform(min_value, max_value)
    next_w12 = individual["w12"] + random.uniform(min_value, max_value)

    #lower_boundary, upper_boundary = (0, 1)

    # Guarantee we keep inside boundaries
    # next_w1 = min(max(next_w1, individual[]), 405424332.26)
    # next_w2 = min(max(next_w2, 0.00019), 131706692)
    # next_w3 = min(max(next_w3, 0.00082), 55436546)
    # next_w4 = min(max(next_w4, 0), 11049981)
    # next_w5 = min(max(next_w5, 0), 244756190.2)
    # next_w6 = min(max(next_w6, 0), 85395371.6)
    # next_w7 = min(max(next_w7, 0.00057), 34517447.3)
    # next_w8 = min(max(next_w8, 0), 291192077)

    result_mutation = {"w1": next_w1, "w2": next_w2, "w3": next_w3, "w4": next_w4, "w5": next_w5,
    "w6": next_w6, "w7": next_w7, "w8": next_w8, "w9": next_w9, "w10": next_w10, "w11": next_w11, "w12": next_w12}
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
    #No estoy seguro pero creo necesito verificacion por parte de otro programador gracias
    correlaciones_obj = read_csv()
    population = generate_population(correlaciones_x=correlaciones_obj, size=10)

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

