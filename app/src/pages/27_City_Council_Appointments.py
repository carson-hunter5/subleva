import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
import logging 
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config (page_title="Appointment Manager", page_icon="📅")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.header("All Appointments", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

logger.info(type(data))
edited_data = st.data_editor(
    data,
    column_config={
        "volunteerID": "Volunteer ID",
        "appDate": "Date",
        "appointmentID": "Appointment ID",
        "subject" : "Appointment Topic",
        "weekday" : "Day of the Week",
    },
)

col1, col2, col3 = st.columns(3)

with col1:
   if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/28_New_Appointment.py')


with col2:
   if st.button('Edit Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_Edit_Appointment.py')


with col3:
   if st.button('Cancel Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/29_Cancel_Appointment.py')