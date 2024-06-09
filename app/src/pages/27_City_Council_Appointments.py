import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
import logging 
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.header("All Appointments", divider='green')

data = {} 
try:
  data = requests.get('http://api:4000/c/city_council/appointments').json()
except:
  st.write("**Important**: Could not connect to database")

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
   if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/28_New_Appointment.py')


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')
