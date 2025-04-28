{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import plotly.express as px\
\
st.title("Comp Finder")\
\
st.write("Compare players using percentile rankings: C-RAM, ATR, PSP and more!")\
\
# Example placeholder data\
data = \{\
    "Player": ["Marcus Spears Jr.", "Jordan Tyler", "Chris Barlow"],\
    "C-RAM Percentile": [92, 81, 78],\
    "ATR Percentile": [88, 74, 65],\
    "PSP Percentile": [91, 80, 70],\
\}\
\
df = pd.DataFrame(data)\
\
# Select Player\
player = st.selectbox("Select a player to compare:", df["Player"].unique())\
\
# Get Player Row\
selected_player = df[df["Player"] == player]\
\
# Display Radar/Bar Chart\
st.subheader(f"Percentile Rankings for \{player\}")\
\
fig = px.bar(\
    selected_player.melt(id_vars=["Player"], var_name="Metric", value_name="Percentile"),\
    x="Metric",\
    y="Percentile",\
    text="Percentile",\
    range_y=[0, 100],\
    title=f"\{player\} Performance Percentiles",\
)\
st.plotly_chart(fig)\
}