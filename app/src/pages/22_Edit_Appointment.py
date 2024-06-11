import logging
import datetime
import requests
import pandas as pd
import streamlit as st

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment Manager", page_icon="📅")
SideBarLinks()

st.header("Edit Appointment", divider='green')

#gets the data
data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])
logger.info(type(data))

#edits the data format and layout
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
    column_order=("appointmentID", "appDate", "weekday", "subject", "volunteerID")
)

#gets all the appointments
data = {} 
data = requests.get('http://api:4000/c/city_council/appointments').json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])

logger.info(type(data))

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
  appointment_ids = [item['appointmentID'] for item in data if 'appointmentID' in item]
# dropdown that includes the list of appointment ids 
  if appointment_ids:
    id_to_edit = st.selectbox("Select the Appointment ID", options=appointment_ids)

volunteer_data = {}
volunteer_data = requests.get("http://api:4000/c/city_council/volunteers").json()
volunteer_dict = pd.DataFrame(volunteer_data)

#allows the user to change any appointment based on the id that is selected
edit_appointment_appDate = st.date_input("Edited Appointment Date", value=datetime.date.today())
edit_weekday = st.selectbox("Weekday", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"),index=None)
edit_subject = st.selectbox("Appointment Topic",("Training", "Marketing", "Accounting", "Services", "Sales", 
     "Engineering", "Legal", "Support", "Human Resources", 
     "Business Development","Product Management", "Reseearch and Development"),index=None)
edit_volunteer_id = st.selectbox("Edited Volunteer ID", options = volunteer_dict["id"],index=None)

#updates the selected appointment to the new inputs from the user
if st.button("Change Appointment Info", type="primary", use_container_width=True):
  if edit_volunteer_id and edit_appointment_appDate and edit_subject and edit_weekday:
    edited_appointment_data = {
          "volunteerID" : str(edit_volunteer_id),
          "appDate" : str(edit_appointment_appDate),
          "appointmentID": str(id_to_edit),
          "subject" : str(edit_subject),
          "weekday" : str(edit_weekday)
      }
    
    #call to update the appointment table to the new information inputted by the user
    response = requests.put("http://api:4000/c/city_council/appointments", json=edited_appointment_data)
    if response.status_code == 200:
          st.session_state["message"] = ":green[Appointment Edited Successfully!]"
    else:
          st.session_state["message"] = ":red[Failed to Edit Appointment.]"

    if "message" in st.session_state:
          st.write(st.session_state["message"])
          del st.session_state["message"]

if st.button('Back', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')