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
try:
  data = requests.get('http://api:4000/c/city_council').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

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


# Creating an Event Page
st.subheader("Create a New Event", divider='green')
if st.button('New Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_New_Community_Event.py')


# Editing an Event Page
st.subheader("Edit an Event", divider='green')
if st.button('Edit Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/26_Edit_Event.py')

# Canceling an Event Page
st.subheader("Cancel an Event", divider='green')
if st.button('Cancel Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Cancel_Event.py')

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')