import streamlit as st
import requests
import requests
import logging 

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Event Manager", page_icon="💻")
SideBarLinks()

st.header("All Community Events", divider='green')

#gets all data
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
        "name": "Event Name",
        "eventDate": "Date",
        "duration": st.column_config.NumberColumn(
            "Duration",
             format="%d Hours",
         ),
        "eventID" : "Event ID",
        "venueCapacity":"Venue Capacity"
    },
    use_container_width= True,
    column_order=("eventID", "name", "eventDate","duration", "venuCapacity")
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