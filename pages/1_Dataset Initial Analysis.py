import streamlit as st
import pandas as pd
import os
# Set page config
# st.markdown(
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

# Directory to save results
results_dir = "tables-analysis-results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Check if the table_sizes.csv already exists
# if not os.path.isfile(f"{results_dir}/table_sizes.csv"):
#     table_sizes = {}
#     # Compute size of each table and save results
#     for table in tables:
#         file_path = f"data/{table}.parquet"
#         df_temp = pd.read_parquet(file_path)
#         table_sizes[table] = len(df_temp)
#         # Number of columns in each table
#         table_sizes[table] = len(df_temp.columns)
#         del df_temp

#     # Convert table sizes into DataFrame and save as CSV
#     df_sizes = pd.DataFrame(list(table_sizes.items()), columns=["Table", "Rows", "Columns"])
#     df_sizes.to_csv(f"{results_dir}/table_sizes.csv")

# Convert large numbers to readable format
def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.1f%s' % (num, ['', 'K', 'M', 'B', 'T'][magnitude])

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
        <strong>Table Sizes Analysis</strong> 
    </div>
    """, unsafe_allow_html=True)


# st.title("Table Sizes Analysis")

# Load table sizes data
df_sizes = pd.read_csv(f"{results_dir}/table_sizes.csv")
df_sizes["Rows"] = df_sizes["Rows"].apply(human_format)

st.table(df_sizes)
