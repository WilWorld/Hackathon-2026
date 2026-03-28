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
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">CREDITS</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

# Sidebar logo
st.sidebar.image("assets/logo1.png")

# Credit pictures and descriptions
with st.container(border=True, gap="small"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Charles Gale", text_alignment="center", divider="orange")
        st.image("assets/charlie.jpg", caption="Frontend development")

        st.subheader("Wil Nahra", text_alignment="center", divider="orange")
        st.image("assets/wil.jpg", caption="Backend development")
        
    with col2:
        st.subheader("Sandy Zhang", text_alignment="center", divider="orange")
        st.image("assets/sandy.jpg", caption="Backend development")

        st.subheader("Anthony Haggerty", text_alignment="center", divider="orange")
        st.image("assets/anthony.jpg", caption="Frontend development")