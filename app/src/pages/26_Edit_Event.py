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

st.header("Edit Community Event", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council').json()

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    event_ids = [item['eventID'] for item in data if 'eventID' in item]

    if event_ids:
        id_to_edit = st.selectbox("Select the Event ID", options=event_ids)


edit_event_name = st.text_input("New Event Name")
edit_duration = st.number_input("New Duration",value=0, step=1, placeholder="Type a value...")
edit_venue_capacity = st.number_input("New Venue Capcity",value=0, step=1, placeholder="Type a value...")
edit_event_date = st.date_input("New Event Date", value=datetime.date.today())


if st.button("Submit Event"):
 if edit_event_name and edit_event_date and edit_duration and edit_venue_capacity:
     edited_event_data = {
           "eventName" : str(edit_event_name),
           "date" : str(edit_event_date),
           "duration" : str(edit_duration),
           "venueCapacity" : str(edit_venue_capacity),
           "eventID" : str(id_to_edit)
       }
     requests.put("http://api:4000/c/city_council/communityEvent", json = edited_event_data)

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')