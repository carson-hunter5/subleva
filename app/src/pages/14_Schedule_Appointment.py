import logging
import requests
import pandas as pd
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Booking Appointment", page_icon="📌")

SideBarLinks()

# Schedule a new appointment
st.subheader("**Schedule a New Appointment**", divider='green')

edited_data = None  # Define edited_data outside the block
appointment_to_book = None  # Define appointment_to_book outside the block

weekday = st.selectbox(label="Select an Appointment Day", options=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
if st.button("Choose Appointment Day"):
    response = requests.get(f'http://api:4000/m/migrant/show_appt/{weekday}')
    logger.info(f'Response status code: {response.status_code}')
    
    if response.status_code == 200:
        data = response.json()  
        logger.info(f'Data is: {data}')
        
        for row in data:
            row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

        logger.info(type(data))
        edited_data = st.data_editor(
            data,
            column_config={
                "appDate": "Date",
                "COUNT(aa.attendeeID)": "Reserved Spots",
                "appointmentID": "Appointment ID",
                "subject": "Topic",
                "weekday": "Day of the Week",
                "name": "Volunteer Name"
            },
        )
    else:
        logger.error(f'Error getting appointment data. Status code: {response.status_code}')

if edited_data: 
    appointment_ids = [row["appointmentID"] for row in data]
    appointment_to_book = st.selectbox("Select an Appointment ID to Book:", options=appointment_ids)

# Use edited_data variable outside the block
#if isinstance(edited_data, pd.DataFrame) and not edited_data.empty:
    #appointment_ids = edited_data['appointmentID'].tolist()
    #appointment_to_book = st.selectbox("Select an Appointment ID to Schedule", options=appointment_ids)

headers = {'Content-Type': 'application/json'}

# 
volunteerID = ()
apptDate = ()
subject = ()
weekday = ()

if st.button('Book Appointment'):
    if volunteerID and apptDate  and subject and weekday:
        json_data = edited_data.to_json(orient='records')
        post_data = {
            "volunteerID" : volunteerID,
            "apptDate" : str(apptDate),
            #"appointmentID" : appointmentID,
            "subject" : subject, 
            "weekday": weekday
        }
         
        response = requests.post(f"http://api:4000/m/make_appointment", json= json_data, headers=headers)
        if response.status_code == 200:
                st.session_state["message"] = ":green[Appointment Booked!]"
                st.balloons()
        else:
                st.session_state["message"] = ":red[Failed to book appointment.]"

        if "message" in st.session_state:
                st.write(st.session_state["message"])
                del st.session_state["message"]
    else:
        st.error("Please select or edit an appointment before booking.")

if st.button('Back',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/11_Appointments.py')