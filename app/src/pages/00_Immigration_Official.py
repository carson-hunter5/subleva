import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="Immigration Official Home", page_icon="🏠")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')

col1, col2 = st.columns(2)

with col1:
 st.image("https://i.imgur.com/mWUPjtq.jpeg")

 st.write('')

# Button links to the proper pages for the user to get to from the home page
 st.subheader("Navigation", divider="green")
 if st.button('View Population Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Population.py')

 if st.button('Application Predictor', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Asylum_Application.py')

 if st.button('View Accepted Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Application_Predictions.py')

# Dashboard inputs to look more professional
with col2:
  st.subheader("Urgent Responses", divider="green")
  companyQuestion = st.radio(
        "Will you be attending the executive meeting on this upcoming Friday **in Person**?",
        ["Yes", "Maybe", " No"],
        index= None,
  )

  companyQuestion2 = st.radio(
        "Have you completed the new AI literacy training yet?",
        ["Yes", " No"],
        index= None,
  )

  opinion = st.select_slider(
    "How satsfied were you with last Tuesday **June 4th's** guest lecture?",
    options=["Highly Dissatsfied", "Dissatsfied", "Average", "Sastfied", "Highly Satsfied"],
    )
  st.write("")
  st.write("You voted:", opinion)

  st.subheader("To-Do", divider="green")
  task1 = st.checkbox("Process Asylum Applications")
  task2 = st.checkbox("Manage Immigration Detention from Serbia")
  task3 = st.checkbox("Review Immigration Forms")
  task4 = st.checkbox("Attend Company Training on Tuesday, June 11th")

  
