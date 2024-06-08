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

st.header("Cancel Event", divider='green')

data = {} 
data = requests.get('http://api:4000/c/city_council').json()


if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    event_ids = [item['eventID'] for item in data if 'eventID' in item]

    if event_ids:
        id_to_delete = st.selectbox("Select the Event ID", options=event_ids)

if st.button('Delete Event'):
    if id_to_delete:
    edited_event_data = {
        "eventID" : str(id_to_delete)
    }
    response = requests.delete(f'http://api:4000/c/city_council/community_event/{id_to_delete}')
    data = [item for item in data if item['eventID'] != id_to_delete] 

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')
