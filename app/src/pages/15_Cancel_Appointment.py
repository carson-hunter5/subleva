import logging
import datetime
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Appointment Deletion  

st.subheader("Cancel an Appointment", divider='green')

date_to_cancel = st.date_input("Type the Appointment Date", value=None)
requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{date_to_cancel}""")

if st.button("Cancel Appointment"):
  requests.delete(f"""http://api:4000/m/migrant/appointment_delete/{date_to_cancel}""")


if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Appointments.py')