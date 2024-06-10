import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

st.set_page_config (page_title= "Application Predictions", page_icon="📊")

st.header("**Asylum Acceptances Applications**", divider='green')

SideBarLinks()

country_list  = requests.get('http://api:4000/i/countrylist').json()

country_dict = pd.DataFrame(country_list)

c_list = list(country_dict["country"])
logging.info(type(c_list))
year = st.number_input(label="Pick a Year",step=1, min_value=1900, max_value=2150)
country_of_origin  = st.selectbox(label="Select a Country of Origin", options = c_list)
coo_index = c_list.index(country_of_origin)
c_list.pop(coo_index)
country_of_asylum  = st.selectbox(label="Select a Country of Asylum", options = c_list)
num_decisions = st.number_input(label="Number of Decisions",step=1)
if st.button("Submit"):
    response = requests.get(f"""http://api:4000/i/testing/{year}/{country_of_origin}/{country_of_asylum}/{num_decisions}""")
    prediction = response.json()['result']
    prediction_percentage = round(prediction * 100,2)
    st.write(f"The predicted acceptance rate is {prediction_percentage}%.")
