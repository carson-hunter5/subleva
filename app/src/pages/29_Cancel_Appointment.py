import streamlit as st
import requests
import logging
from streamlit_extras.app_logo import add_logo 
from modules.nav import SideBarLinks
logger = logging.getLogger(__name__)

st.set_page_config (page_title="Appointment Manager", page_icon="📅")

add_logo("assets/logo.png", height=400)

SideBarLinks()

#Cancel appointment
st.header("Cancel Appointment", divider='green')

#gets all the appointments
data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

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

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    appointment_ids = [item['appointmentID'] for item in data if 'appointmentID' in item]

    if appointment_ids:
        id_to_delete = st.selectbox("Select the Appointment ID",options = appointment_ids)

#deletes the appointment of the id that is selected 
if st.button('Delete Appointment'):
    if id_to_delete:
     edited_event_data = {
        "appointmentID" : str(id_to_delete)
    }
     
     #route to delete an appointment
    response = requests.delete(f'http://api:4000/c/city_council/appointments/{id_to_delete}')
    data = [item for item in data if item['appointmentID'] != id_to_delete]
    if response.status_code == 200:
                st.session_state["message"] = ":green[Appointment Deleted Sucessfully!]"
    else:
                st.session_state["message"] = ":red[Failed to Delete Appointment.]"

    if "message" in st.session_state:
         st.write(st.session_state["message"])
    del st.session_state["message"]

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')