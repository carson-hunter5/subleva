import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Manage Community Bulletin", page_icon="")

add_logo("assets/logo.png", height=400)

SideBarLinks()
st.header("All Bulletin Posts", divider='green')

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

st.subheader("Delete a Post", divider='green')

if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    post_ids = [item['postID'] for item in data if 'postID' in item]

    if post_ids:
        id_to_delete = st.selectbox("Select the post ID", options=post_ids)
        delete_button = st.button('Delete Post')

        if delete_button:
            response = requests.delete(f'http://api:4000/c/city_council/delete_bulletin/{id_to_delete}')
            data = [item for item in data if item['postID'] != id_to_delete]
            st.experimental_rerun()  

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')