import streamlit as st
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

# Appointment Deletion / Edit 

st.write("Cancel/Edit an Appointment:")

id_to_edit = st.number_input("Type the ID of the Appointment You'd Like to Cancel or Edit")

appointment_to_edit = {}
appointment_to_edit = requests.get(f"""http://api:4000/m/migrant/show_appt/{id_to_edit}""")
st.dataframe(appointment_to_edit)

if st.button("Cancel Appointment:"):
  requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{id_to_edit}""")


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')
