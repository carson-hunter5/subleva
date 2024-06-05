

import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo



st.set_page_config (page_title="API Test", page_icon="🙏")

add_logo("assets/logo.png", height=400)

# set the header of the page
st.header('All Community Events')
st.write("Displaying all community events ever created by all city council")


data = {} 
try:
  data = requests.get('http://api:4000/c/city_council').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)