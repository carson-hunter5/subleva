import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Bulletin", page_icon="🙏")
SideBarLinks()
add_logo("assets/logo.png", height=400)

st.header("Recent Bulletin Posts", divider='green')

data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/posts').json()
except:
  st.write("**Important**: Could not connect to database")

edited_data = st.data_editor(
    data,
    column_config={
        "createdAt": "Date Posted",
        "displayName": "Display Name",
        "postContent": "Post",
    },
)

col1, col2 = st.columns(2, gap = "medium")

with col1:
 st.header("**Create a Post**", divider='green')
 migrantID = st.session_state["id"]
 displayName = st.text_input("Display Name")
 post_content = st.text_input("Post Content")
 post_id = st.number_input("Post ID",value=0, step=1)

if st.button("Submit"):
    if post_content and displayName and migrantID:
        post_data = {
            "postContent" : post_content,
            "postID" : post_id,
            "displayName" : displayName,
            "migrantID" : migrantID
        }
        response = requests.post("http://api:4000/m/migrant/add_post",json=post_data)

with col2:
   st.subheader("Trending Post")
   st.image("https://i.imgur.com/Hcmqbu2.jpeg")
   st.caption("Congrats to my baby sister Samara fopr graduating from Rutgers University!")
   st.caption("#firstgen    #youdidit    #classof2k23")

if st.button('Back', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_Migrant_Home.py')