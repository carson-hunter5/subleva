import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title="Asylum Statistics", page_icon="📊")

import logging 
import requests
import pandas as pd
import streamlit as st

SideBarLinks()

country_list  = requests.get('http://api:4000/i/countrylist').json()

country_dict = pd.DataFrame(country_list)
year = st.number_input(label="Pick a Year",step=1)
country_of_origin  = st.selectbox(label="Select a Country of Origin", options = country_dict['country'])
country_of_asylum  = st.selectbox(label="Select a Country of Asylum", options = country_dict['country'])
num_decisions = st.number_input(label="Number of Decisions",step=1)
if st.button("Submit"):
    response = requests.get(f"""http://api:4000/i/testing/{year}/{country_of_origin}/{country_of_asylum}/{num_decisions}""")
    prediction = response.json()['result']
    prediction_percentage = round(prediction * 100,2)
    st.write(f"The predicted acceptance rate is {prediction_percentage}%.")


