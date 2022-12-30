# streamlit_app.py

import streamlit as st
import mysql.connector
#importing streamwebrtc
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2

# model with har casscade
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# passing it through model
class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')

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
# SignupSection=st.container()
logOutSection = st.container()
LeftNav=st.sidebar.radio("Navigation",["SignIn","SignUp"])
 
def show_main_page():
    with mainSection:
        # dataFile = st.text_input("Enter your Test file name: ")
        # Topics = st.text_input("Enter your Model Name: ")
        # ModelVersion = st.text_input("Enter your Model Version: ")
        # processingClicked = st.button ("Start Processing", key="processing")
        # if processingClicked:
        #        st.balloons() 
        st.header('Henlo!!!')
        webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	                )
 
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
    rows = run_query("SELECT * from User_Info ;")
    for row in rows:
        # st.write(f"{row[0]} has a :{row[1]}:")
        if userName == row[1] and password == row[3]:
            st.session_state['loggedIn']=True
            st.write(row[1], row[2], row[3])
            break
    

def Signup_Clicked(userName, password, email, phonenumber):
    txt1 = "INSERT INTO User_Info VALUES ({ph},'{Nm}','{Em}','{pa_ss}')".format(ph = phonenumber, Nm= userName, Em= email, pa_ss=password)
    print(txt1)
    txt2=txt1
    run_query(txt2)
    st.session_state['loggedIn']=True
    conn.commit()



def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))
def show_signup_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            email = st.text_input (label="", value="",placeholder="Enter email")
            phonenumber = st.number_input (label="")
            st.button ("Login", on_click=Signup_Clicked, args= (userName, password,email, phonenumber))

if LeftNav == "SignIn":
    with headerSection:
        st.title("SignIn")
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
if LeftNav == "SignUp":
    with headerSection:
        st.title("SignUp")
        #first run will have nothing in session_state
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn'] = False
            show_signup_page() 
        else:
            if st.session_state['loggedIn']:
                show_logout_page()    
                show_main_page()  
            else:
                show_signup_page()



