import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Kairung Hengpraprohm")

col1, col2 = st.columns(2)
with col1:
    st.image('./pic/kairung.jpg')
    lot3="https://lottie.host/9d7858db-0b59-4395-ae0f-b57203577235/vTJKGelBz0.json"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
