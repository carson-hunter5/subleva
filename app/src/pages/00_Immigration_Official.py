import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')

col1, col2 = st.columns(2)

with col1:
 st.image("https://i.imgur.com/mWUPjtq.jpeg")

 st.write('')

 st.subheader("Your Tasks", divider="green")
 if st.button('View Population Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Population.py')

 if st.button('View Current Asylum Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Asylum_Application.py')

 if st.button('View Asylum Applications Statistics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Asylum_Statistics.py')

with col2:
  st.subheader("Urgent Responses", divider="green")
  companyQuestion = st.radio(
        "Will you be attending the executive meeting on this upcoming Friday **in Person**?",
        ["Yes", "Maybe", " No"],
        index= None,
  )

  opinion = st.select_slider(
    "How satsfied were you with last Tuesday **June 4th's** guest lecture?",
    options=["Highly Dissatsfied", "Dissatsfied", "Average", "Sastfied", "Highly Satsfied"],
    )
  st.write("You voted:", opinion)

  st.image("https://i.imgur.com/FDCOhVv.png")
