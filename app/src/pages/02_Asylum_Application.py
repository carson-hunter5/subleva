import logging
import requests
import pandas as pd 
import streamlit as st
import numpy as np

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config (page_title="Asylum Applications", page_icon="🗂️")
SideBarLinks()

# Predicting the Asylum Applications
st.header("**Predict Asylum Applications**", divider='green')

country_list  = requests.get('http://api:4000/i/countrylist').json()

# Input values form the user
country_dict = pd.DataFrame(country_list)
year = st.number_input(label="Pick a Year",step=1,min_value=1900, max_value=2150)
country_name  = st.selectbox(label="Select a Country of Asylum", options = country_dict['country'])

gender = st.selectbox("Select a Gender",("Male", "Female"))

age_options = ["0-4", "5-11", "12-17", "18-59", "60+"]
age_group = st.radio("Select an Age Group 👇", age_options,index=0, horizontal=True,)
age_index = age_options.index(age_group)
age_array = np.zeros(5, dtype=int)
age_array[age_index] = 1

# Button to submit and use the model01 to predict the number of applications
if st.button("Submit",type="primary", use_container_width=True):
    response = requests.get(f"""http://api:4000/i/prediction/{year}/{country_name}/{gender}/{age_array}""")
    prediction = response.json()['result']
    st.write("")
    st.write(f"The Predicted Number of Applications to {country_name} is {round(prediction,3)}.")