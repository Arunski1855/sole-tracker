import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Comp Finder")

    st.write("Compare players using percentile rankings like C-RAM, ATR, and PSP.")

    # Sample percentile data (replace with live data later)
    data = {
        "Player": ["Marcus Spears Jr.", "Jordan Tyler", "Chris Barlow"],
        "C-RAM Percentile": [92, 81, 78],
        "ATR Percentile": [88, 74, 65],
        "PSP Percentile": [91, 80, 70],
    }

    df = pd.DataFrame(data)

    # Player selection
    player = st.selectbox("Select a player to view percentile breakdown:", df["Player"].unique())

    selected_player = df[df["Player"] == player]

    # Convert to long format for bar chart
    melted = selected_player.melt(id_vars="Player", var_name="Metric", value_name="Percentile")

    # Bar chart
    fig = px.bar(
        melted,
        x="Metric",
        y="Percentile",
        color="Metric",
        range_y=[0, 100],
        text="Percentile",
        title=f"{player} Percentile Rankings",
    )
    st.plotly_chart(fig)
