import streamlit as st
import requests
import logging

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Events", page_icon="🎟️")
SideBarLinks()

st.header("Community Events Near You", divider='green')

# getting the list of events 
data = {} 
data = requests.get('http://api:4000/m/migrant/events').json()
logger.info(f'Data is: {data}')
for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])

# editing the data format and layout
logger.info(type(data))
edited_data = st.data_editor(
    data,
    column_config={
        "name": "Event Name",
        "eventDate": "Date",
        "duration": st.column_config.NumberColumn(
            "Duration",
             format="%d Hours",
         ),
    },
    use_container_width= True,
    column_order=("name", "eventDate", "duration")
)

# General dashboard aesthetics with a photo gallery
st.header("Photo Gallery", divider='green')

col1, col2 = st.columns(2)
with col1:
   st.image("https://i.imgur.com/7E7XKw6.jpeg", caption='Dr. Wilson Madea speaking at the 50th anniversary')
   st.image("https://i.imgur.com/lvRekP3.jpeg", caption="Students listening to city council elect - Tanya Bracker" )
   st.image("https://i.imgur.com/QtGEdj2.jpeg", caption="Celebration of Cultures Festival")


with col2:
   st.image("https://i.imgur.com/Hcmqbu2.jpeg", caption= "Samara and Akira Dahli celebrating graduation at Rutgers University")
   st.image("https://i.imgur.com/oNfXkWU.jpeg", caption= "4th graders at Duncanville Elementary learning about the importance of healthy living")