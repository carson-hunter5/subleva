import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
import logging 
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="🙏")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.header("All Community Events", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council').json()

edited_data = st.data_editor(
    data,
    column_config={
        "name": "Event Name",
        "date": "Date",
        "duration": "Duration in Hours",
        "eventID" : "Event ID",
        "venueCapacity":"Venue Capacity"
    },
)
col1, col2, col3 = st.columns(3, gap = "medium")


# Creating an Event Page
with col1:
 if st.button('New Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_New_Community_Event.py')


# Editing an Event Page
with col2:
 if st.button('Edit Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/26_Edit_Event.py')

# Canceling an Event Page
with col3:
 if st.button('Cancel Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Cancel_Event.py')
