import streamlit as st
import requests
import datetime
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="API Test", page_icon="🙏")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.write("Displaying all community events")

"""
Simply retrieving data from a REST api running in a separate Docker Container.

If the container isn't running, this will be very unhappy.  But the Streamlit app 
should not totally die. 
"""
data = {} 
try:
  data = requests.get('http://api:4000/c/city_council').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

st.write("**Create an Event:**")
event_name = st.text_input("Event Name")
event_id = st.number_input("Event ID")
date = st.date_input("Event Date", value=datetime.date.today())
duration = st.number_input("Duration")
venue_capacity = st.number_input("Venue Capcity")

if st.button("Submit"):
    if event_name and date and duration and venue_capacity:
        post_data = {
            "eventName" : event_name,
            "eventID" : event_id,
            "date" : str(date),
            "duration" : duration,
            "venueCapacity" : venue_capacity

        }
        response = requests.post("http://api:4000/c/council_add_event", json=post_data)

st.write("Cancel an Event:")


id_to_cancel = st.number_input("Type the ID of the Event You'd Like to Cancel")
requests.delete(f"""http://api:4000/c/city_council/communityEvent/{id_to_cancel}""")

st.write("Edit an Event:")

id_to_edit = st.number_input("Type the ID of the Event You'd Like to Edit")

event_id_to_edit = id_to_edit
edit_event_name = st.text_input("Edited Event Name")
edit_duration = st.number_input("Edited Duration")
edit_venue_capacity = st.number_input("Edited Venue Capcity")
edit_event_date = st.date_input("Edited Event Date", value=datetime.date.today())
if st.button("Submit Edited Info"):
  if edit_event_name and edit_event_date and edit_duration and edit_venue_capacity:
    edited_event_data = {
          "eventName" : str(edit_event_name),
          "date" : str(edit_event_date),
          "duration" : str(edit_duration),
          "venueCapacity" : str(edit_venue_capacity),
          "eventID" : str(event_id_to_edit)
      }
    requests.put("http://api:4000/c/city_council/communityEvent", json = edited_event_data)
 
if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')