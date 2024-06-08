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

# add columns to the volunteer table for each day of the week
# randomly assign volunteers to days
# when a migrant wants to make an appt for a particular day, randomly assign them 
#      to one of the volunteers on that day. 

# assigns random volunteers based on the volunteers availability to the appointment
# the booking appointment will feature the date and from the date they could select

st.subheader("**Schedule a New Appointment**", divider='green')
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
  st.switch_page('pages/11_Appointments.py')