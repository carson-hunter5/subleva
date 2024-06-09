import logging
import datetime
import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Appointment Deletion  

st.subheader("Cancel an Appointment", divider='green')

attendeeID = st.session_state["id"]
data = requests.get(f"""http://api:4000/m/migrant/appointments_cancel/{attendeeID}""").json()
logger.info(f'Data is: {data}')
for row in data:
  row["Date"] = ' '.join(row["Date"].split(' ')[:4])

# ' '.join(test_string.split(' ')[:4])
logger.info(type(data))
edited_data = st.data_editor(
    data,
    column_config={
        "appDate": "Date",
        "appointmentID": "Appointment ID",
        "name": "Volunteer Name",
    },
)

col1, col2, col3 = st.columns(3, gap = "medium")

json_data = data[0]
logger.info(json_data)
logger.info(type(json_data))
appointment_to_delete = st.selectbox("Select an Appointment ID to  Delete:", options = [json_data["appointmentID"]])

if st.button("Cancel Appointment"):
  requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{attendeeID}/{appointment_to_delete}""")


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')