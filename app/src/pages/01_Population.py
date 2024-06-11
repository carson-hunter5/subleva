import logging
import requests
import streamlit as st

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config (page_title="Population Data", page_icon="🗺️")
SideBarLinks()

st.header("**Population Data**", divider='green')

# Getting the data from the population
data = requests.get('http://api:4000/i/get_population').json()

#edits the data layout and format
edited_data = st.data_editor(
    data,
    use_container_width= True,
)

st.header("**Global Population Statsitics**", divider='green')

# Columns displaying some historical data (not from the data just to serve as an aesthetic purpose)
col1, col2 = st.columns(2)
with col1:
 st.write("**Population Factor**")
 col1.metric("Birth Rates", "18.1 Births", "-0.94%")
 col1.metric("Death Rates", "7.75 Deaths", "5.8%")
 col1.metric("Year to Date Population", "8.1 Billion", "0.8%")

with col2: 
  st.write("**Country Population**")
  col2.metric("India", "1.428 Billion", "0.81%")
  col2.metric("China", "1.425 Billion", "-0.02%")
  col2.metric("United States of America", "339 Million", "0.50%")