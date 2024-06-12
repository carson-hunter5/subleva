import streamlit as st
import requests
import requests
import logging

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="💻")
SideBarLinks()

st.header("Cancel Event", divider='green')

# gets all the data
data = {} 
data = requests.get('http://api:4000/c/city_council').json()
logger.info(f'Data is: {data}')
for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])

logger.info(type(data))

#edits the data layout and format
edited_data = st.data_editor(
    data,
    column_config={
        "eventDate": "Date",
        "eventID": "Event ID",
        "name": "Name",
        "duration": st.column_config.NumberColumn(
            "Duration",
             format="%d Hours",
         ),
        "venueCapacity": "Venue Capcity"
    },
    use_container_width= True,
    column_order=("eventID", "name", "eventDate", "duration", "venueCapacity")
)

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    event_ids = [item['eventID'] for item in data if 'eventID' in item]

#dropdown that includes the list of ids of the events
    if event_ids:
        id_to_delete = st.selectbox("Select the Event ID", options=event_ids, index=None)

# deletes the event based on the event id
if st.button('Delete Event', type="primary", use_container_width=True):
    if id_to_delete:
     edited_event_data = {
        "eventID" : str(id_to_delete)
    }
     #route that deletes the event based on the event id selected
    response = requests.delete(f'http://api:4000/c/city_council/communityEvent/{id_to_delete}')
    data = [item for item in data if item['eventID'] != id_to_delete] 
    if response.status_code == 200:
                st.session_state["message"] = ":green[Event Deleted]"
    else:
                st.session_state["message"] = ":red[Failed to Delete Event.]"

    if "message" in st.session_state:
         st.write(st.session_state["message"])
    del st.session_state["message"]

if st.button('Back', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')