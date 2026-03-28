import streamlit as st

# Page styling
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #8C5F1E;  
    }
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .stText {
        font-size: 110%;
        font-weight: bold;
    }
    [data-testid="stSidebar"] * {
        color: #fff;  
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Freckle+Face" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Page setup
st.set_page_config(
    page_title="GRUG", 
    page_icon="🗿", 
    layout="wide",
)

# Header
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">GENERATE REALLY UNBREAKABLE GIBBERISH</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

# Sidebar logo
st.sidebar.image("assets/logo1.png")

# Homepage picture
st.image("assets/caveman_password.jpg", width="stretch")
