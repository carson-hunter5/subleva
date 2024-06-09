import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint
import json
import os

def get_data(url):
    
    category = str(url)
    response = requests.get(category)
    data = response.json()
    data_dict = data["items"]
    
    data = pd.DataFrame.from_records(data_dict)
    
    return data

asylum_decisions = get_data('https://api.unhcr.org/population/v1/asylum-decisions/?&yearFrom=2010&yearTo=2025&coo_all=TRUE&limit=10000000&coa_all=TRUE')
asylum_decisions.to_csv('asylum_decisions.csv', header=True, index=False)
asylum_decisions = pd.read_csv('asylum_decisions.csv')

asylum_decisions = asylum_decisions.dropna()
asylum_decisions[['year', 'dec_recognized', 'dec_other', 'dec_rejected', 'dec_closed', 'dec_total']] = asylum_decisions[['year', 'dec_recognized', 'dec_other', 'dec_rejected', 'dec_closed', 'dec_total']].astype(int)
asylum_decisions = asylum_decisions.drop(['dec_pc', 'coo_iso', 'coa', 'coa_iso', 'procedure_type', 'dec_level', 'dec_pc'], axis=1)
asylum_decisions = asylum_decisions[asylum_decisions.coo != 'UKN']

asylum_decisions["dec_rejected"] = asylum_decisions['dec_total'] - asylum_decisions['dec_recognized']

asylum_decisions = asylum_decisions.drop(['coo_id', 'coo', 'coa_id', 'dec_other', 'dec_closed'], axis = 1)

asylum_decisions = asylum_decisions[asylum_decisions['dec_total'] > 0]

asylum_decisions['acceptance_rate'] = asylum_decisions['dec_recognized'] / asylum_decisions['dec_total'] 

insert_statements = []
for index, row in asylum_decisions.iterrows():
    insert_statement = f"INSERT INTO decisionStats (year, coo_name, coa_name, dec_recognized, dec_rejected, dec_total, acceptance_rate) VALUES ('{row['year']}', '{row['coo_name']}', '{row['coa_name']}', '{row['dec_recognized']}', '{row['dec_rejected']}', '{row['dec_total']}', '{row['acceptance_rate']}');"
    insert_statements.append(insert_statement)

# Print the generated SQL statements
for statement in insert_statements:
    with open ("countrystats3.sql", "a") as outfile:
        outfile.write(statement + '\n')



"""
#
asylum_decisions_dict = asylum_decisions.to_dict()
# 
# print(asylum_decisions.head())
print(asylum_decisions_dict)
# with open("countrydata3.json", "w") as outfile: 
   #  json.dump(asylum_decisions_dict, outfile)
"""