import logging
import streamlit as st

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="Migrant Home", page_icon="🏠")
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}")

col1, col2 = st.columns(2)

# Dashboard Information
with col1:
 st.image("https://i.imgur.com/5wysIa3.jpeg", use_column_width="auto")
 st.subheader("Profile:", divider="blue")
 st.write(":green[**Full Name**]: Hugo Ignacio Davilia")
 st.write(":green[**Age**]: 26 years old")
 st.write(":green[**Birthday**]: January 22nd, 1998")
 st.write(":green[**Current Occupation**]: IT Technician @ UnitedHealth Care")
 st.write(":green[**Username**]: hugo_davi")

# Dashboard Information with page links to other things the migrant can do
with col2:
  st.subheader("Navigation", divider="blue")
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
  st.write("")

  st.subheader("Appointment Stats", divider='blue')
  opinion = st.selectbox(
    "**How would you rate your last appointment?**",
    options=["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"],index=None)
  st.write("You selected:", opinion)

  rating = st.selectbox(
    "**How would you rate the services recommmended?**",
    options=["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"],index=None)
  st.write("You selected:", rating)