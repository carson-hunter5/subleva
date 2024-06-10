import logging
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title="Population Data", page_icon="🗺️")

SideBarLinks()

st.subheader("**Population Data**", divider='green')

#Get the country data
st.write("Current Migrant Population")

try:
  data = requests.get('http://api:4000/i/get_population').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

st.subheader("**Global Population Statsitics**", divider='green')

col1, col2 = st.columns(2)
col1.metric("Birth Rates", "18.1 Births", "-0.94%")
col1.metric("Death Rates", "7.75 Deaths", "5.8%")
col1.metric("Year to Date Population", "8.1 Billion", "0.8%")

with col2: 
  st.write("India")
  st.write("China")
  st.write("United States of America")
  st.write("India")
  st.write("India")