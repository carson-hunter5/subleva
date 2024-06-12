import logging
import streamlit as st

logger = logging.getLogger()

from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide', page_title="Immigration Official Home", page_icon="🏠")
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}")
st.write('')

col1, col2 = st.columns(2)

with col1:
 st.image("https://i.imgur.com/mWUPjtq.jpeg", use_column_width="auto")

# Button links to the proper pages for the user to get to from the home page
 st.subheader("Navigation", divider="green")
 if st.button('Application Predictor', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/02_Asylum_Application.py')

 if st.button('Accepted Application Prediction', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Application_Predictions.py')

 if st.button('View Population Data', 
             type='primary',
             use_container_width=True):
   st.switch_page('pages/01_Population.py')


# Dashboard inputs to look more professional
with col2:
  st.subheader("Urgent Responses", divider="green")
  companyQuestion2 = st.radio(
        "Have you completed the new AI literacy training yet?",
        ["Yes", " No"],
        index= None,
  )

  opinion = st.select_slider(
    "On a scale of 1-10, how satsfied were you with last Tuesday **June 4th's** guest lecture?",
    options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    )
  st.write("You voted:", opinion)

  st.subheader("To-Do", divider="green")
  task1 = st.checkbox("Process Asylum Applications")
  task2 = st.checkbox("Manage Immigration Detention from Serbia")
  task3 = st.checkbox("Contact UNHCR Representatives")
  task4 = st.checkbox("Attend Company Training on Tuesday, June 11th")
  task5 = st.checkbox("Immigration Policy Meeting on Thursday, June 23th")