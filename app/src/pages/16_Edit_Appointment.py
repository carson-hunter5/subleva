import logging
import datetime
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Edit Appointment 

id_to_edit = st.number_input("Type the ID of the appointment you'd Like to Edit")

appointment_id_to_edit = id_to_edit
edit_volunteer_id = st.text_input("Edited Volunteer ID")
edit_appointment_date = st.date_input("Edited Appointment Date", value=datetime.date.today())
if st.button("Submit Edited Info"):
  if edit_appointment_date and edit_volunteer_id:
    edited_appointment_data = {
          "date" : str(edit_appointment_date),
          "volunteerID" : str(edit_volunteer_id),
      }
    requests.put("http://api:4000/m/migrant/appointment", json = edited_appointment_data)


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')