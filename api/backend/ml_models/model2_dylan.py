import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def get_data(url):
    
    category = str(url)
    response = requests.get(category)
    data = response.json()
    data_dict = data["items"]
    
    data = pd.DataFrame.from_records(data_dict)
    
    return data

asylum_decisions = get_data('https://api.unhcr.org/population/v1/asylum-decisions/?&yearFrom=2010&yearTo=2025&coo_all=TRUE&limit=10000000&coa_all=TRUE')

asylum_decisions = asylum_decisions.dropna()
asylum_decisions[['year', 'dec_recognized', 'dec_other', 'dec_rejected', 'dec_closed', 'dec_total']] = asylum_decisions[['year', 'dec_recognized', 'dec_other', 'dec_rejected', 'dec_closed', 'dec_total']].astype(int)
asylum_decisions = asylum_decisions.drop(['dec_pc', 'coo_iso', 'coa', 'coa_iso', 'procedure_type', 'dec_level', 'dec_pc'], axis=1)
asylum_decisions = asylum_decisions[asylum_decisions.coo != 'UKN']

asylum_decisions["dec_rejected"] = asylum_decisions['dec_total'] - asylum_decisions['dec_recognized']

asylum_decisions = asylum_decisions.drop(['coa_name', 'coo', 'coo_name', 'dec_other', 'dec_closed'], axis = 1)


asylum_decisions = asylum_decisions[asylum_decisions['dec_total'] > 0]

asylum_decisions['acceptance_rate'] = asylum_decisions['dec_recognized'] / asylum_decisions['dec_total'] 


X = asylum_decisions[['year', 'coo_id', 'coa_id', 'dec_total']]
y = asylum_decisions['acceptance_rate']

# split data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# regression and fit model
rf_regressor = RandomForestRegressor(n_estimators=100)
rf_regressor.fit(X_train, y_train)
y_pred = rf_regressor.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('mse:', mse)
print('r2:', r2)

