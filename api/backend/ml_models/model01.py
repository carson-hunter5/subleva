from backend.db_connection import db
"""
import numpy as np
"""

import logging 
import matplotlib.pyplot as plt
import statistics as stats 


def predict(var1, var2, var3, var4):

    cursor = db.get_db().cursor()
    query = 'SELECT beta_vals FROM model1_params ORDER BY sequence_number DESC LIMIT 1'
    cursor.execute(query)
    return_val = cursor.fetchone()
    params = return_val['beta_vals']
    logging.info(f'params = {params}')
    logging.info(f'params datatype = {type(params)}')

    index_query = f"""select index_num from country_table where country_name = {var2}"""
    cursor.execute(index_query)
    index_num = cursor.fetchone()

    num_countries = "select count(*) as countries from country_table"

    params_array = np.array(list(map(float, params[1:-1].split(','))))
    logging.info(f'params array = {params_array}')
    logging.info(f'params_array datatype = {type(params_array)}')
    year = np.array([var1])
   
    # if var2 in countries[0].values:
    array = np.zeros(num_countries, dtype=int) # replace len(countries) with result of count(*) query
    # index = countries[countries[0] == var2].index[0]
    array[index_num] = 1

    if var3 == 'Male':
        gender = np.array([1])
    else:
        gender = np.array([0])
        
    age = var4

    m = np.concatenate([year, array, gender, age])
    prediction = np.exp(np.dot(params_array, m))

    return prediction 

