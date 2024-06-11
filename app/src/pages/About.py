import streamlit as st

from modules.nav import SideBarLinks

# Set page configuration first
st.set_page_config(page_title="About Subleva",page_icon= "🧠")
SideBarLinks()

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


    """
)

st.subheader("**Concept and Creation By**:"  )

col1, col2, col3 = st.columns(3)

with col1:
  st.write("")
  st.write(":green[**Carson Hunter**]")

with col2:
  st.write("")
  st.write(":green[**Ivionna Jordan**]")

with col3:
  st.write("")
  st.write(":green[**Dylan Sacks**]")

if st.button('Subleva Home', 
             type='primary',
             use_container_width=True):
  st.switch_page('Home.py')