
import streamlit as st
import requests

st.title("AVA Agent - Standard Bank AI Assistant")

user_input = st.text_input("Ask AVA something...")

if user_input:
    response = requests.post("https://<your-app-service-url>/chat", json={"query": user_input})
    if response.status_code == 200:
        st.write("💬 AVA says:", response.json().get("response"))
    else:
        st.error("Error talking to AVA Agent.")
