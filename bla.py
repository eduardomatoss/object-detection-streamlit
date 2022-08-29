import cv2
import streamlit as st

st.title("Checking profile")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


while run:
    validation, frame = camera.read()
    if not validation:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
