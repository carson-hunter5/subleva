import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Bulletin", page_icon="🙏")
SideBarLinks()
add_logo("assets/logo.png", height=400)

st.header("Recent Bulletin Posts")

data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/posts').json()
except:
  st.write("**Important**: Could not connect to database")

edited_data = st.data_editor(
    data,
    column_config={
        "createdAt": "Date Posted",
        "displayName": "User Name",
        "postContent": "Post",
    },
)

st.header("**Create a Post**")
migrantID = st.session_state["id"]
displayName = st.text_input("Display Name")
post_content = st.text_input("Post Content")
post_id = st.number_input("Post ID")

if st.button("Submit"):
    if post_content and post_id and displayName and migrantID:
        post_data = {
            "postContent" : post_content,
            "postID" : post_id,
            "displayName" : displayName,
            "migrantID" : migrantID
        }
        response = requests.post("http://api:4000/m/migrant/add_post",json=post_data)

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')