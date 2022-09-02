import streamlit as st

from app.view.form import registration
from app.view.check_profile import check_profile


def startup():
    st.title("Bank XPTO")
    registration()
    check_profile()
