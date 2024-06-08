import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['authenticated'] = False

SideBarLinks(show_home=True)

st.title('Subleva')

st.write('\n\n')
st.write('### Welcome to Subleva! Please log in. ')

if st.button("Act as Jackson Davies, a Senior Immigration Official", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True 
    st.session_state['role'] = 'immigration_officer'
    st.session_state['first_name'] = 'Jackson' 
    st.session_state['last_name'] = 'Davies'
    st.switch_page('pages/00_Immigration_Official.py') 

if st.button('Act as Hugo Diallo, a Migrant', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'migrant'
    st.session_state['first_name'] = 'Hugo'
    st.session_state['last_name'] = 'Davies'
    st.session_state['dob'] = 'August 19th, 19'
    st.session_state["id"] = 31
    st.switch_page('pages/10_Migrant_Home.py')

if st.button('Act as Tanya Bracker, the Head of Refugee Affairs for her city council', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'city_council'
    st.session_state['first_name'] = 'Tanya'
    st.session_state['last_name'] = 'Bracker'
    st.switch_page('pages/20_City_Council_Home.py')