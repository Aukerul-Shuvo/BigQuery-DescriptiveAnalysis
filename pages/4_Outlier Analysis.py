import streamlit as st
import pandas as pd
import os
import gc
import plotly.express as px
import db_dtypes
# List of tables
# Set page config
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

# Directory to save outlier results and column names
results_dir = "outliers-analysis-results"
columns_dir = "column-names"

# if not os.path.exists(results_dir):
#     os.makedirs(results_dir)
# if not os.path.exists(columns_dir):
#     os.makedirs(columns_dir)

# Compute outliers using IQR method and save results
# for table in tables:
#     file_path = f"modified-data/{table}.parquet"
#     df_temp = pd.read_parquet(file_path)

#     # Save numerical column names
#     numerical_columns = df_temp.select_dtypes(include=['float64', 'int64']).columns
#     pd.DataFrame(numerical_columns, columns=["Column_Name"]).to_parquet(f"{columns_dir}/{table}_columns.parquet")

#     for column in numerical_columns:
#         Q1 = df_temp[column].quantile(0.25)
#         Q3 = df_temp[column].quantile(0.75)
#         IQR = Q3 - Q1

#         # Filter out the outliers
#         outliers_df = df_temp[(df_temp[column] < (Q1 - 1.5 * IQR)) | (df_temp[column] > (Q3 + 1.5 * IQR))]
#         outliers_df.to_parquet(f"{results_dir}/{table}_{column}_outliers.parquet", index=False)

#     del df_temp
#     gc.collect()

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
        <strong>Outlier Analysis</strong> 
    </div>
    """, unsafe_allow_html=True)

# st.title("Outlier Analysis")

selected_table = st.selectbox("Select a Table:", tables)

# Load column names for the selected table
column_file_path = f"{columns_dir}/{selected_table}_columns.parquet"
if os.path.exists(column_file_path):
    df_columns = pd.read_parquet(column_file_path)
    selected_column = st.selectbox("Select a Column:", df_columns["Column_Name"])

    # Load the outliers for the selected table and column
    file_path = f"{results_dir}/{selected_table}_{selected_column}_outliers.parquet"
    if os.path.exists(file_path):
        df_outliers = pd.read_parquet(file_path)
        #if no outliers found or only one row found
        if df_outliers.shape[0] == 0 or df_outliers.shape[0] == 1:
            st.warning(f"No outliers found for {selected_table}_{selected_column}")
        # Display boxplot with outliers
        fig = px.box(df_outliers, y=selected_column, title=f"Boxplot with Outliers for {selected_column} in {selected_table}")
        st.plotly_chart(fig)
    else:
        st.warning(f"No outliers file found for {selected_table}_{selected_column}")
else:
    st.warning(f"No column names file found for {selected_table}")

# Close the connection to the database
df_columns = None
df_outliers = None
gc.collect()
