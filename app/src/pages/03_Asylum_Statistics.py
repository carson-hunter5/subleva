import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config (page_title="Asylum Statistics", page_icon="📊")

SideBarLinks()