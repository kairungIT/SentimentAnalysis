import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Kairung Hengpraprohm")

col1, col2 = st.columns(2)
with col1:
    lot3="https://lottie.host/defef63f-5b59-455d-a6e0-ff03f2791104/t43d8wbLKq.json"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
