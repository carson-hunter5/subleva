import logging
import datetime
import requests
logger = logging.getLogger()
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment Manager", page_icon="📅")

SideBarLinks()

st.header("Edit Appointment", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
  appointment_ids = [item['appointmentID'] for item in data if 'appointmentID' in item]

  if appointment_ids:
    id_to_edit = st.selectbox("Select the Appointment ID", options=appointment_ids)

edit_volunteer_id = st.number_input("Edited Volunteer ID",value=0, step=1)
edit_appointment_appDate = st.date_input("Edited Appointment Date", value=datetime.date.today())
edit_subject = st.selectbox("Appointment Topic",("Training", "Marketing", "Accounting", "Services", "Sales", 
     "Engineering", "Legal", "Support", "Human Resources", 
     "Business Development","Product Management", "Reseearch and Development"))
edit_weekday = st.selectbox("Weekday", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))

if st.button("Change Appointment Info"):
  if edit_volunteer_id and edit_appointment_appDate and edit_subject and edit_weekday:
    edited_appointment_data = {
          "volunteerID" : str(edit_volunteer_id),
          "appDate" : str(edit_appointment_appDate),
          "appointmentID": str(id_to_edit),
          "subject" : str(edit_subject),
          "weekday" : str(edit_weekday)
      }
    requests.put("http://api:4000/c/city_council/appointments", json = edited_appointment_data)

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')