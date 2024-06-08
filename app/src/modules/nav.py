# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of Immigration Official ------------------------
def ImmigrationHomeNav():
    st.sidebar.page_link("pages/00_Immigration_Official.py", label="Home", icon='👤')

def PopulationNav():
    st.sidebar.page_link("pages/01_Population.py", label="Population Statistics Map", icon='🗺️')

def AsylumApplicationNav():
    st.sidebar.page_link("pages/02_Asylum_Application.py", label="Asylum Application Map", icon='🗺️')

def AsylumStatisticsNav():
    st.sidebar.page_link("pages/03_Asylum_Statistics.py", label="Asylum Statistics", icon='🗺️')

## ------------------------ Examples for Role of Migrant ------------------------
def MigrantHomeNav():
    st.sidebar.page_link("pages/10_Migrant_Home.py", label="Home", icon='🛜')

def AppointmentsNav():
    st.sidebar.page_link("pages/11_Appointments.py", label="Your Appointments", icon='🌺')

def CommunityEventsNav():
    st.sidebar.page_link("pages/12_Community.py", label=" View Community Events", icon='🏦')

def BulletinBoardNav():
    st.sidebar.page_link("pages/13_Bulletin.py", label='Community Bulletin Board', icon='🏢')



#### ------------------------ Examples for Role of City Council ------------------------

def CityCouncilHomeNav():
    st.sidebar.page_link("pages/20_City_Council_Home.py", label="Home", icon='🛜')

def EventManagementNav():
    st.sidebar.page_link("pages/23_Community_Events.py", label="Manage Events", icon='🛜')

def BulletinManagementNav():
    st.sidebar.page_link("pages/24_City_Council_Bulletin.py", label='Manage Bulletin Board', icon='🏢')
# --------------------------------Links Function -----------------------------------------------
# Define the sidebar links function
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role,
    which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show [insert pages here] if the user is a immigration officer.
        if st.session_state['role'] == 'immigration_officer':
            ImmigrationHomeNav()
            AsylumApplicationNav()
            AsylumStatisticsNav()
            PopulationNav()

        # If the user role is migrant, show the [insert pages here] 
        elif st.session_state['role'] == 'migrant':
            MigrantHomeNav()
            AppointmentsNav()
            BulletinBoardNav()
            CommunityEventsNav()
           
        # If the user is an city council member, show them [insert pages here] 
        elif st.session_state['role'] == 'city_council':
            CityCouncilHomeNav()
            EventManagementNav()
            BulletinManagementNav()
            

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

