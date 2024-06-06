import logging
import datetime
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Create a new appointment

st.write("**Schedule a New Appointment:**")
volunteerID = st.text_input("volunteerID")
date = st.date_input("Event Date", value=datetime.date.today())
appointmentID = st.text_input("appointmentID")
migrantID = st.session_state["id"]

if st.button("Submit"):
    if volunteerID and date and appointmentID and migrantID:
        post_data = {
            "volunteerID" : volunteerID,
            "appointmentID" : appointmentID,
            "date" : date,
            "migrantID" : migrantID
        }
        response = requests.post("http://api:4000/m/migrant/",json=post_data)


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')