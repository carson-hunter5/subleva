import streamlit as st
import requests
import logging
import requests

from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config (page_title="Appointments", page_icon="📌")
SideBarLinks()

# set the header of the page
st.header('Appointments', divider='green')
st.write("Hello! Here is a list of all your appointments scheduled to meet with a representative on behalf of Tanya Bracker.")

attendeeID = st.session_state["id"]

#add a filter 
#topic = st.selectbox(label= "Filter By Topic", options=("Appointment Topic",("Training", "Marketing", "Accounting", "Services", "Sales", 
     #"Engineering", "Legal", "Support", "Human Resources", 
     #"Business Development","Product Management", "Research and Development")))

# data from the appointments for a specifc attendee from the users table
data = {} 
data = requests.get(f"""http://api:4000/m/migrant/appointments/{attendeeID}""").json()
logger.info(f'Data is: {data}')
for row in data:
  row["appDate"] = ' '.join(row["appDate"].split(' ')[:4])
logger.info(type(data))

#editing the data layout and format
edited_data = st.data_editor(
    data,
    column_config={
        "appDate": "Date",
        "COUNT(aa.attendeeID)" : "Reserved Spots",
        "subject": "Topic",
        "weekday": "Day",
        "name": "Volunteer Name"
    },
    use_container_width= True,
    column_order=("appDate","weekday", "name", "subject", "COUNT(aa.attendeeID)")
)

col1, col2 = st.columns(2, gap = "medium")

# Creating an Appointment
with col1:
 if st.button('New Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Schedule_Appointment.py')

# Appointment Deletion 
with col2: 
 if st.button('Delete Appointment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Cancel_Appointment.py')