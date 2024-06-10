import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Bulletin", page_icon="📝")
SideBarLinks()
add_logo("assets/logo.png", height=400)

st.header("Recent Bulletin Posts", divider='green')

# getting all the posts 
data = {} 
try:
  data = requests.get('http://api:4000/m/migrant/posts').json()
except:
  st.write("**Important**: Could not connect to database")

# edits the column names
edited_data = st.data_editor(
    data,
    column_config={
        "createdAt": "Date Posted",
        "displayName": "Display Name",
        "postContent": "Post",
    },
)

col1, col2 = st.columns(2, gap = "medium")

# allows the user to make a post onto the bulletin board and it displays
with col1:
 st.header("**Create a Post**", divider='green')
 migrantID = st.session_state["id"]
 displayName = st.text_input("Display Name")
 post_content = st.text_input("Post Content")

 if st.button("Submit"):
    if post_content and displayName and migrantID:
        post_data = {
            "postContent" : post_content,
            "displayName" : displayName,
            "migrantID" : migrantID
        }
        response = requests.post("http://api:4000/m/migrant/add_post",json=post_data)
        if response.status_code == 200:
                st.session_state["message"] = ":green[Posted Sucessfully!]"
        else:
                st.session_state["message"] = ":red[Failed to post.]"

        if "message" in st.session_state:
         st.write(st.session_state["message"])
    del st.session_state["message"]

# general aesthetic information
with col2:
   st.header("Trending Post", divider = 'green')
   st.image("https://i.imgur.com/Hcmqbu2.jpeg")
   st.caption("Congrats to my baby sister Samara fopr graduating from Rutgers University!")
   st.caption("#firstgen    #youdidit    #classof2k23")