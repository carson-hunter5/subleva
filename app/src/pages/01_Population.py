import logging
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title="Population Data", page_icon="🗺️")

SideBarLinks()

#Get the country data
st.write("Displaying all country populations")

try:
  data = requests.get('http://api:4000/i/get_population').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)