import streamlit as st

from app.service.captcha import create_captcha

image, captcha_text = create_captcha()


def registration():
    st.title("Form Registration")

    with st.form("my_form"):
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
