import logging
import requests
import streamlit as st

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="City Council Home", page_icon="🏠")
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}")

col1, col2 = st.columns(2)

# column that divides up the tasks which lead to the correpsoning pages for a city council woman
with col1:
 st.subheader("Navigation", divider="green")
 if st.button('Manage Community Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Community_Events.py')

 if st.button('Manage Bulletin Board', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_City_Council_Bulletin.py')

 if st.button('Manage Appointments', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')

 st.subheader("Upcoming Events", divider="green")

 #gets all the events from the database
 data = {} 
 data = requests.get('http://api:4000/c/city_council/database').json()
 logger.info(f'Data is: {data}')
 for row in data:
  row["eventDate"] = ' '.join(row["eventDate"].split(' ')[:4])

 logger.info(type(data))

 #edits the column name
 edited_data = st.data_editor(
    data,
    column_config={
        "name": "Event Name",
        "eventDate": "Date",
        "eventID": "Event ID",
    },
    use_container_width= True,
    column_order=("eventID", "name", "eventDate")
)

# general dashboard aestethics 
with col2:
 st.image("https://i.imgur.com/TbrU8c8.jpeg" ,use_column_width="auto")

 st.subheader("To-Do", divider="green")
 task1 = st.checkbox("Check Post Analytics")
 task2 = st.checkbox("Read Volunteer Notes")
 task3 = st.checkbox("Plan the Annual Town Hall")
 task4 = st.checkbox("University Tour for Local Students")
 task5 = st.checkbox("Add New Community Events to the Bulletin")
 task6 = st.checkbox("Set up Election Campaign Posts")