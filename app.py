import streamlit as st

# Type this in to run the file
# streamlit run app.py

# Streamlit stuff
st.set_page_config(
    page_title="GRUG", 
    page_icon="🗿", 
    layout="wide",
)

st.title(":orange[GENERATE REALLY UNBREAKABLE GIBBERISH]", text_alignment="center")

st.sidebar.image("assets/logo1.png")

st.image("assets/caveman_password.jpg", width="stretch")
