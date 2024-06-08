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

# Creating an Appointment
st.header("Create a New Event", divider='green')
if st.button('New Event', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_New_Community_Event.py')



col1, col2 = st.columns(2, gap= "large")

with col1:
# Edits an event
 st.subheader("Edit an Event", divider='green')

 id_to_edit = st.number_input("Enter Event ID",value=0, step=1, placeholder="Type a value...")

 event_id_to_edit = id_to_edit
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
           "eventID" : str(event_id_to_edit)
       }
     requests.put("http://api:4000/c/city_council/communityEvent", json = edited_event_data)

with col2:
# Cancels an event
 st.subheader("Cancel an Event", divider='green')

 id_to_cancel = st.number_input("Enter Event ID",value=0, step=1)

country_name  = st.selectbox(label="Select an Appointment ID to Cancel", options = data['name'])
st.write(data)
requests.delete(f"""http://api:4000/c/city_council/communityEvent/{id_to_cancel}""")

if st.button("Cancel Appointment"):
    requests.delete(f"""http://api:4000/c/city_council/communityEvent/{id_to_cancel}""")

##
#options = st.multiselect(
    #"Which events would you like to delete?",
    #event_options,
#)

#st.write("You selected:", options)
# id_to_cancel = st.number_input("Type the ID of the Event You'd Like to Cancel")
#requests.delete(f"http://api:4000/c/city_council/communityEvent/{id_to_cancel}")

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')