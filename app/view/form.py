import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox
import streamlit as st


from app.service.captcha import create_captcha

image, captcha_text = create_captcha()


def handle_picture(picture):
    return detect_on_image(picture)


def detect_on_image(image):
    bbox, label, conf = cv.detect_common_objects(
        image, confidence=0.2, model="yolov3-tiny", enable_gpu=True
    )
    return draw_bbox(image, bbox, label, conf), label


def registration():
    st.title("Form Registration")

    with st.form("Registration"):
        st.write("Registration")
        st.text_input("Name")
        st.text_input("Last Name")
        st.image(image)
        captcha_input = st.text_input("Captcha")

        register = st.form_submit_button("Register")
        if register:
            if captcha_text == captcha_input:
                st.success("Captcha Valid")
            else:
                st.error("Captcha Invalid")

    with st.form("Checking profile"):
        st.write("Checking profile")

        run = st.checkbox("Run")

        validate = st.form_submit_button("Validate")
        if validate:
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)

            while run:
                validation, frame = camera.read()
                if not validation:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img, label = handle_picture(frame)
                FRAME_WINDOW.image(frame)

                if "person" in label and "clock" in label:
                    st.success("Successfully Registered!")
                    break
                elif "person" in label and "apple" in label:
                    st.success("Successfully Registered!")
                    break
                elif "person" in label and "apple" in label:
                    st.success("Successfully Registered!")
                    break

            camera.release()
