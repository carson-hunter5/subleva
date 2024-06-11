import streamlit as st
import requests

from modules.nav import SideBarLinks

st.set_page_config (page_title="Manage Community Bulletin", page_icon="🔖")
SideBarLinks()

st.header("All Bulletin Posts", divider='green')

#gets all data
data = {} 
data = requests.get('http://api:4000/c/city_council/bulletin').json()

#edits the data layout and format
edited_data = st.data_editor(
    data,
    column_config={
        "displayName": "User Name",
        "migrantID": "User ID",
        "postContent": "Post",
        "postID" : "Post ID",
    },
    use_container_width= True,
    column_order=("migrantID","displayName", "postID", "postContent")
)

st.subheader("Delete a Post", divider='green')
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    post_ids = [item['postID'] for item in data if 'postID' in item]

#selects the post id from the list of ids in the dropdown
    if post_ids:
        id_to_delete = st.selectbox("Select a Post ID", options=post_ids, index=None)
        delete_button = st.button('Delete Post', type="primary", use_container_width=True)

        if delete_button:
            #route that deletes the post based on the post id
            response = requests.delete(f'http://api:4000/c/city_council/delete_bulletin/{id_to_delete}')
            data = [item for item in data if item['postID'] != id_to_delete]
            if response.status_code == 200:
                st.session_state["message"] = ":green[Posted Deleted!]"
            else:
                st.session_state["message"] = ":red[Failed to Delete Post.]"

        if "message" in st.session_state:
         st.write(st.session_state["message"])
         del st.session_state["message"] 

if st.button('Back', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/20_City_Council_Home.py')