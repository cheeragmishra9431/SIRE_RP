import cv2
import streamlit as st
import torch

# model = torch.hub.load('ultralytics/yolov5', 'custom','best.pt',force_reload=True)
model = torch.hub.load('ultralytics/yolov5', 'custom','best.pt')

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    results = model(frame)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # FRAME_WINDOW.image(frame)
    df = results.pandas().xyxy[0]
    df = df[df['name'].isin(["Handgun","Knife"])]
    xmin = df['xmin'].values
    ymin = df['ymin'].values
    xmax = df['xmax'].values
    ymax = df['ymax'].values
    name = df['name'].values
    vhcont = len(name)
    for(x1,y1,x2,y2,objectname) in zip(xmin,ymin,xmax,ymax,name):
        cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
        cv2.putText(frame,objectname,(int(x1),int(y1)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.putText(frame,str(vhcont),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
