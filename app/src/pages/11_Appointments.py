import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment", page_icon="🙏")
SideBarLinks()
add_logo("assets/logo.png", height=400)

# set the header of the page
st.header('Appointments')
st.write("Hello! Here is a list of all your appointments scheduled to meet with a representative on behalf of Tanya Bracker.")

attendeeID = st.session_state["id"]
data = {} 
data = requests.get(f"""http://api:4000/m/migrant/appointments/{attendeeID}""").json()

edited_data = st.data_editor(
    data,
    column_config={
        "date": "Date",
        "appointmentID": "Appointment ID",
        "volunteerID": "Volunteer ID",
        "subject": "Topic",
        "weekday": "Day of the Week"
    },
)

col1, col2, col3 = st.columns(3, gap = "medium")

# Creating an Appointment

with col1:
 if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Schedule_Appointment.py')

# Editing an Appointment

with col2:
 if st.button('Edit Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_Edit_Appointment.py')

# Appointment Deletion 

with col3: 
 if st.button('Delete Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Cancel_Appointment.py')
