import random
import math
import pandas as pd
import numpy as np
import json
from keras.models import model_from_json
from numpy import array

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
ufcf = 0.0
dfcf = 0.0
max_D = {}
min_D = {}
max_N = {}
min_N = {}

class boundaries:
    max_D = {}
    min_D = {}
    max_N = {}
    min_N = {}

    def __init__(self, max_D, min_D, max_N, min_N): 
        self.max_D = max_D 
        self.min_D = min_D
        self.max_N = max_N
        self.min_N = min_N

def read_csv():
    #Leyendo archivo
    df = pd.read_csv('Interpolation/CHKP/InterpolatedDenWeekCHKP.csv')
    df_N = pd.read_csv('Interpolation/CHKP/InterpolatedNumWeekCHKP.csv')
    global ufcf, dfcf, max_D, max_N, min_D, min_N
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12
    #Denominador
    max_D = {'D Revenue':df['D Revenue'].max(), 'U CR':df['U CR'].max(), 'D OE':df['D OE'].max(), 
       'U NOI':df['U NOI'].max(),'U CAPEX':df['U CAPEX'].max(), 'U WK':df['U WK'].max()} 
    min_D = {'D Revenue':df['D Revenue'].min(), 'U CR':df['U CR'].min(), 'D OE':df['D OE'].min(), 
       'U NOI':df['U NOI'].min(),'U CAPEX':df['U CAPEX'].min(), 'U WK':df['U WK'].min()}
    #Numerador
    max_N = {'U Revenue':df_N['U Revenue'].max(), 'D CR':df_N['D CR'].max(), 'U OE':df_N['U OE'].max(), 
       'D NOI':df_N['D NOI'].max(),'D CAPEX':df_N['D CAPEX'].max(), 'D WK':df_N['D WK'].max()} 
    min_N = {'U Revenue':df_N['U Revenue'].min(), 'D CR':df_N['D CR'].min(), 'U OE':df_N['U OE'].min(), 
       'D NOI':df_N['D NOI'].min(),'D CAPEX':df_N['D CAPEX'].min(), 'D WK':df_N['D WK'].min()}
   
    filas_d, columnas_d = df.count()-1, len(df.columns)-1
    dataset_D = df.values
    #Variables a pasar a la funcion generate_population
    dfcf = float(dataset_D[filas_d, columnas_d][1])
    filas_n, columnas_n = df_N.count()-1, len(df_N.columns)-1
    dataset_N = df_N.values
    ufcf = float(dataset_N[filas_d, columnas_d][1])
    
    boundaries_x = boundaries(max_D, min_D, max_N, min_N)
        
    
    ##Calculo de las x
    #Numerador
    x1 = df_N['U Revenue'].corr(df_N['U FCF'])
    x2 = df_N['D CR'].corr(df_N['U FCF'])
    x3 = df_N['U OE'].corr(df_N['U FCF'])
    x4 = df_N['D NOI'].corr(df_N['U FCF'])
    x5 = df_N['D CAPEX'].corr(df_N['U FCF'])
    x6 = df_N['D WK'].corr(df_N['U FCF'])
    x7 = df['D Revenue'].corr(df['D FCF'])
    #Denominador
    x8 = df['U CR'].corr(df['D FCF'])
    x9 = df['D OE'].corr(df['D FCF'])
    x10 = df['U NOI'].corr(df['D FCF'])
    x11 = df['U CAPEX'].corr(df['D FCF'])
    x12 = df['U WK'].corr(df['D FCF'])

    return boundaries_x


def generate_population(boundarie, size):
    population = []
    min_N = boundarie.min_N
    max_N = boundarie.max_N
    min_D = boundarie.min_D
    max_D = boundarie.max_D
    for i in range(size):
        individual = {
            "w1": random.uniform(min_N['U REVENUE'], max_N['U REVENUE']),
            "w2": random.uniform(min_N['D CR'], max_N['D CR']),
            "w3": random.uniform(min_N['U OE'], max_N['U OE']),
            "w4": random.uniform(min_N['U NOI'], max_N['U NOI']),
            "w5": random.uniform(min_N['D CAPEX'], max_N['D CAPEX']),
            "w6": random.uniform(min_N['D CWK'], max_N['D CWK']),
            "w7": random.uniform(min_D['D REVENUE'], max_D['D REVENUE']),
            "w8": random.uniform(min_D['U CR'], max_D['U CR']),
            "w9": random.uniform(min_D['D OE'], max_D['D OE']),
            "w10": random.uniform(min_D['D NOI'], max_D['D NOI']),
            "w11": random.uniform(min_D['U CAPEX'], max_D['U CAPEX']),
            "w12": random.uniform(min_D['U CWK'], max_D['U CWK']),
        }    
        population.append(individual)
    return population

def apply_function(individual):
    # Numerador
    # load json and create model 
    # Numerador
    # load json and create model
    json_file = open('C:/Users/alejo/Documents/Proyecto_Integrador_2/AI_Value/Combination/Interpolation/CHKP/modelNumCHKP.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_num = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model_num.load_weights('C:/Users/alejo/Documents/Proyecto_Integrador_2/AI_Value/Combination/Interpolation/CHKP/modelNumCHKP.h5')
    # Denominador
    json_file = open('C:/Users/alejo/Documents/Proyecto_Integrador_2/AI_Value/Combination/Interpolation/CHKP/modeldenCHKP.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_den = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model_den.load_weights('C:/Users/alejo/Documents/Proyecto_Integrador_2/AI_Value/Combination/Interpolation/CHKP/modeldenCHKP.h5')    
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
    #Numerador
    w1_std = (w1-min_N['U Revenue'])/(max_N['U Revenue']-min_N['U Revenue'])
    w2_std = (w2-min_N['D CR'])/(max_N['D CR']-min_N['D CR'])
    w3_std = (w3-min_N['U OE'])/(max_N['U OE']-min_N['U OE'])
    w4_std = (w4-min_N['D NOI'])/(max_N['D NOI']-min_N['D NOI'])
    w5_std = (w5-min_N['D CAPEX'])/(max_N['D CAPEX']-min_N['D CAPEX'])
    w6_std = (w6-min_N['D WK'])/(max_N['D WK']-min_N['D WK'])
    #Denominador
    w7_std = (w7-min_D['D Revenue'])/(max_D['D Revenue']-min_D['D Revenue'])
    w8_std = (w8-min_D['U CR'])/(max_D['U CR']-min_D['U CR'])
    w9_std = (w9-min_D['D OE'])/(max_D['D OE']-min_D['D OE'])
    w10_std = (w10-min_D['U NOI'])/(max_D['U NOI']-min_D['U NOI'])
    w11_std = (w11-min_D['U CAPEX'])/(max_D['U CAPEX']-min_D['U CAPEX'])
    w12_std = (w12-min_D['U WK'])/(max_D['U WK']-min_D['U WK'])
    w_numerador = [[w1_std, w2_std, w3_std, w4_std, w5_std, w6_std]]
    w_denominador = [[w7_std, w8_std, w9_std, w10_std, w11_std, w12_std]]
    Xnewnum = array(w_numerador)
    Xnewden = array(w_denominador)
    # make a prediction
    numerador = loaded_model_num.predict(Xnewnum) 
    denominador = loaded_model_den.predict(Xnewden)
    function_costo1 = ufcf/dfcf
    function_costo2 = numerador/denominador
    function_costo2num = function_costo2[0][0]
    function_result = (function_costo2num - function_costo1)/function_costo1
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
    min_value = -1
    max_value = 1
    next_w1 = individual["w1"] * (1+random.uniform(min_value, max_value)) 
    next_w2 = individual["w2"] * (1+random.uniform(min_value, max_value))
    next_w3 = individual["w3"] * (1+random.uniform(min_value, max_value))
    next_w4 = individual["w4"] * (1+random.uniform(min_value, max_value))
    next_w5 = individual["w5"] * (1+random.uniform(min_value, max_value))
    next_w6 = individual["w6"] * (1+random.uniform(min_value, max_value))
    next_w7 = individual["w7"] * (1+random.uniform(min_value, max_value))
    next_w8 = individual["w8"] * (1+random.uniform(min_value, max_value))
    next_w9 = individual["w9"] * (1+random.uniform(min_value, max_value))
    next_w10 = individual["w10"] * (1+random.uniform(min_value, max_value))
    next_w11 = individual["w11"] * (1+random.uniform(min_value, max_value))
    next_w12 = individual["w12"] * (1+random.uniform(min_value, max_value))

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
    generations = 10
    #min_value = 0
    #max_value = 0.85    
    boundaries_x = read_csv()    
    population = generate_population(boundarie=boundaries_x, size=10)

    i = 1
    while True:
        print(f"🧬 GENERATION {i}")

        for individual in population:
             print(individual, apply_function(individual))

        if i == generations:
            break

        i += 1

        population = make_next_generation(population)

    best_individual = sort_population_by_fitness(population)[-1]
    print("\n🔬 FINAL RESULT")
    print(best_individual, (apply_function(best_individual)*100), "%")

if __name__ == "__main__":
    main()
