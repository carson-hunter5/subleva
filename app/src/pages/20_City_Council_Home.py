import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Schedule Appointments', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Appointments_Confirmation.py')

if st.button('View Community Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Community_Creation.py')

if st.button('View Community Bulletin Board', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Bulletin.py')