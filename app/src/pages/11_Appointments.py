import streamlit as st
import requests
import logging
import datetime
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config (page_title="Appointment", page_icon="🙏")
SideBarLinks()
add_logo("assets/logo.png", height=400)

# set the header of the page
st.header('Appointments', divider='green')
st.write("Hello! Here is a list of all your appointments scheduled to meet with a representative on behalf of Tanya Bracker.")

attendeeID = st.session_state["id"]
data = {} 
data = requests.get(f"""http://api:4000/m/migrant/appointments/{attendeeID}""").json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

logger.info(type(data))
edited_data = st.data_editor(
    data,
    column_config={
        "appDate": "Date",
        "COUNT(aa.attendeeID)" : "Reserved Spots",
        "appointmentID": "Appointment ID",
        "subject": "Topic",
        "weekday": "Day of the Week",
        "name": "Volunteer Name"
    },
)

col1, col2 = st.columns(2, gap = "medium")

# Creating an Appointment

with col1:
 if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Schedule_Appointment.py')

# Appointment Deletion 

with col2: 
 if st.button('Delete Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Cancel_Appointment.py')
