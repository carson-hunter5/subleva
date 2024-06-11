import streamlit as st
import requests
import datetime
import logging

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="💻")
SideBarLinks()

st.header("Edit Community Event", divider='green')

#gets all the community events
data = {} 
data = requests.get('http://api:4000/c/city_council').json()
logger.info(f'Data is: {data}')
for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])
logger.info(type(data))

#edit the data format and layout
edited_data = st.data_editor(
    data,
    column_config={
        "eventDate": "Date",
        "eventID": "EventID",
        "name": "Name",
        "duration": st.column_config.NumberColumn(
            "Duration",
             format="%d Hours",
         ),
        "venueCapacity" : "Venue Capacity"
    },
    use_container_width= True,
    column_order=("eventID", "name", "eventDate", "duration", "venueCapacity")
)

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    event_ids = [item['eventID'] for item in data if 'eventID' in item]
    # gets the event id from the list of ids from the dropdown
    if event_ids:
        id_to_edit = st.selectbox("Select the Event ID", options=event_ids,index=None)

# inputs for the user to change any of the event properties
edit_event_name = st.text_input("New Event Name", max_chars=50)
edit_event_date = st.date_input("New Event Date", value=datetime.date.today())
edit_duration = st.number_input("New Duration",value=0, step=1, min_value= 0,max_value=10,placeholder="Type a value...")
edit_venue_capacity = st.number_input("New Venue Capcity",value=0, step=1,min_value= 0, placeholder="Type a value...")

# updates the old information to the inputted values from the user
if st.button("Change Event Info", type="primary", use_container_width=True):
 if edit_event_name and edit_event_date and edit_duration and edit_venue_capacity:
     edited_event_data = {
           "eventName" : str(edit_event_name),
           "eventDate" : str(edit_event_date),
           "duration" : str(edit_duration),
           "venueCapacity" : str(edit_venue_capacity),
           "eventID" : str(id_to_edit)
       }
     
     #call that adds the new event data into the community table again 
     response = requests.put("http://api:4000/c/city_council/communityEvent", json=edited_event_data)
     try:
         response_json = response.json()
         error_message = response_json.get('error', 'Unknown error')
     except ValueError:
         error_message = 'Invalid response from server'

     if response.status_code == 200:
         st.session_state["message"] = f":green[Event Edited Successfully!]"
     else:
         st.session_state["message"] = f":red[Failed to Edit Event: {error_message}]"

     if "message" in st.session_state:
         st.write(st.session_state["message"])
         del st.session_state["message"]

if st.button('Back', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')