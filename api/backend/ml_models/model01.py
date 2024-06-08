from backend.db_connection import db
import numpy as np
import logging 
import matplotlib.pyplot as plt
import statistics as stats 


def predict(var1, var2, var3, var4):

    cursor = db.get_db().cursor()
    query = 'SELECT beta_vals FROM model1_params'
    cursor.execute(query)
    return_val = cursor.fetchone()
    logging.info(f'return val datatype = {type(return_val)}')
    params = return_val[0]
    logging.info(f'params = {params}')
    logging.info(f'params datatype = {type(params)}')

    index_query = f"""select index_num from country_table where country = '{var2}'"""
    cursor.execute(index_query)
    index_num = cursor.fetchone()

    num_countries_query = "select count(*) as countries from country_table"
    cursor.execute(num_countries_query)
    num_countries = cursor.fetchone()

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
    
    logging.info(f'var4: {var4}')
    age = np.array(list(map(float, var4[3:-1].split(' '))))
    
    logging.info(f'year = {year}')
    logging.info(f'array = {array}')
    logging.info(f'gender = {gender}')
    logging.info(f'age = {age}')
    logging.info(f"age dtype: {type(age)}")
    logging.info(f"age dim: {age.shape}")
    m = np.concatenate([np.array([1]), year, array, gender, age])
    prediction = np.exp(np.dot(params_array, m))

    return prediction 

