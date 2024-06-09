import logging
import datetime
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

migrant_id = st.session_state["id"]

# Schedule a new appointment

st.subheader("**Schedule a New Appointment**", divider='green')

weekday = st.selectbox(label = "Select a Weekday to View", options = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")) 
if st.button("Pick Weekday"):
       response = requests.get(f'http://api:4000/m/migrant/show_appt/{weekday}').json()
       logger.info(f'Data is: {response}')
       for row in response:
           row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

       logger.info(type(response))
       edited_data = st.data_editor(
       response,

    column_config={
        "appDate": "Date",
        "COUNT(aa.attendeeID)":"Spots Reserved",
        "appointmentID": "Appointment ID",
        "name": "Volunteer Name",
        "subject": "Topic",
        "weekday": "Day of the Week"
    },
)

appt_id = st.number_input("Input Appointment to Reserve", step= 1, value=0)
if st.button("Reserve Appointment"):
       post_data = {
           "appointmentID" : appt_id,
           "attendeeID" : migrant_id   
       }
       response = requests.post("http://api:4000/m/make_appointment",json=post_data)

""""
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    weekdays_list = [item['weekday'] for item in data if 'weekday' in item]


if weekdays_list:
    selected_day = st.selectbox("Select a Day", options=weekdays_list)

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        
        available_appointments = [item['appointmentID'] for item in data if 'appointmentID' in item]

        if available_appointments:
            selected_appointment = st.selectbox("Select an Appointment Slot", options=available_appointments)

            migrantID = st.session_state.get("id")
"""
"""
if st.button("Submit"):
                if selected_appointment and migrantID:
                    post_data = {
                        "appointmentID": selected_appointment,
                        "migrantID": migrantID,
                        "day": selected_day
                    }

response = requests.post("http://api:4000/m/migrant/",json=post_data)
"""

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')