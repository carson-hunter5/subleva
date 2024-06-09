import pandas as pd
import numpy as np
from backend.db_connection import db
import logging 
import matplotlib.pyplot as plt
import statistics as stats 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_predict(var1,var2,var3,var4):
    cursor = db.get_db().cursor()
    query = "SELECT year,coo_name,coa_name,dec_recognized,dec_rejected,dec_total,acceptance_rate FROM decisionStats;"
    cursor.execute(query)
    logging.info(f"query is {query}")
    return_val = cursor.fetchall()
    # logging.info(f"return val is {return_val}")
    asylum_decisions = pd.DataFrame(return_val)
    asylum_decisions = asylum_decisions.rename(columns={0: "year", 1: "coo_name", 2: "coa_name", 3: "dec_recognized", 4: "dec_rejected", 5: "dec_total", 6: "acceptance_rate"})
    logging.info(f"df is {asylum_decisions}")

    label_encoder = LabelEncoder()
    asylum_decisions['coo_name'] = label_encoder.fit_transform(asylum_decisions['coo_name'])
    new_coo = label_encoder.transform(np.array([var2]))

    asylum_decisions['coa_name'] = label_encoder.fit_transform(asylum_decisions['coa_name'])
    new_coa = label_encoder.transform(np.array([var3]))
    logging.info(f"Asylum decisons psot logging  {asylum_decisions}")

    X = asylum_decisions[['year', 'coo_name', 'coa_name', 'dec_total']]
    logging.info(f"X:{X}")
    y = asylum_decisions['acceptance_rate']

    X_predict = np.array([var1, new_coo[0], new_coa[0], var4])
    logging.info(f'X_predict is: {X_predict.reshape(1,-1)}')

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X, y)

    y_pred = rf_regressor.predict(X_predict.reshape(1,-1))

    return y_pred
