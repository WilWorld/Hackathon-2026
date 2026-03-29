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

# Links
with st.container(border=True, gap="small"):
    column1, column2, column3 = st.columns(3)
    with column1:
        st.link_button("Github", url="https://github.com/WilWorld/Hackathon-2026.git", width="stretch")
    with column2:
        st.link_button("Devpost", url="https://devpost.com/submit-to/25559-kent-hack-enough-2026/manage/submissions/981922-grug-generate-really-unbreakable-gibberish/project_details/edit", width="stretch")
    with column3:
        st.link_button("Demo Video", url="https://www.youtube.com/watch?v=pZ_jagPxsYw&list=PLZVB6961ef9oSxDhjXOV5Ih2l4ovSh5eH", width="stretch")

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