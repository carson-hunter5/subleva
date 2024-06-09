import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="City Council Home", page_icon="🏠")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Manage Community Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')

if st.button('Manage Bulletin Board', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_City_Council_Bulletin.py')

if st.button('Manage Appointments', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')