import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Growth Tracker")

    st.write("Track C-RAM progression across multiple events for each player.")

    # Sample growth data (replace with Cerebro API data later)
    data = {
        "Event": ["Spring 2024", "Summer 2024", "Fall 2024", "Winter 2025"],
        "Marcus Spears Jr.": [82, 87, 90, 93],
        "Jordan Tyler": [78, 79, 80, 81],
        "Chris Barlow": [75, 76, 78, 80],
    }

    df = pd.DataFrame(data)

    # Player selector
    player = st.selectbox("Select a player to track:", ["Marcus Spears Jr.", "Jordan Tyler", "Chris Barlow"])

    # Line chart for growth
    fig = px.line(
        df,
        x="Event",
        y=player,
        markers=True,
        title=f"{player} C-RAM Growth Over Time",
    )
    st.plotly_chart(fig)
