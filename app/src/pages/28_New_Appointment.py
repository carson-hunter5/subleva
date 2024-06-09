import streamlit as st
import requests
import datetime
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Appointment Manager", page_icon="📅")

add_logo("assets/logo.png", height=400)

SideBarLinks()

st.header("New Appoinment", divider='green')

# Creates an Appointment
volunteerID = st.number_input("Volunteer ID", value=0, step=1)
appDate = st.date_input("Event Date", value=datetime.date.today())
subject = st.selectbox("Appointment Topic",("Training", "Marketing", "Accounting", "Services", "Sales", 
     "Engineering", "Legal", "Support", "Human Resources", 
     "Business Development","Product Management", "Reseearch and Development"))
weekday = st.selectbox("Weekday", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))

if st.button("Submit"):
    if volunteerID and appDate and subject and weekday:
        post_data = {
            "volunteerID" : volunteerID,
            "appDate" : str(appDate),
            "subject" : subject,
            "weekday" : weekday
        }
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
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_City_Council_Appointments.py')