import streamlit as st
import requests
import datetime
import requests
import logging
import pandas as pd

from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment Manager", page_icon="📅")
SideBarLinks()

st.header("New Appoinment", divider='green')

#gets all data
volunteer_data = {}
volunteer_data = requests.get("http://api:4000/c/city_council/volunteers").json()
logging.info(volunteer_data)

#edit the data format and layout
edited_data = st.data_editor(
    volunteer_data,
    column_config={
        "name": "Volunteer Name",
        "id": "Volunteer ID",
    },
    use_container_width= True,
    column_order=("id", "name")
)
volunteer_dict = pd.DataFrame(volunteer_data)

# Creates an Appointment
volunteerID = st.selectbox("Select a Volunteer ID", options = volunteer_dict["id"],index=None)
appDate = st.date_input("Event Date", value=datetime.date.today())
subject = st.selectbox("Appointment Topic",("Training", "Marketing", "Accounting", "Services", "Sales", 
     "Engineering", "Legal", "Support", "Human Resources", 
     "Business Development","Product Management", "Research and Development"),index=None)

if st.button("Submit", type= "primary", use_container_width=True):
    if volunteerID and appDate and subject:
        post_data = {
            "volunteerID" : volunteerID,
            "appDate" : str(appDate),
            "subject" : subject,
            "weekday" : appDate.strftime('%A')
        }

        #route to add the appointment to the list of appointments
        response = requests.post("http://api:4000/c/council/add_appointments", json=post_data)
        if response.status_code == 200:
                st.session_state["message"] = ":green[Appointment Created Sucessfully!]"
                st.balloons()
        else:
                st.session_state["message"] = ":red[Failed to Create Appointment.]"

        if "message" in st.session_state:
         st.write(st.session_state["message"])
    del st.session_state["message"]


if st.button('Back', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')