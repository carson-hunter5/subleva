from backend.db_connection import db
import numpy as np
import logging 
import matplotlib.pyplot as plt
import statistics as stats 


def predict(var1, var2, var3, var4):
    year = np.array([var1])
   
    if var2 in countries[0].values:
        array = np.zeros(len(countries), dtype=int)
        index = countries[countries[0] == var2].index[0]
        array[index] = 1

    if var3 == 'Male':
        gender = np.array([1])
    else:
        gender = np.array([0])
        
    age = var4

    m = np.concatenate([year, array, gender, age])
    return m