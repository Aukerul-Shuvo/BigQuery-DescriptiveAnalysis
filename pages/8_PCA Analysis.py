import streamlit as st
import pandas as pd
import os
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import db_dtypes
import gc
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

# UI Components
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
        <strong>PCA Analysis Dashboard</strong> 
    </div>
    """, unsafe_allow_html=True)
# st.title("PCA Analysis Dashboard")
selected_table = st.selectbox("Select a Table:", tables)
pca_dimension = st.radio("Select PCA Dimension:", ["2D", "3D"])

# # Load and preprocess data
# data_path = f"data/{selected_table}.parquet"
# df_temp = pd.read_parquet(data_path)
# df_temp['date_local'] = pd.to_datetime(df_temp['date_local'])
# df_temp = df_temp[df_temp['date_local'].between('2020-01-01', '2021-12-31')]
# df_numeric = df_temp.select_dtypes(['float64', 'int64'])
# del df_temp
# gc.collect()
# imputer = SimpleImputer(strategy='mean')
# data_imputed = imputer.fit_transform(df_numeric)
# data_scaled = StandardScaler().fit_transform(data_imputed)

# Perform PCA and create plot
file_path_2d = f"pca-analysis-results/{selected_table}_2d.parquet"
file_path_3d = f"pca-analysis-results/{selected_table}_3d.parquet"

if pca_dimension == "2D" and os.path.exists(file_path_2d):
    df_pca = pd.read_parquet(file_path_2d)
    fig = px.scatter(df_pca, x='PC1', y='PC2', title=f'2D PCA for {selected_table}')
    del df_pca
    gc.collect()
elif pca_dimension == "3D" and os.path.exists(file_path_3d):
    df_pca = pd.read_parquet(file_path_3d)
    fig = px.scatter_3d(df_pca, x='PC1', y='PC2', z='PC3', title=f'3D PCA for {selected_table}')
    del df_pca
    gc.collect()
# else:
#     if pca_dimension == '2D':
#         pca = PCA(n_components=2)
#         principalComponents = pca.fit_transform(data_scaled)
#         df_pca = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])
#         df_pca.to_parquet(file_path_2d)
#         fig = px.scatter(df_pca, x='PC1', y='PC2', title=f'2D PCA for {selected_table}')
#         del df_pca, principalComponents, pca
#     else:
#         pca = PCA(n_components=3)
#         principalComponents = pca.fit_transform(data_scaled)
#         df_pca = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2', 'PC3'])
#         df_pca.to_parquet(file_path_3d)
#         fig = px.scatter_3d(df_pca, x='PC1', y='PC2', z='PC3', title=f'3D PCA for {selected_table}')
#         del df_pca, principalComponents, pca

# Display the plot
st.plotly_chart(fig)
del fig
gc.collect()

# Clean-up
# del df_numeric, data_imputed, data_scaled
# gc.collect()
