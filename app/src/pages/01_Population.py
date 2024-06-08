import logging
import datetime
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
SideBarLinks()

#Get the 
st.write("Displaying all country populations")

data = {} 
try:
  data = requests.get('http://api:4000/i/immigration_officialpopulation').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)