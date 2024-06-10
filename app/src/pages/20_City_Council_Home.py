import logging
import requests
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="City Council Home", page_icon="🏠")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")

col1, col2 = st.columns(2)

with col1:
 st.subheader("Navigation", divider="green")
 if st.button('Manage Community Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')

 if st.button('Manage Bulletin Board', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_City_Council_Bulletin.py')

 if st.button('Manage Appointments', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')

 st.subheader("Upcoming Events", divider="green")
 data = {} 
 data = requests.get('http://api:4000/c/city_council/database').json()
 logger.info(f'Data is: {data}')
 for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])

 logger.info(type(data))
 edited_data = st.data_editor(
    data,
    column_config={
        "name": "Event Name",
        "eventDate": "Date",
    },
)

with col2:
 st.image("https://i.imgur.com/TbrU8c8.jpeg")

 st.subheader("To-Do", divider="green")
 task1 = st.checkbox("Check Post Analytics")
 task2 = st.checkbox("Consult Volunteers from this week's appointments")
 task3 = st.checkbox("Plan the Annual Town Hall")
 task4 = st.checkbox("University Tour for Local Students")