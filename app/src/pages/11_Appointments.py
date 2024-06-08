import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="API Test", page_icon="🙏")
SideBarLinks()
add_logo("assets/logo.png", height=400)

# set the header of the page
st.header('Appointments')
st.write("Hello! Here is a list of all your appointments scheduled to meet with a representative on behalf of Tanya Bracker.")

id = st.session_state["id"]

data = {} 
try:
  data = requests.get(f"""http://api:4000/m/migrant/appointments/{id}""").json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

# Creating an Appointment

if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Schedule_Appointment.py')

# Appointment Edit

st.write("Edit an Appointmemt:")

id_to_edit = st.number_input("Type the ID of the appointment You'd Like to Edit")

appointment_id_to_edit = id_to_edit
edit_volunteer_id = st.text_input("Edited Volunteer ID")
edit_appointment_date = st.date_input("Edited Appointment Date", value=datetime.date.today())
if st.button("Submit Edited Info"):
  if edit_appointment_date and edit_volunteer_id:
    edited_appointment_data = {
          "date" : str(edit_appointment_date),
          "volunteerID" : str(edit_volunteer_id),
      }
    requests.put("http://api:4000/m/migrant/appointment", json = edited_appointment_data)

# Appointment Deletion  

st.write("Cancel an Appointment:")

date_to_cancel = st.date_input("Type the date of the appointment You'd Like to Cancel")
requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{date_to_cancel}""")

if st.button("Cancel Appointment"):
  requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{date_to_cancel}""")


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')
