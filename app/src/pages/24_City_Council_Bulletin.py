import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Manage Community Bulletin", page_icon="")

add_logo("assets/logo.png", height=400)

SideBarLinks()
st.header("All Bulletin Posts")

data = {} 
try:
  data = requests.get('http://api:4000/c/city_council/bulletin').json()
except:
  st.write("**Important**: Could not connect to database")

edited_data = st.data_editor(
    data,
    column_config={
        "displayName": "User Name",
        "migrantID": "User ID",
        "postContent": "Post",
        "postID" : "Post ID",
    },
)


st.write("Delete a Post:")

id_to_delete = st.number_input("Type the post ID",value=0, step=1)
delete_button = st.button('Delete Post')

if delete_button:
 response = requests.delete(f"""http://api:4000/c/city_council/delete_bulletin/{id_to_delete}""")
 if response.status_code == 200:
        st.write(f"Post Deleted")

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')