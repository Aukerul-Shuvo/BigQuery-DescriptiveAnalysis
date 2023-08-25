import streamlit as st
import pandas as pd
import plotly.graph_objs as go

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
def main():
    # List of tables and results directory (same as the Dash app)
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
    observations_dict = {
    "co_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a very strong positive correlation of approximately 0.999. This suggests that the number of observations and the percentage of observations are almost identical.",
            "arithmetic_mean and aqi have a strong positive correlation of approximately 0.944. This indicates that as the arithmetic mean of CO values increases, the AQI (Air Quality Index) generally increases.",
            "first_max_value and aqi have an exceptionally strong positive correlation of approximately 0.999. This suggests that the maximum daily CO value is nearly always aligned with the AQI value for CO."
        ],
        "Low Correlations": [
            "poc and latitude have a correlation of -0.043.",
            "poc and longitude have a correlation of -0.065.",
            "latitude and longitude have a correlation of 0.012."
        ]
    },
    "hap_daily_summary": {
        "High Correlations": [
            "arithmetic_mean and first_max_value have a strong positive correlation of approximately 0.964. This indicates that the average daily value for HAP (Hazardous Air Pollutants) tends to align closely with its maximum daily value."
        ],
        "Low Correlations": [
            "poc and latitude have a correlation of 0.006.",
            "poc and longitude have a correlation of -0.005.",
            "latitude and longitude have a correlation of -0.025."
        ]
    },
    "lead_daily_summary": {
        "High Correlations": [
            "Interestingly, there are no exceptionally high correlations (i.e., close to 1 or -1) in the lead_df dataset."
        ],
        "Low Correlations": [
            "poc and latitude have a correlation of -0.089.",
            "poc and arithmetic_mean have a correlation of -0.045.",
            "latitude and arithmetic_mean have a correlation of 0.050.",
            "longitude and arithmetic_mean have a correlation of -0.006."
        ]
    },
    "no2_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.913.",
            "arithmetic_mean and aqi have a correlation of approximately 0.916.",
            "first_max_value and aqi have a correlation of approximately 0.995."
        ],
        "Low Correlations": [
            "poc with latitude, longitude, observation_count, and arithmetic_mean show low correlations."
            # ... other low correlation observations
        ]
    },
    "nonoxnoy_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.999."
        ],
        "Low Correlations": [
            "poc with latitude, longitude, observation_count, and others show low correlations."
            # ... other low correlation observations
        ]
    },
    "o3_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.998."
        ],
        "Low Correlations": [
            "poc with latitude, longitude, observation_count, and others show low correlations."
            # ... other low correlation observations
        ]
    },
    "pm10_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have correlations close to 1 in all three datasets.",
            "arithmetic_mean and first_max_value also have correlations close to 1."
        ],
        "Low Correlations": [
            "numerous variable pairs exhibit low correlations in these datasets."
            # ... other low correlation observations
        ]
    },
    "pm25_frm_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have correlations close to 1 in all three datasets.",
            "arithmetic_mean and first_max_value also have correlations close to 1."
        ],
        "Low Correlations": [
            "numerous variable pairs exhibit low correlations in these datasets."
            # ... other low correlation observations
        ]
    },
    "pm25_nonfrm_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have correlations close to 1 in all three datasets.",
            "arithmetic_mean and first_max_value also have correlations close to 1."
        ],
        "Low Correlations": [
            "numerous variable pairs exhibit low correlations in these datasets."
            # ... other low correlation observations
        ]
    },
    "pressure_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.999."
        ],
        "Low Correlations": [
            "numerous low correlations were observed, similar to other datasets."
            # ... other low correlation observations
        ]
    },
    "rh_and_dp_daily_summary": {
        "High Correlations": [
            "observation_count and method_code have a very strong negative correlation of approximately -0.954.",
        ],
        "Low Correlations": [
            "numerous variable pairs, such as poc with latitude, longitude, observation_count, observation_percent, and others, show low correlations."
            # ... other low correlation observations
        ]
    },
    "so2_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.917."
        ],
        "Low Correlations": [
            "many variable pairs, such as poc with latitude, longitude, observation_count, observation_percent, and others, exhibit low correlations."
            # ... other low correlation observations
        ]
    },
    "temperature_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.917."
        ],
        "Low Correlations": [
            "numerous variable pairs, like poc with latitude, longitude, observation_count, and others, show low correlations."
            # ... other low correlation observations
        ]
    },
    "wind_daily_summary": {
        "High Correlations": [
            "observation_count and observation_percent have a correlation of approximately 0.999.",
            "arithmetic_mean and first_max_value have a correlation of approximately 0.940."
        ],
        "Low Correlations": [
            "many variable pairs, such as poc with latitude, longitude, observation_count, and others, exhibit low correlations."
            # ... other low correlation observations
        ]
    }
    }

    results_dir = r"correlation-analysis-results"

    # UI Components
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
            <strong>Correlation Analysis</strong> 
        </div>
        """, unsafe_allow_html=True)

    selected_table = st.selectbox('Select a Table:', tables)

    # Displaying the Correlation Heatmap based on the selected table
    corr_data = pd.read_csv(f"{results_dir}/{selected_table}_corr.csv", index_col=0)

    fig = go.Figure(data=go.Heatmap(
        z=corr_data.values,
        x=corr_data.columns,
        y=corr_data.index,
        colorscale='Viridis',
        hoverongaps=False,
        hoverinfo='x+y+z'
    ))

    fig.update_layout(
        title=f'{selected_table}',
        title_font_size=20,
        title_font_family='Times New Roman',
        xaxis_tickfont_family='Times New Roman',
        yaxis_tickfont_family='Times New Roman',
        xaxis_tickfont_size=12,
        yaxis_tickfont_size=12,
        xaxis_tickfont_color='#ffffff',
        yaxis_tickfont_color='#ffffff',
        coloraxis_colorbar_tickfont_family='Times New Roman',
        coloraxis_colorbar_tickfont_size=12,
        coloraxis_colorbar_tickfont_color='#000000',
        coloraxis_colorbar_title_font_color='#000000',
        width=700,
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),  # Add some margins for better alignment
        title_x=0.5,  # Center the title
    )

    # Display the centered figure
    st.plotly_chart(fig)

    # Displaying observations for the selected table after the heatmap
    # Displaying observations for the selected table after the heatmap
    if selected_table in observations_dict:
        st.markdown(
        """
        
            <!-- High Correlations -->
            <div style='background-color: #142D55; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                <h3 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>🔺 High Correlations</h3>
            
        """, unsafe_allow_html=True)
        
        for observation in observations_dict[selected_table]["High Correlations"]:
            st.markdown(f"<div style='margin-left: 20px;'>🔵 {observation}</div>", unsafe_allow_html=True)

        # A small space between sections
        st.write("")

        st.markdown(
        """
            <!-- Low Correlations -->
            <div style='background-color: #D64541; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                <h3 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>🔻 Low Correlations</h3>
            </div>
        """, unsafe_allow_html=True)
        
        for observation in observations_dict[selected_table]["Low Correlations"]:
            st.markdown(f"<div style='margin-left: 20px;'>🔴 {observation}</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)  # Closing div of the main container


if __name__ == "__main__":
    main()
