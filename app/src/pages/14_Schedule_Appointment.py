import logging
import requests
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Booking Appointment", page_icon="📌")

SideBarLinks()

migrant_id = st.session_state["id"]

# Schedule a new appointment
st.subheader("**Schedule a New Appointment**", divider='green')

weekday = st.selectbox(label="Select an Appointment Day", options=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))

# initializing the list of data
appointment_ids = []
data = {}
appointment_to_book = None

# getting all the appointments for a certain migrant based on what day they want
response = requests.get(f'http://api:4000/m/migrant/show_appt/{weekday}')
logger.info(f'Response status code: {response.status_code}')
    
if response.status_code == 200:
    data = response.json()
    logger.info(f'Data is: {data}')
        
    for row in data:
        row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])
    appointment_ids = [row["appointmentID"] for row in data]
    logger.info(type(data))

    # editing the column names
    edited_data = st.data_editor(
        data,
        column_config={
                "appointmentID": "Appointment ID",
                "appDate": "Date",
                "COUNT(aa.attendeeID)": "Reserved Spots",
                "subject": "Topic",
                "weekday": "Day of the Week",
                "name": "Volunteer Name"
            },
        )
else:
        logger.error(f'Error getting appointment data. Status code: {response.status_code}')
        st.error("Failed to fetch appointment data.")

# if data:
appointment_ids = [row["appointmentID"] for row in data]
appointment_to_book = st.selectbox("Select an Appointment ID to Book:", options=appointment_ids)
logger.info(f'appointment_to_book = {appointment_to_book}')
headers = {'Content-Type': 'application/json'}

if st.button("Reserve Appointment"):
        post_data = {
            "appointmentID": appointment_to_book,
            "attendeeID": migrant_id   
        }

        #takes the inputed appointment and adds the data to the migrant to show up in their table of appointments
        response = requests.post("http://api:4000/m/make_appointment", json=post_data)
        if response.status_code == 200:
            st.session_state["message"] = ":green[Appointment Booked!]"
            st.balloons()
        else:
            st.session_state["message"] = ":red[Failed to book appointment.]"

        if "message" in st.session_state:
            st.write(st.session_state["message"])
            del st.session_state["message"]
     # else:
        # st.error("Please select or edit an appointment before booking.")

if st.button('Back', type='primary', use_container_width=True):
    st.switch_page('pages/11_Appointments.py')
