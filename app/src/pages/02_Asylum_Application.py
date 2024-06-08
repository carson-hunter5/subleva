import logging
logger = logging.getLogger()

import json
import pandas as pd
import requests
import streamlit as st
import numpy as np
from modules.nav import SideBarLinks
SideBarLinks()

st.write("**Predict Asylum Applications**")

country_list  = requests.get('http://api:4000/i/countrylist').json()

country_dict = pd.DataFrame(country_list)
year = st.number_input(label="Pick a Year",step=1)
country_name  = st.selectbox(label="Select a Country of Asylum", options = country_dict['country'])
gender = st.selectbox("Select a Gender",("Male", "Female"))
age_options = ["0-4", "5-11", "12-17", "18-59", "60+"]
age_group = st.radio("Select an Age Group 👇",age_options)
age_index = age_options.index(age_group)
age_array = np.zeros(5, dtype=int)
age_array[age_index] = 1
if st.button("Submit"):
    response = requests.get(f"""http://api:4000/i/prediction/{year}/{country_name}/{gender}/{age_array}""")
    prediction = response.json()['result']
    st.write(f"The predicted number of applications to {country_name} is {prediction}!")


