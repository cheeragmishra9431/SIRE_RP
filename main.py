# streamlit_app.py

import streamlit as st
import mysql.connector


@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()




 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
SignupSection=st.container()
logOutSection = st.container()
 
def show_main_page():
    with mainSection:
        # dataFile = st.text_input("Enter your Test file name: ")
        # Topics = st.text_input("Enter your Model Name: ")
        # ModelVersion = st.text_input("Enter your Model Version: ")
        # processingClicked = st.button ("Start Processing", key="processing")
        # if processingClicked:
        #        st.balloons() 
        st.header('Henlo!!!')
 
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    # if login(userName, password):
    #     st.session_state['loggedIn'] = True
    # else:
    #     st.session_state['loggedIn'] = False;
    #     st.error("Invalid user name or password")
    # loginSection.empty()
    
    #Run a query for the specific phone number or email and then match the passoword.

    # st.session_state['loggedIn']=True
    rows = run_query("SELECT * from User_Info ")
    for row in rows:
        # st.write(f"{row[0]} has a :{row[1]}:")
        if userName == row[1] and password == row[3]:
            st.session_state['loggedIn']=True
            st.write(row[1], row[2], row[3])
            break
    st.error('Invalid user name or password')
    # st.write(rows)
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))


with headerSection:
    st.title("Welcome!!!")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
        else:
            show_login_page()

