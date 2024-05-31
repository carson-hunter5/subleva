# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of Immigration Official ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link("pages/00_Immigration_Official.py", label="Immigration Home", icon='👤')

def WorldBankVizNav():
    st.sidebar.page_link("pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon='🏦')

def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon='🗺️')

## ------------------------ Examples for Role of Migrant ------------------------
def MigrantHomeNav():
    st.sidebar.page_link("pages/10_Migrant_Home.py", label="Migrant", icon='🛜')

#def PredictionNav():
   # st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

#def ClassificationNav():
    #st.sidebar.page_link("pages/13_Classification.py", label="Classification Demo", icon='🌺')

#### ------------------------ Examples for Role of City Council ------------------------

def CityCouncilNav():
    st.sidebar.page_link("pages/20_City_Council_Home.py", label="City Council Home", icon='🛜')

#def AdminPageNav():
    #st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    #st.sidebar.page_link("pages/21_ML_Model_Mgmt.py", label='ML Model Management', icon='🏢')


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
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

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'immigration_officer':
            PolStratAdvHomeNav()
            WorldBankVizNav()
            MapDemoNav()

        # If the user role is usaid worker, show the Api Testing page
       # if st.session_state['role'] == 'migrant':
            # ClassificationNav()
        
        # If the user is an administrator, show them their corresponding pages
        if st.session_state['role'] == 'city_council':
            CityCouncilNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

