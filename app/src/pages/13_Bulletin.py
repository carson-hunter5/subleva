import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo

st.set_page_config (page_title="Bulletin", page_icon="🙏")

add_logo("assets/logo.png", height=400)

st.write("See Recent Bulletin Posts")

data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/posts').json()
except:
  st.write("**Important**: Could not connect to database")

st.dataframe(data)

st.write("**Create a Post:**")
post_content = st.text_input("Post Content")
post_id = st.number_input("Post ID")
displayName = st.text_input("Display Name")
migrantID = st.session_state["id"]

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