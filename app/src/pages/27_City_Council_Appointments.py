import streamlit as st
import requests
import datetime
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

col1, col2 = st.columns(2)

with col1:
  st.subheader("Filter Appointments", divider='green')
  options = st.multiselect(
    "Select Appointment Topic to View",
    ["Training", "Marketing", "Accounting", "Services", "Sales", 
     "Engineering", "Legal", "Support", "Human Resources", 
     "Business Development","Product Management", "Reseearch and Development"],
    default=None)


with col2:
   st.subheader("Appointment Editors", divider='green')
   if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/28_New_Appointment.py')

   if st.button('Edit Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_Edit_Appointment.py')

   if st.button('Cancel Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/29_Cancel_Appointment.py')


st.write("")
st.write("")
