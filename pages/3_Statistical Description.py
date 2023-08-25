import streamlit as st
import pandas as pd
import os

# # Set page config
# # st.markdown(
#     """
#     <style>
#         /* Main content area */
#         .stApp {
#             background-color: #142D55;
#         }
        
#         /* Sidebar */
#         .css-1l02zno {
#             background-color: #142D55;
#         }
        
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
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

# Check if the statistics-result directory exists
results_dir = "../statistics-result"
load_from_directory = os.path.exists(results_dir)
global_stats_df = {}

if load_from_directory:
    for table in tables:
        stats_file_path = os.path.join(results_dir, f"stats_{table}.csv")
        stats_temp = pd.read_csv(stats_file_path)
        global_stats_df[table] = stats_temp.reset_index(drop=True)
else:
    global_stats_df = {table: None for table in tables}

# Streamlit UI
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
        <strong>Data Statistics Analysis</strong> 
    </div>
    """, unsafe_allow_html=True)

# st.title("Table Statistics Viewer")
# st.title("Table Statistics Viewer")
selected_table = st.selectbox('Select a Table:', tables)

if load_from_directory and global_stats_df[selected_table] is not None:
    df = global_stats_df[selected_table]
    st.table(df)
else:
    st.write("No statistics data available for the selected table.")

