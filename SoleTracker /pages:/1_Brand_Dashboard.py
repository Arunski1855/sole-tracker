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
st.title("Brand Dashboard")\
\
st.write("Filter top athletes by shoe circuit, graduating class, position, and more.")\
\
# Example placeholder for data\
# Later you can connect this to live data if needed\
data = \{\
    "Player": ["Marcus Spears Jr.", "Jordan Tyler", "Chris Barlow"],\
    "Circuit": ["Nike EYBL", "Adidas 3SSB", "UA Next"],\
    "Class": ["2027", "2026", "2027"],\
    "Position": ["SG", "PG", "SF"],\
    "State": ["Texas", "Georgia", "Florida"],\
\}\
\
df = pd.DataFrame(data)\
\
# Filters\
circuit = st.multiselect("Select Circuit(s)", options=df["Circuit"].unique(), default=df["Circuit"].unique())\
grad_class = st.multiselect("Select Class(es)", options=df["Class"].unique(), default=df["Class"].unique())\
position = st.multiselect("Select Position(s)", options=df["Position"].unique(), default=df["Position"].unique())\
\
# Apply Filters\
filtered_df = df[\
    (df["Circuit"].isin(circuit)) &\
    (df["Class"].isin(grad_class)) &\
    (df["Position"].isin(position))\
]\
\
st.dataframe(filtered_df)\
\
# Visual Chart Example\
st.subheader("Players by Circuit")\
fig = px.histogram(filtered_df, x="Circuit", color="Circuit")\
st.plotly_chart(fig)\
}