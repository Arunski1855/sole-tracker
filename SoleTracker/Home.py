{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
from PIL import Image\
\
# App Config\
st.set_page_config(\
    page_title="Sole Tracker",\
    page_icon="\uc0\u55357 \u56415 ",\
    layout="wide",\
)\
\
# Load logos\
eybl_logo = Image.open("assets/eybl.png")\
sssb_logo = Image.open("assets/3ssb.png")\
uaa_logo = Image.open("assets/uaa.png")\
puma_logo = Image.open("assets/puma.png")\
\
# Sidebar\
st.sidebar.image(eybl_logo, width=150)\
st.sidebar.image(sssb_logo, width=150)\
st.sidebar.image(uaa_logo, width=150)\
st.sidebar.image(puma_logo, width=150)\
\
st.sidebar.title("Sole Tracker Navigation")\
page = st.sidebar.radio("Go to:", ["Brand Dashboard", "Comp Finder", "Growth Tracker"])\
\
# Pages\
if page == "Brand Dashboard":\
    st.experimental_set_query_params(page="1_Brand_Dashboard")\
    st.switch_page("pages/1_Brand_Dashboard.py")\
elif page == "Comp Finder":\
    st.experimental_set_query_params(page="2_Comp_Finder")\
    st.switch_page("pages/2_Comp_Finder.py")\
elif page == "Growth Tracker":\
    st.experimental_set_query_params(page="3_Growth_Tracker")\
    st.switch_page("pages/3_Growth_Tracker.py")\
}