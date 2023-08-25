import pandas as pd
import os
import streamlit as st
import plotly.express as px
import db_dtypes
import gc
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
results_dir = "frequency-analysis-results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Compute frequency analysis and save results
# for table in tables:
#     file_path = f"modified-data/{table}.parquet"
#     df_temp = pd.read_parquet(file_path)

#     for column in df_temp.columns:
#         freq_df = df_temp[column].value_counts().reset_index()
#         freq_df.columns = [column, 'count']
#         freq_df.to_csv(f"{results_dir}/{table}_{column}_freq.csv", index=False)

#     del df_temp

# Streamlit app
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
        <strong>Frequency Analysis Dashboard</strong> 
    </div>
    """, unsafe_allow_html=True)
# st.title("Frequency Analysis Dashboard")

selected_table = st.selectbox("Select a Table:", tables)
# selected_column = st.selectbox("Select a Column:", options=[])
columns_dir = "column-names"
column_file_path = f"{columns_dir}/{selected_table}_columns.parquet"
df_columns = pd.read_parquet(column_file_path)
selected_column = st.selectbox("Select a Column:", df_columns["Column_Name"])
# file_path = f"modified-data/{selected_table}.parquet"
# df_temp = pd.read_parquet(file_path)
# columns = df_temp.columns.tolist()
# del df_temp
# gc.collect()
# selected_column = st.selectbox("Select a Column:", columns)

freq_df = pd.read_csv(f"{results_dir}/{selected_table}_{selected_column}_freq.csv")
fig = px.bar(freq_df, x=selected_column, y='count', title=f'Frequency Analysis for {selected_column} in {selected_table}')
st.plotly_chart(fig)
