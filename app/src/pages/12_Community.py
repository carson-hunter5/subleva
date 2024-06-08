import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Events", page_icon="🙏")
SideBarLinks()

add_logo("assets/logo.png", height=400)

st.header("Community Events Near You")

data = {} 
data = requests.get('http://api:4000/m/migrant/events').json()

edited_data = st.data_editor(
    data,
    column_config={
        "name": "Event Name",
        "date": "Date",
        "duration": "Duration in Hours",
    },
)

st.header("Photo Gallery")

col1, col2 = st.columns(2)
with col1:
   st.image("https://i.imgur.com/7E7XKw6.jpeg", caption='Dr. Wilson Madea speaking at the 50th anniversary')
   st.image("https://i.imgur.com/lvRekP3.jpeg")
   st.caption("Students listening to a city council elect - Tanya Bracker")
   st.image("https://i.imgur.com/QtGEdj2.jpeg")
   st.caption("Celebration of Cultures Festival")


with col2:
   st.image("https://i.imgur.com/Hcmqbu2.jpeg")
   st.caption("Samara and Akira Dahli celebrating graduation at Rutgers University")
   st.image("https://i.imgur.com/oNfXkWU.jpeg")
   st.caption("4th graders at Duncanville Elementary learning about the importance of healthy living")



if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')
