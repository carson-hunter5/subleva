import logging
import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title=" Cancel Appointment", page_icon="📌")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Appointment Deletion  

st.subheader("Cancel an Appointment", divider='green')

attendeeID = st.session_state["id"]

#gets all the appointments from a certain migrant based on their id from the table of appointmnet attendees 
data = {} 
data = requests.get(f"""http://api:4000/m/migrant/appointments_cancel/{attendeeID}""").json()
logger.info(f'Data is: {data}')
for row in data:
  row["Date"] = ' '.join(row["Date"].split(' ')[:4])

logger.info(type(data))

#edits the column name
edited_data = st.data_editor(
    data,
    column_config={
        "appDate": "Date",
        "appointmentID": "Appointment ID",
        "volunteerID": "Volunteer ID",
        "subject" : "Topic",
        "weekday" : "Weekday"
    },
)

json_data = data[0]
logger.info(json_data)
logger.info(type(json_data))

if data:
    appointment_ids = [row["appointmentID"] for row in data]
    appointment_to_delete = st.selectbox("Select an Appointment ID to Delete:", options=appointment_ids)

#cancels the appointment by  removes the appointment id from the attendees' table 
if st.button("Cancel Appointment"):
      response = requests.delete(f"http://api:4000/m/migrant/appointment_delete/{attendeeID}/{appointment_to_delete}")
      if response.status_code == 200:
                st.session_state["message"] = ":green[Appointment Cancelled]"
      else:
                st.session_state["message"] = ":red[Failed to Cancel.]"

      if "message" in st.session_state:
         st.write(st.session_state["message"])
      del st.session_state["message"]


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')