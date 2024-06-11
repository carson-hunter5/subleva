import streamlit as st
import requests
import logging 

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment Manager", page_icon="📅")
SideBarLinks()

st.header("All Appointments", divider='green')

#gets all the appointments 
data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])
logger.info(type(data))

#edits the data layout and format
edited_data = st.data_editor(
    data,
    column_config={
        "volunteerID": "Volunteer ID",
        "appDate": "Date",
        "appointmentID": "Appointment ID",
        "subject" : "Appointment Topic",
        "weekday" : "Day",
    },
    use_container_width= True,
    column_order=("appointmentID","appDate","weekday", "subject", "volunteerID")
)

# makes a new appointment
col1, col2, col3 = st.columns(3)

# button to makes a new appointment
with col1:
   if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/28_New_Appointment.py')

# button to edits a appointment
with col2:
   if st.button('Edit Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_Edit_Appointment.py')

# button to deletes a appointment
with col3:
   if st.button('Cancel Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/29_Cancel_Appointment.py')