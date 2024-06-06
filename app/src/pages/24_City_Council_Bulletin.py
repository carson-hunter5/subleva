import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Bulletin", page_icon="🙏")

add_logo("assets/logo.png", height=400)

SideBarLinks()
st.write("See Recent Bulletin Posts")

data = {} 
try:
  data = requests.get('http://api:4000/c/city_council/bulletin').json()
except:
  st.write("**Important**: Could not connect to database")

st.dataframe(data)

st.write("Delete a Post:")


id_to_delete = st.number_input("Type the ID of the Post You'd Like to Delete")
requests.delete(f"""http://api:4000/c/city_council/delete_bulletin/{id_to_delete}""")

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')