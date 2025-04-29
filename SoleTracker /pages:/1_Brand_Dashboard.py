import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Brand Dashboard")

st.write("Explore players by shoe circuit, class, and position.")

# Sample data — replace this with your real CSV/API data later
data = {
    "Player": ["Marcus Spears Jr.", "Jordan Tyler", "Chris Barlow", "Jalen Cook", "Braylon Harris"],
    "Circuit": ["Nike EYBL", "Adidas 3SSB", "UA Next", "NXT Pro", "Nike EYBL"],
    "Class": ["2027", "2026", "2027", "2026", "2026"],
    "Position": ["SG", "PG", "SF", "PF", "SG"],
    "State": ["Texas", "Georgia", "Florida", "California", "New York"],
    "AAU Team": ["Team Takeover", "TSF", "Houston Defenders", "Team Griffin", "PSA Cardinals"],
}

df = pd.DataFrame(data)

# Filters
circuits = st.multiselect("Select Circuit(s):", df["Circuit"].unique(), default=df["Circuit"].unique())
classes = st.multiselect("Select Class(es):", df["Class"].unique(), default=df["Class"].unique())
positions = st.multiselect("Select Position(s):", df["Position"].unique(), default=df["Position"].unique())

# Apply filters
filtered_df = df[
    (df["Circuit"].isin(circuits)) &
    (df["Class"].isin(classes)) &
    (df["Position"].isin(positions))
]

st.dataframe(filtered_df)

# Chart: Players by Circuit
st.subheader("Player Count by Circuit")
fig = px.histogram(filtered_df, x="Circuit", color="Circuit", title="Distribution by Circuit")
st.plotly_chart(fig)
