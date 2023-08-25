import streamlit as st
import pandas as pd
import plotly.express as px
import db_dtypes
# List of your table names
# Set page config
# st.markdown(
#     """
#     <style>
#         /* Main content area */
#         .stApp {
#             background-color: #142D55;
#             secondary-background: #07366B;
#         }
        
#         /* Sidebar */
#         .css-1l02zno {
#             background-color: #142D55;
#         }
        
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
tables = [
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
        <strong>Time Series Analysis</strong> 
    </div>
    """, unsafe_allow_html=True)
# st.title("Air Quality Patterns: A Data Mining Approach to Big Data")
selected_table = st.selectbox('Select a Table:', tables)

# Load and process data
file_path = f"two-columns-time-series-data/{selected_table}_original.parquet"
columns_to_load = ['arithmetic_mean', 'date_local']
df_temp = pd.read_parquet(file_path, columns=columns_to_load)
# df_temp['date_local'] = pd.to_datetime(df_temp['date_local'])
# df_temp = df_temp[df_temp['date_local'].dt.year == 2021]
# df_temp.set_index('date_local', inplace=True)
#save the original data of year 2021 only for later use in local storage as parquet file
# df_temp.to_parquet(f"two-columns-time-series-data/{selected_table}_original.parquet")

# df_temp['date_local'] = pd.to_datetime(df_temp['date_local'])
# df_temp = df_temp[df_temp['date_local'].dt.year == 2021]
# df_temp.set_index('date_local', inplace=True)  # Set the index
df_resampled = df_temp.resample('W').mean().reset_index()

# Create Time Series Plot
fig = px.line(df_resampled, x='date_local', y='arithmetic_mean', title=f'Time Series for {selected_table}')

# Display the Time Series Plot
st.plotly_chart(fig)

# Clean-up
del df_temp
del df_resampled
