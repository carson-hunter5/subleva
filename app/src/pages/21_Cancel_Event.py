import streamlit as st
import requests
import requests
import logging
from streamlit_extras.app_logo import add_logo
logger = logging.getLogger(__name__) 
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="💻")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.header("Cancel Event", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council').json()
logger.info(f'Data is: {data}')
for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])

logger.info(type(data))
edited_data = st.data_editor(
    data,
    column_config={
        "eventDate": "Date",
        "eventID": "Event ID",
        "name": "Name",
        "duration" : "Duration in Hours",
        "venueCapacity": "Venue Capcity"
    },
)

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    event_ids = [item['eventID'] for item in data if 'eventID' in item]

    if event_ids:
        id_to_delete = st.selectbox("Select the Event ID", options=event_ids)

if st.button('Delete Event'):
    if id_to_delete:
     edited_event_data = {
        "eventID" : str(id_to_delete)
    }
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
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')
