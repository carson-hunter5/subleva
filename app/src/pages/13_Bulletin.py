import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo

st.set_page_config (page_title="Bulletin", page_icon="🙏")

add_logo("assets/logo.png", height=400)

st.write("See Recent Bulletin Posts")

data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/posts').json()
except:
  st.write("**Important**: Could not connect to database")

st.dataframe(data)