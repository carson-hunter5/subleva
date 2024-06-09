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

# appts_on_weekday = {} 
# data = requests.get('http://api:4000/m/migrant').json()
weekday = st.selectbox(label = "Select a Weekday to View", options = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")) 
if st.button("Pick Weekday"):
       response = requests.get(f'http://api:4000/m/migrant/show_appt/{weekday}').json()
       st.dataframe(response)




""""
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    weekdays_list = [item['weekday'] for item in data if 'weekday' in item]

st.subheader("**Schedule a New Appointment**", divider='green')

if weekdays_list:
    selected_day = st.selectbox("Select a Day", options=weekdays_list)

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        
        available_appointments = [item['appointmentID'] for item in data if 'appointmentID' in item]

        if available_appointments:
            selected_appointment = st.selectbox("Select an Appointment Slot", options=available_appointments)

            migrantID = st.session_state.get("id")
"""
if st.button("Submit"):
                if selected_appointment and migrantID:
                    post_data = {
                        "appointmentID": selected_appointment,
                        "migrantID": migrantID,
                        "day": selected_day
                    }

response = requests.post("http://api:4000/m/migrant/",json=post_data)


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')