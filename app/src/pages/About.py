import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Set page configuration first
st.set_page_config(page_title="About")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Add logo
add_logo("assets/logo.png", height=400)

# Write content
st.write("# About Subleva")
st.markdown(
    """
    Migration is a natural byproduct of human society and remains a highly 
    important topic for governments, politicians, and citizens alike. Often 
    polarizing, this topic can evoke a wide range of emotions. Subleva aims 
    to mitigate this contention by providing a quantitative approach to understanding
    migration from both perspectives and offers resources for migrants. Our app focuses
    on visualizing and predicting migration patterns, to offer stakeholders a data-driven
    perspective on refugees and refugee stories.  

    Created By:

    Carson Hunter    

    Ivionna Jordan 
             
    Dylan Sacks
    """
)

if st.button('Back Home', 
             type='primary',
             use_container_width=True):
  st.switch_page('Home.py')