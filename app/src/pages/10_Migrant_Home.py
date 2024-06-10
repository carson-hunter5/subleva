import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="Migrant Home", page_icon="🏠")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")

col1, col2 = st.columns(2)

# Dashboard Information
with col1:
 st.image("https://i.imgur.com/5wysIa3.jpeg")
 st.write("**Full Name**: Hugo Ignacio Davilia")
 st.write("**Age**: 23 years old")
 st.write("**Current Occupation**: IT Technician @ UnitedHealth Care")

# Dashboard Information with page links to other things the migrant can do
with col2:
  st.subheader("Navigation", divider="green")
  if st.button('Appointment Book', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/11_Appointments.py')

  if st.button('Schedule Appointment', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/14_Schedule_Appointment.py')

  if st.button('View Community Events', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/12_Community.py')

  if st.button('View Community Bulletin Board', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/13_Bulletin.py')

  st.write("")
  st.write("")

  st.subheader("Appointment Stats", divider='green')
  opinion = st.selectbox(
    "**How would you rate your last appointment?**",
    options=["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"])
  st.write("You selected:", opinion)
