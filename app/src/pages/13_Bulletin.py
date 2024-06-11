import streamlit as st
import requests

from modules.nav import SideBarLinks

st.set_page_config (page_title="Community Bulletin", page_icon="📝")
SideBarLinks()

st.header("Recent Bulletin Posts", divider='green')

# getting all the posts 
data = {} 
data = requests.get('http://api:4000/m/migrant/posts').json()

# edits the data layout and format
edited_data = st.data_editor(
    data,
    column_config={
        "createdAt": "Date Posted",
        "displayName": "Display Name",
        "postContent": "Post",
    },
    use_container_width= True,
    column_order=("displayName", "postContent", "createdAt")
)

col1, col2 = st.columns(2, gap = "medium")

# allows the user to make a post onto the bulletin board and it displays
with col1:
 st.header("**Create a Post**", divider='green')
 migrantID = st.session_state["id"]
 displayName = st.text_input("Display Name", max_chars=12)
 post_content = st.text_area("Post Content",height = 130, max_chars=500)

 if st.button("Submit", type= "primary", use_container_width=True):
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
   st.image("https://i.imgur.com/Hcmqbu2.jpeg",use_column_width=True, caption="Congrats to my baby sister Samara fopr graduating from Rutgers University!")