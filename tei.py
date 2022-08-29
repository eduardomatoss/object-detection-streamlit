import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox
import streamlit as st


def handle_picture(picture):
    return detect_on_image(picture)


def detect_on_image(image):
    bbox, label, conf = cv.detect_common_objects(image, confidence=0.5, enable_gpu=True)
    return draw_bbox(image, bbox, label, conf), label


st.title("Checking profile")
run = st.checkbox("Run")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    validation, frame = camera.read()
    if not validation:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img, label = handle_picture(frame)
    FRAME_WINDOW.image(frame)

    if 'person' in label and 'clock' in label:
        st.success('Successfully Registered!')
        break
    else:
        st.error('Validation image error, please try again!')

camera.release()