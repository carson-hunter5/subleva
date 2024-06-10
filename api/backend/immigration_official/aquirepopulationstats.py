import pandas as pd 

# setting input file as constant
FILE = 'api/backend/immigration_official/country-capital-lat-long-population.csv'
#create df from file 
pop_df = pd.read_csv(FILE)


# make insert statements 
insert_statements = []
for index, row in pop_df.iterrows():
    insert_statement = f"INSERT INTO populationStats (Country,Capital City,Latitude,Longitude,Population,Capital Type) VALUES ('{row['Country']}', '{row['Capital City']}', '{row['Latitude']}', '{row['Longitude']}', '{row['Population']}', '{row['Capital Type']}');"
    insert_statements.append(insert_statement)

# Print the generated SQL statements
for statement in insert_statements:
    with open ("populationstats.sql", "a") as outfile:
        outfile.write(statement + '\n')