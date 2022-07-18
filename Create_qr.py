import streamlit as st
import json
from urllib.request import urlopen
import pyqrcode as py

st.header("Create QR Code With Your Json")

js = st.text_input("Json Api", "Write Your Json Link")

dictt = st.text_input("Dict Value", "Write Your Json Dict Value")

z = st.number_input("Qr Scale: recommended=8", )

def createqr():
    with urlopen(js) as response:
        kaynak = response.read()
    global veri
    veri = json.loads(kaynak)

    t = 0
    for res in veri:
        t+=1
        x = res[dictt]
        y = py.create(x)
        y.svg(f"qr{t}.svg", scale=z)

if st.button("Create"):
    createqr()
    st.text("Wait a few minutes...")
    time.sleep(15)

