import streamlit as st
import leafmap.foliumap as leafmap

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

with open("custom.css") as f:
    custom_css = f.read()


# Customize the sidebar
markdown = """
GitHub Repository: <https://github.com/Aukerul-Shuvo/BigQuery-DescriptiveAnalysis>
"""

# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# # st.sidebar.image(logo)
# # st.sidebar.image(logo)

# Customize page title
#Image in center alignment
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


# Use columns to mimic the flex layout
col1, col2 = st.columns(2)

box_style = """
    text-align: center;
    font-family: Times New Roman;
    border: 1px solid #7289DA;
    border-radius: 8px;
    padding: 10px 0;
"""

# First column content
with col1:
    st.markdown(f"""
    <div style='{box_style}'>
        <strong>Student's Name:</strong> <a href="https://www.linkedin.com/in/aukerul-moin-shuvo">Md. Aukerul Moin Shuvo</a>
    </div>
    """, unsafe_allow_html=True)

# Second column content
with col2:
    st.markdown(f"""
    <div style='{box_style}'>
        <strong>Supervised by:</strong> <a href="https://www.cse.ruet.ac.bd/dr.almamun">Prof. Dr. Md. Al Mamun</a>
    </div>
    """, unsafe_allow_html=True)
