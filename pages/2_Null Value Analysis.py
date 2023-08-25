import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import os
# Set page config
st.markdown(
    """
    <style>
        /* Main content area */
        .stApp {
            background-color: #142D55;
        }
        
        /* Sidebar */
        .css-1l02zno {
            background-color: #142D55;
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)
# List of tables
tables = [
    "air_quality_annual_summary",
    "co_daily_summary",
    "hap_daily_summary",
    "lead_daily_summary",
    "no2_daily_summary",
    "nonoxnoy_daily_summary",
    "o3_daily_summary",
    "pm10_daily_summary",
    "pm25_frm_daily_summary",
    "pm25_nonfrm_daily_summary",
    "pressure_daily_summary",
    "rh_and_dp_daily_summary",
    "so2_daily_summary",
    "temperature_daily_summary",
    "wind_daily_summary"
]

# Directory to save results
results_dir = "null-value-results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)


# UI components
image_url = 'https://www.cse.ruet.ac.bd/public/assets/images/cse_website_logo.png'
st.markdown(
    f'<img src="{image_url}" width="550" style="display: block; margin: auto; align: center;">',
    unsafe_allow_html=True
)
title = "Air Quality Patterns: A Data Mining Approach to Big Data"
font_family = "Times New Roman"  # Example font family
font_weight = "bold"  # Example font weight
font_size = "5px"  # Example font size
st.markdown(
    f'<h1 style="text-align: center; font-family: {font_family}; font-weight: {font_weight}; font_size: {font_size}; ">{title}</h1>', 
    unsafe_allow_html=True
)

box_style = """
    text-align: center;
    font-family: Times New Roman;
    border: 1px solid #7289DA;
    border-radius: 8px;
    padding: 10px 0;
    margin: 30px 0;
    font-size: 20px
"""

# Student's Name content
st.markdown(f"""
    <div style='{box_style}'>
        <strong>Null Value Analysis</strong> 
    </div>
    """, unsafe_allow_html=True)

# st.title("Null Value Analysis")
selected_table = st.selectbox('Select a Table:', tables)

# Load null value percentages for the selected table
null_values = pd.read_csv(f"{results_dir}/{selected_table}_null_percentage.csv", index_col=0)[selected_table]

# Create the bar plot
fig = go.Figure(data=[
    go.Bar(x=null_values.index, y=null_values.values)
])
fig.update_layout(
    title=f"Null Value Percentage for {selected_table}",
    xaxis_title="Columns",
    yaxis_title="Percentage of Missing Values",
    xaxis_tickangle=45
)

# Display the bar plot
st.plotly_chart(fig)
