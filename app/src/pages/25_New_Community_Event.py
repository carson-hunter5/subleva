import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="💻")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.header("New Community Event", divider='green')

# Creates an Event
event_name = st.text_input("Event Name")
eventDate = st.date_input("Event Date", value=datetime.date.today())
duration = st.number_input("Duration",value=0, step=1, placeholder="Type a value...")
venue_capacity = st.number_input("Venue Capcity",value=0, step=1, placeholder="Type a value...")

#submits the event info
if st.button("Submit"):
    if event_name and eventDate and duration and venue_capacity:
        post_data = {
            "eventName" : event_name,
            "eventDate" : str(eventDate),
            "duration" : duration,
            "venueCapacity" : venue_capacity
        }
        #call that adds the event to the list of events
        response = requests.post("http://api:4000/c/council_add_event", json=post_data)
        if response.status_code == 200:
                st.session_state["message"] = ":green[Event Created Sucessfully!]"
                st.balloons()
        else:
                st.session_state["message"] = ":red[Failed to Create Event.]"

        if "message" in st.session_state:
         st.write(st.session_state["message"])
    del st.session_state["message"]

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')