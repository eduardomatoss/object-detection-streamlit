import streamlit as st


from app.view.form import registration

st.set_page_config()

def create():
    st.title("Bank XPTO")

    if st.button("Start Registration"):
        registration()
