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
    [class="stVerticalBlock st-emotion-cache-1gz5zxc e12zf7d53"] {
        background-color: #8C5F1E;  
    }
    [data-testid="stContainer"] * {
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
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">RULES</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

# Instruction box
with st.container(border=True, gap="small"):
    st.text("1. Create a password of your choice")
    st.text("2. Press \"Enter\"")
    st.text("3. Create a better password based on the prompts")
    st.text("4. Have fun!")
    st.text("5. Repeat")

# Sidebar logo
st.sidebar.image("assets/logo1.png")
