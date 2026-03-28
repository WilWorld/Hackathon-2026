import streamlit as st

st.set_page_config(
    page_title="GRUG", 
    page_icon="🗿", 
    layout="wide",
)

st.title(":orange[CREDITS]", text_alignment="center")

st.sidebar.image("assets/logo1.png")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Charles Gale", text_alignment="center", divider="orange")
    st.image("assets/charlie.jpg", caption="Frontend development")

    st.subheader("Wil Narah", text_alignment="center", divider="orange")
    st.image("assets/wil.jpg", caption="Backend development")
    
with col2:
    st.subheader("Sandy Zhang", text_alignment="center", divider="orange")
    st.image("assets/sandy.jpg", caption="Backend development")

    st.subheader("Anthony Haggerty", text_alignment="center", divider="orange")
    st.image("assets/anthony.jpg", caption="Frontend development")