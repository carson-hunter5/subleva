import logging
import datetime
import requests
logger = logging.getLogger()
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
st.set_page_config (page_title="Appointment Manager", page_icon="📅")

SideBarLinks()

st.header("Edit Appointment", divider='green')


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

data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

logger.info(type(data))

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
  appointment_ids = [item['appointmentID'] for item in data if 'appointmentID' in item]

  if appointment_ids:
    id_to_edit = st.selectbox("Select the Appointment ID", options=appointment_ids)


volunteer_data = {}
volunteer_data = requests.get("http://api:4000/c/city_council/volunteers").json()

volunteer_dict = pd.DataFrame(volunteer_data)
edit_volunteer_id = st.selectbox("Edited Volunteer ID", options = volunteer_dict["id"])
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
    response = requests.put("http://api:4000/c/city_council/appointments", json=edited_appointment_data)
    if response.status_code == 200:
          st.session_state["message"] = ":green[Appointment Edited Successfully!]"
    else:
          st.session_state["message"] = ":red[Failed to Edit Appointment.]"

    if "message" in st.session_state:
          st.write(st.session_state["message"])
          del st.session_state["message"]

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')