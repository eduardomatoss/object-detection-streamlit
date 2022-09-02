import streamlit as st

from app.service.captcha import create_captcha

image, captcha_text = create_captcha()


def registration():

    form = st.form(key="form_registration")
    form.title("Form Registration")
    form.text_input("Name")
    form.text_input("Last Name")
    form.image(image)
    captcha_input = form.text_input("Captcha")
    register = form.form_submit_button("Register")
    if register:
        if captcha_text == captcha_input:
            st.success("Captcha Valid")
            return True
        else:
            st.error("Captcha Invalid")
