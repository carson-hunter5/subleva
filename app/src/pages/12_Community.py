import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo

st.set_page_config (page_title="Community Events", page_icon="🙏")

add_logo("assets/logo.png", height=400)

st.write("Displaying all community events for your local area")

data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/events').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')
