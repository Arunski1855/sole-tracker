import streamlit as st
from PIL import Image

# Set up page configuration
st.set_page_config(
    page_title="Sole Tracker",
    page_icon="👟",
    layout="wide",
)

# Sidebar with logos and navigation
st.sidebar.title("Sole Tracker Navigation")

# Load logos
try:
    eybl_logo = Image.open("assets/eybl.png")
    sssb_logo = Image.open("assets/3ssb.png")
    uaa_logo = Image.open("assets/uaa.png")
    puma_logo = Image.open("assets/puma.png")

    st.sidebar.image(eybl_logo, width=120)
    st.sidebar.image(sssb_logo, width=120)
    st.sidebar.image(uaa_logo, width=120)
    st.sidebar.image(puma_logo, width=120)

except:
    st.sidebar.warning("Logos not found. Continue without them.")

# Page Navigation
page = st.sidebar.radio("Go to:", ["Brand Dashboard", "Comp Finder", "Growth Tracker"])

# Redirect based on selection
if page == "Brand Dashboard":
    st.switch_page("pages/1_Brand_Dashboard.py")
elif page == "Comp Finder":
    st.switch_page("pages/2_Comp_Finder.py")
elif page == "Growth Tracker":
    st.switch_page("pages/3_Growth_Tracker.py")
