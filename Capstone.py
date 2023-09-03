#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 20:42:06 2023

@author: layankaissi
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import hydralit_components as hc
from streamlit_lottie import st_lottie
import json
import numpy as np
from PIL import Image
import joblib
from sklearn.preprocessing import MinMaxScaler

# Set page configuration
st.set_page_config(
    page_title="Capstone Project",
    layout='wide'
)

# hide streamlit features
hide_streamlit_style = """
    <style>
        div[data-testid="stToolbar"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stDecoration"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stStatusWidget"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        #MainMenu {
            visibility: hidden;
            height: 0%;
        }
        header {
            visibility: hidden;
            height: 0%;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Add CSS styles and icon libraries
st.markdown("""
    <style>
    .navigation-bar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #006400; /* Dark green color code */
        padding: 20px;
        margin-bottom: 20px;
        margin-top: 250px; /* Adjust the margin top value to move the navigation bar lower */
    }
    .navigation-bar {
        display: flex;
        justify-content: space-around;
        align-items: center;
        font-size: 24px;
        color: white;
    }
    .navigation-bar-item {
        display: flex;
        align-items: center;
        cursor: pointer;
        color: white;
        margin-right: 20px;
    }
    .navigation-bar-item i {
        margin-right: 10px;
    }
    .navigation-bar-item.active {
        background-color: #2F4F4F;
        border-radius: 4px;
        padding: 4px 8px;
    }
    
 
    </style>
""", unsafe_allow_html=True)


# Add CSS styles and icon libraries
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
   
    """, unsafe_allow_html=True)
    

# Define menu data with labels and icons
menu_data = [
    {'label': 'Home', 'icon': '<i class="fa-solid fa-key" style="color: #ffffff;"></i>'},
    {'label': 'Overview', 'icon': "bi bi-globe"},
    {'label': 'Statistics', 'icon': "bi bi-bar-chart-fill"},
    {'label': 'Forecast', 'icon': "bi bi-brightness-alt-high-fill"},
    {'label': 'Agri Model', 'icon': "bi bi-boxes"},
    {'label': 'Crop Index Model', 'icon': "bi bi-sliders"},
    {'label': 'Water Stress Model', 'icon': "bi bi-droplet-fill"}
   
        ]


# Remove duplicate "Home" tab
menu_data = [item for item in menu_data if item['label'] != 'Home']


    
over_theme = {'txc_inactive': 'white', 'menu_background': 'darkblue'}
menu_label = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False,
    sticky_nav=True,
    sticky_mode='sticky'
)


# Home Page
if menu_label == 'Home':
    st.title("AgriEco Analyzer")
 
    # Create two columns with custom CSS classes
    col1, col2 = st.columns(2)
    with col1:
     st.subheader("Sustainable Agriculture Analytics: Unveiling the Interplay of Socio-economic Factors and Agricultural Variables")        
     st.markdown("""
<div style="text-align: justify;">
        <p>AgriEco Analyzer is a powerful analytics tool designed to provide crucial insights into the world of sustainable agriculture. Our app aims to unravel the intricate interplay between socio-economic factors and agricultural variables, empowering farmers, policymakers, and agricultural enthusiasts with data-driven knowledge for informed decision-making.</p>   
        <ul>
        </ul>
    </div>
""", unsafe_allow_html=True)
     
    with col2:         
     with open("/Users/apple/Desktop/agrieco.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=300, width=500)
            
  # Display a dark blue line break
    st.markdown("<hr style='border: 2px solid darkblue;'>", unsafe_allow_html=True)  
    
    col1, col2 = st.columns(2)
    with col1:
        with open("/Users/apple/Desktop/statistics.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=300, width=500)
        st.write("#### Exploratory Data Analysis") 
        st.write("""
- Visualizations
- Statistical Analysis""")
        
    with col2:
        with open("/Users/apple/Desktop/EDA.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=300, width=500)
        st.write("#### Forecasting & Predictive Models")  
        st.write("""
- SARIMA Model
- Random Forest Regression Models""")

if menu_label == "Overview":
    st.title("Agriculture's Footprint: Farming the Future")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""<div style="text-align: justify;"><p>In a world where agriculture stands as the cornerstone of sustenance and prosperity, the intricate dance between water resources and crop yield is nothing short of vital. Picture a region where life and livelihood are intertwined with the rhythm of the land, where bountiful harvests provide not only sustenance but also economic growth. Yet beneath this rustic surface lies a complex tapestry of variables: changing weather patterns, socio-economic shifts, and the delicate dance of resource allocation. As we delve into the data, we will unearth the nuances that shape not only the fields but also the lives of millions.</p>   
       <p>Driven by the spirit of the United Nations' Sustainable Development Goal (SDG) of Zero Hunger, this project aims to illuminate the connections between agriculture, socio-economic conditions, and the well-being of individuals worldwide. By delving into these complexities, we are committed to shaping a world where food security isn't just a goal, but a reality that transforms lives and propels us towards a more prosperous future for all.</p> 
       <p><strong>Problem Statement:</strong>
       How can Socio-Economic Factors influence Agricultural Sustainability and Hunger Eradication?</li>
        </ul>
    </div>""", unsafe_allow_html=True)
    
    
    with col2:
        image = Image.open("/Users/apple/Desktop/hunger.png")
        st.image(image, width=600, use_column_width=True)
        
        
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.write("")
        st.write("")
        st.write("")
        with open("/Users/apple/Desktop/soup.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=150, width=150)
    
    with col1:
        with open("/Users/apple/Desktop/water.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=150, width=150)  
        
    with col1:
        with open("/Users/apple/Desktop/agriculture.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=150, width=150)   
        
    with col1:
        with open("/Users/apple/Desktop/economy.json", "r") as f:
               lottie_json = json.load(f)
               st_lottie(lottie_json, height=150, width=150) 
               
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col2.metric("Have alarming levels of hunger", "44 Countries")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col2.metric("Die everyday from dirty water", "> 800 Children")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col2.metric("Share of agriculture in global GDP ", "4 %")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col2.metric("Projected Inflation", "6.6 %")
    
    with col3:
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       col3.metric("Global GHI Score in 2022", "18.2")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       col3.metric("Water withdrawals used by Agriculture", "72 %")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       col3.metric("Global workforce employed in Agriculture", "27 %")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       st.write("")
       col3.metric("Food price index reached new highs", "159.7")
       
    with col4:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col4.metric("Global number of undernourished people", "722 M")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col4.metric("People living without clean drinking water", "780 M")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col4.metric("Agricultural and forest land decline", "134 M Ha")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        col4.metric("People living in extreme poverty", "714 M")
        
    with col1:
      st.markdown('<a href="https://www.globalhungerindex.org/pdf/en/2022.pdf" style="text-decoration: none; color: #3366CC; font-weight: bold;">Learn more : Global Hunger Index 2022</a>', unsafe_allow_html=True)
      st.markdown('<a href="https://www.fao.org/3/cc2211en/cc2211en.pdf" style="text-decoration: none; color: #3366CC; font-weight: bold;">Learn more : World Food and Agriculture</a>', unsafe_allow_html=True)
    

if menu_label == "Statistics":
  df = pd.read_csv('/Users/apple/Desktop/Capstone_df.csv')
  st.title("Global Overview")
  viz1 = st.columns((0.3, 2, 0.3))
  with viz1[1]: 
   
    # Function to create the interactive Plotly graph object choropleth map
    def create_choropleth_map(df, variable):
       fig = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color=variable,
        animation_frame="Year",
        projection="natural earth",
        title=f"Global {variable} from 2001 to 2020",
        hover_name="Country",
        color_continuous_scale="Viridis"
    )

       fig.update_geos(showcoastlines=True, coastlinecolor="RebeccaPurple", showland=True, landcolor="LightGray", showframe=False)
         # Increase the size of the plot


       return fig

# Define the list of variables for the dropdown
    variable_options = ["Water Use (mm/day/yr) - Cropland", "Air Temp (Kelvin)", "Vapor pressure deficit VPD", "Normalized difference vegetation index NDVI"]
       
# Add a dropdown to select the variable
    selected_variable = st.selectbox("", variable_options)

# Create the choropleth map based on the selected variable
    fig = create_choropleth_map(df, selected_variable)
    fig.update_layout(autosize=False, width=920, height=520)
# Show the interactive map
    
    # Show the interactive map
    st.plotly_chart(fig)
    

  viz2 = st.columns((2,2))  # Create a layout with 2 columns and 2 rows
  # First row, first column
 # Define the list of variables for the scatter plot
  selected_variables = ['Water Use (mm/day/yr) - Cropland', 'Air Temp (Kelvin)', 'Vapor pressure deficit VPD', 'Normalized difference vegetation index NDVI']
  # Define the list of marker symbols and colors for each variable
  marker_symbols = ['circle', 'square', 'triangle-up', 'diamond']
  line_colors = ['darkblue', 'orange', 'red', 'darkgreen']

  # Add a dropdown to select the country
  selected_country = st.selectbox("", df['Country'].unique())

  # Filter the data for the selected country
  filtered_df = df[df['Country'] == selected_country]
  
  # Determine the y-axis range for each variable
  y_axis_ranges = {
    'Water Use (mm/day/yr) - Cropland': [min(filtered_df['Water Use (mm/day/yr) - Cropland']), max(filtered_df['Water Use (mm/day/yr) - Cropland'])],  # Adjust the range as needed
    'Air Temp (Kelvin)': [min(filtered_df['Air Temp (Kelvin)']), max(filtered_df['Air Temp (Kelvin)'])],
    'Vapor pressure deficit VPD': [min(filtered_df['Vapor pressure deficit VPD']), max(filtered_df['Vapor pressure deficit VPD'])],
    'Normalized difference vegetation index NDVI': [min(filtered_df['Normalized difference vegetation index NDVI']), max(filtered_df['Normalized difference vegetation index NDVI'])]
}

  # Create a layout with two columns
  col1, col2 = st.columns(2)

  # First column
  with col1:
      for i in range(2):
          var = selected_variables[i]
          fig = go.Figure()
          
          fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df[var],
                                   mode='markers+lines',
                                   name=var,
                                   marker_symbol=marker_symbols[i],
                                   line=dict(color=line_colors[i]),
                                   hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Value: %{y}<extra></extra>',
                                   text=filtered_df['Country'] + ': ' + filtered_df[var].astype(str)))
          
          fig.update_layout(title=f"{var} from 2001 to 2020 for {selected_country}",
                            xaxis_title="",
                            yaxis_title="",
                            hovermode="x unified",
                            xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=False,range=y_axis_ranges[var], dtick=0.25))
          
          fig.update_layout(autosize=False, width=460, height=520)
          
          st.plotly_chart(fig)

  # Second column
  with col2:
      for i in range(2, 4):
          var = selected_variables[i]
          fig = go.Figure()
          
          fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df[var],
                                   mode='markers+lines',
                                   name=var,
                                   marker_symbol=marker_symbols[i],
                                   line=dict(color=line_colors[i]),
                                   hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Value: %{y}<extra></extra>',
                                   text=filtered_df['Country'] + ': ' + filtered_df[var].astype(str)))
          
          fig.update_layout(title=f"{var} from 2001 to 2020 for {selected_country}",
                            xaxis_title="",
                            yaxis_title="",
                            hovermode="x unified",
                            xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=False,range=y_axis_ranges[var], dtick=0.25))
          
          fig.update_layout(autosize=False, width=500, height=520)
          
          st.plotly_chart(fig)
    
  
  
  viz3 = st.columns((0.8, 2))  
  with viz3[0]:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Select the relevant columns for the analysis
    agricultural_vars = ['Water Use (mm/day/yr) - Cropland', 'Vapor pressure deficit VPD', 'Normalized difference vegetation index NDVI']
    socio_economic_vars = ['Access to clean fuels and technologies for cooking (% of population)',
       'Access to electricity (% of population)',
       'Agricultural land (% of land area)',
       'Agriculture, forestry, and fishing, value added (% of GDP)',
       'Agriculture, forestry, and fishing, value added (annual % growth)',
       'Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)',
       'Annual freshwater withdrawals, total (% of internal resources)',
       'Arable land (% of land area)', 'Birth rate, crude (per 1,000 people)',
       'CO2 emissions (kg per PPP $ of GDP)',
       'Consumer price index (2010 = 100)',
       'Crop production index (2014-2016 = 100)',
       'Current health expenditure (% of GDP)',
       'Employment in agriculture (% of total employment) (modeled ILO estimate)',
       'Employment to population ratio, 15+, total (%) (modeled ILO estimate)',
       'Exports of goods and services (% of GDP)',
       'Fertility rate, total (births per woman)',
       'Forest area (% of land area)', 'GDP growth (annual %)',
       'GDP per capita (current US$)',
       'Individuals using the Internet (% of population)',
       'Inflation, consumer prices (annual %)',
       'Life expectancy at birth, total (years)',
       'Lifetime risk of maternal death (%)',
       'People using at least basic drinking water services (% of population)',
       'People using at least basic sanitation services (% of population)',
       'Permanent cropland (% of land area)', 'Population growth (annual %)',
       'Population, female (% of total population)',
       'Population, male (% of total population)',
       'Rural population (% of total population)',
       'Unemployment, total (% of total labor force) (modeled ILO estimate)',
       'Urban population (% of total population)',
       'Wage and salaried workers, total (% of total employment) (modeled ILO estimate)',
       'Water productivity, total (constant 2015 US$ GDP per cubic meter of total freshwater withdrawal)',
       ]

    
# Create an interactive scatter plot based on selected variables
    def create_interactive_scatter_plot(selected_country, selected_agricultural_var, selected_socio_economic_factor):
      country_data = df[df['Country'] == selected_country]
    
      scaler = MinMaxScaler()
      country_data[[selected_socio_economic_factor, selected_agricultural_var]] = scaler.fit_transform(country_data[[selected_socio_economic_factor, selected_agricultural_var]])

  
      # Create bar plot
      fig = go.Figure(data=[
        go.Bar(x=country_data['Year'], y=country_data[selected_agricultural_var], name=selected_agricultural_var, marker_color='darkblue', width=0.6),
        go.Bar(x=country_data['Year'], y=country_data[selected_socio_economic_factor], name=selected_socio_economic_factor, marker_color='lightblue', width=0.6)
    ])
      fig.update_layout(barmode='group', xaxis=dict(showgrid=False))
                        
      fig.update_layout(title=f"{selected_agricultural_var} and {selected_socio_economic_factor} for {selected_country}",
      height=400,width=1000)
      st.plotly_chart(fig)

# Main function for Streamlit app
    def main():
    # Dropdown for selecting country
     
    
    # Radio buttons for selecting agricultural variable
      selected_agricultural_var = st.radio('', agricultural_vars)
    
    # Dropdown for selecting socio-economic factor
      selected_socio_economic_factor = st.selectbox('', df[socio_economic_vars].columns, key="socio_economic_factor")
      with viz3[1]:
    # Show the interactive scatter plot
       create_interactive_scatter_plot(selected_country, selected_agricultural_var, selected_socio_economic_factor)

    if __name__ == '__main__':
      main()
      
      
  viz4 = st.columns((1))  
  with viz4[0]:   
     
      # Define a function to create the correlation heatmap
     def create_correlation_heatmap():
         correlation_matrix = pd.read_csv('/Users/apple/Desktop/Corr_MATRIX.csv')
         # Create the heatmap using Plotly Express
         fig = go.Figure(data=go.Heatmap(
                         z=correlation_matrix.values,
                         x=correlation_matrix.columns,
                         y=correlation_matrix.columns,
                         zmin=-1,
                         zmax=1, 
                         colorscale='Blues', 
                         ))
  
         # Add annotations to display correlation coefficients
         for i in range(len(correlation_matrix.columns)):
             for j in range(len(correlation_matrix.columns)):
                 fig.add_annotation(
                     x=correlation_matrix.columns[i],
                     y=correlation_matrix.columns[j],
                     text=f"{correlation_matrix.iloc[j, i]:.2f}",  # Display correlation coefficient with 2 decimal places
                     showarrow=False,
                 )
         # Update the layout for better readability
         fig.update_layout(width=1200, height=1000, title="Correlation Heatmap between Agricultural and Socio-Economic Variables")

         # Display the heatmap using Streamlit
         st.plotly_chart(fig)

     # Main Streamlit app
     def main():

         # Create a button to trigger the correlation heatmap
         if st.button("Show Correlation Heatmap"):
             create_correlation_heatmap()

     if __name__ == "__main__":
         main()    
         
  if st.button("Show Correlation Maps"):        
   viz5 = st.columns((1, 1))  
   with viz5[0]:  
             
     cluster_countries = {
    2: ['Afghanistan', 'Algeria', 'Azerbaijan', 'Bahrain', 'Belgium', 'Botswana', 'Canada', 'Chad', 'Cyprus', 'Denmark', 'Djibouti', 'Eritrea', 'Finland', 'Hungary', 'Iraq', 'Ireland', 'Israel', 'Jordan', 'Kazakhstan', 'Kuwait', 'Lebanon', 'Lesotho', 'Libya', 'Lithuania', 'Mauritania', 'Mongolia', 'Morocco', 'Namibia', 'Netherlands', 'New Zealand', 'Niger', 'Oman', 'Portugal', 'Qatar', 'Saudi Arabia', 'Senegal', 'Somalia', 'South Africa', 'Spain', 'Syrian Arab Republic', 'Tunisia', 'Turkmenistan', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Zimbabwe'],
    0: ['Albania', 'Angola', 'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Barbados', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Canada', 'Chad', 'Chile', 'China', 'Croatia', 'Cuba', 'Cyprus', 'Denmark', 'Djibouti', 'Ecuador', 'El Salvador', 'Eritrea', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lebanon', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malawi', 'Mali', 'Mexico', 'Mongolia', 'Morocco', 'Mozambique', 'Namibia', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Pakistan', 'Paraguay', 'Poland', 'Portugal', 'Puerto Rico', 'Romania', 'Senegal', 'Singapore', 'Slovenia', 'Somalia', 'South Africa', 'Sweden', 'Switzerland', 'Tajikistan', 'Turkmenistan', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Zambia', 'Zimbabwe'],
    1: ['Angola', 'Barbados', 'Belize', 'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei Darussalam', 'Burundi', 'Cameroon', 'Central African Republic', 'Colombia', 'Comoros', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Equatorial Guinea', 'Gabon', 'Ghana', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'India', 'Indonesia', 'Jamaica', 'Japan', 'Kenya', 'Latvia', 'Liberia', 'Lithuania', 'Madagascar', 'Malaysia', 'Myanmar', 'Nepal', 'Nicaragua', 'Nigeria', 'Papua New Guinea', 'Paraguay', 'Puerto Rico', 'Rwanda', 'Sierra Leone', 'Singapore', 'Sri Lanka', 'Suriname', 'Togo', 'Trinidad and Tobago', 'Uganda', 'Vietnam', 'Zambia']
    }      
             
     cluster_data = []
     for cluster_label, countries in cluster_countries.items():
         for country in countries:
             cluster_data.append({'Country': country, 'Cluster': cluster_label})

     cluster_df = pd.DataFrame(cluster_data)

     cluster_mean = {0: 2.03, 1: 3.47, 2: 1.05}  # Mean values for each cluster

     # Load a world map
     world_map = px.data.gapminder().query("year == 2007")

     # Merge cluster data with the world map data
     merged_data = world_map.merge(cluster_df, how='left', left_on='country', right_on='Country')

     # Filter out rows with null clusters
     merged_data = merged_data.dropna(subset=['Cluster'])
     
    

     # Create the scatter plot on the map
     fig1 = px.scatter_geo(merged_data,
                          locations="iso_alpha",  # ISO alpha-3 country codes
                          color=merged_data['Cluster'].map(cluster_mean),
                          color_continuous_scale=['red', 'blue'],  # Adjust color scale
                          hover_data=["country", "Cluster"],
                          projection="natural earth",
                          title="Countries Clustered by Water Use",
                          color_continuous_midpoint=2.0  # Set midpoint for color scale
                          )

     # Update layout to adjust figure size, remove border, and set custom color scale
     fig1.update_layout(geo=dict(showcoastlines=True, coastlinecolor="RebeccaPurple", showland=True, landcolor="LightGray", showframe=False),
                       coloraxis_colorbar=dict(title="", tickvals=[0,1, 2, 3,4], ticktext=["0", "1", "2", "3", "4"]))

     # Show the scatter plot on the map using Streamlit

     st.plotly_chart(fig1, use_container_width=True)    
      
   with viz5[1]:  
              
      cluster_countries = {
     0: ['Afghanistan', 'Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Canada', 'Chile', 'China', 'Croatia', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Japan', 'Kazakhstan', 'Latvia', 'Lebanon', 'Lesotho', 'Lithuania', 'Luxembourg', 'Mongolia', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Romania', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Tajikistan', 'Ukraine', 'United Kingdom', 'United States', 'Uzbekistan'],
     1: ['Angola', 'Bahrain', 'Barbados', 'Belize', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Burkina Faso', 'Cameroon', 'Central African Republic', 'Chad', 'Colombia', 'Comoros', 'Cuba', 'Djibouti', 'Dominican Republic', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Gabon', 'Ghana', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'India', 'Indonesia', 'Iraq', 'Jamaica', 'Kuwait', 'Liberia', 'Madagascar', 'Malaysia', 'Mali', 'Mauritania', 'Mozambique', 'Myanmar', 'Namibia', 'Nicaragua', 'Niger', 'Nigeria', 'Oman', 'Pakistan', 'Papua New Guinea', 'Paraguay', 'Puerto Rico', 'Qatar', 'Saudi Arabia', 'Senegal', 'Sierra Leone', 'Singapore', 'Somalia', 'Sri Lanka', 'Suriname', 'Togo', 'Trinidad and Tobago', 'Uganda', 'United Arab Emirates', 'Vietnam'],
     2: ['Algeria', 'Angola', 'Argentina', 'Botswana', 'Burundi', 'Cyprus', 'Ecuador', 'Ethiopia', 'Greece', 'Honduras', 'Iraq', 'Israel', 'Italy', 'Jordan', 'Kenya', 'Lebanon', 'Lesotho', 'Libya', 'Madagascar', 'Malawi', 'Mexico', 'Morocco', 'Namibia', 'Nepal', 'Papua New Guinea', 'Portugal', 'Rwanda', 'South Africa', 'Spain', 'Syrian Arab Republic', 'Tunisia', 'Turkmenistan', 'Uganda', 'Uruguay', 'Uzbekistan', 'Zambia', 'Zimbabwe']
        }              
      cluster_data = []
      for cluster_label, countries in cluster_countries.items():
          for country in countries:
              cluster_data.append({'Country': country, 'Cluster': cluster_label})

      cluster_df = pd.DataFrame(cluster_data)

      cluster_mean = {0: 283.08, 1: 298.94, 2: 292.48}  # Mean values for each cluster

      # Load a world map
      world_map = px.data.gapminder().query("year == 2007")

      # Merge cluster data with the world map data
      merged_data = world_map.merge(cluster_df, how='left', left_on='country', right_on='Country')

      # Filter out rows with null clusters
      merged_data = merged_data.dropna(subset=['Cluster'])
      
      

      # Create the scatter plot on the map
      fig2 = px.scatter_geo(merged_data,
                           locations="iso_alpha",  # ISO alpha-3 country codes
                           color=merged_data['Cluster'].map(cluster_mean),
                           color_continuous_scale=['blue', 'yellow'],  # Adjust color scale
                           hover_data=["country", "Cluster"],
                           projection="natural earth",
                           title="Countries Clustered by Air temperature",
                           color_continuous_midpoint=292  # Set midpoint for color scale
                           )

      # Update layout to adjust figure size, remove border, and set custom color scale
      fig2.update_layout(geo=dict(showcoastlines=True, coastlinecolor="RebeccaPurple", showland=True, landcolor="LightGray", showframe=False),
                        coloraxis_colorbar=dict(title="", tickvals=[283, 292, 298], ticktext=['283', '292', '298']))


      # Show the scatter plot on the map using Streamlit
      st.plotly_chart(fig2)   
      
      
   viz6 = st.columns((1, 1))  
   with viz6[0]:  
                
        cluster_countries = {
       0: ['Afghanistan', 'Algeria', 'Angola', 'Argentina', 'Bahrain', 'Barbados', 'Belize', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Burundi', 'Cameroon', 'Central African Republic', 'Cuba', 'Cyprus', 'Djibouti', 'Dominican Republic', 'El Salvador', 'Eritrea', 'Ethiopia', 'Ghana', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Haiti', 'India', 'Israel', 'Jamaica', 'Jordan', 'Kenya', 'Lebanon', 'Lesotho', 'Libya', 'Malawi', 'Mexico', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Oman', 'Pakistan', 'Paraguay', 'Portugal', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Syrian Arab Republic', 'Tajikistan', 'Togo', 'Tunisia', 'Turkmenistan', 'Uganda', 'Uzbekistan', 'Zambia', 'Zimbabwe'],
       1: ['Albania', 'Algeria', 'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burundi', 'Canada', 'Chile', 'China', 'Colombia', 'Comoros', 'Croatia', 'Cuba', 'Cyprus', 'Denmark', 'Dominican Republic', 'Ecuador', 'Equatorial Guinea', 'Estonia', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Greece', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Indonesia', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Mongolia', 'Morocco', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Norway', 'Papua New Guinea', 'Poland', 'Portugal', 'Puerto Rico', 'Romania', 'Rwanda', 'Sierra Leone', 'Singapore', 'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland', 'Trinidad and Tobago', 'Uganda', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay', 'Vietnam'],
       2: ['Botswana', 'Burkina Faso', 'Central African Republic', 'Chad', 'Djibouti', 'Eritrea', 'Iraq', 'Kuwait', 'Mali', 'Mauritania', 'Namibia', 'Niger', 'Nigeria', 'Oman', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Senegal', 'United Arab Emirates']
          }              
        cluster_data = []
        for cluster_label, countries in cluster_countries.items():
            for country in countries:
                cluster_data.append({'Country': country, 'Cluster': cluster_label})

        cluster_df = pd.DataFrame(cluster_data)

        cluster_mean = {0: 1.13, 1: 0.51, 2: 2.28}  # Mean values for each cluster

        # Load a world map
        world_map = px.data.gapminder().query("year == 2007")

        # Merge cluster data with the world map data
        merged_data = world_map.merge(cluster_df, how='left', left_on='country', right_on='Country')

        # Filter out rows with null clusters
        merged_data = merged_data.dropna(subset=['Cluster'])
        
        

        # Create the scatter plot on the map
        fig3 = px.scatter_geo(merged_data,
                             locations="iso_alpha",  # ISO alpha-3 country codes
                             color=merged_data['Cluster'].map(cluster_mean),
                             color_continuous_scale=['blue', 'red'],  # Adjust color scale
                             hover_data=["country", "Cluster"],
                             projection="natural earth",
                             title="Countries Clustered by Vapor pressure deficit VPD",
                             color_continuous_midpoint=1  # Set midpoint for color scale
                             )

        # Update layout to adjust figure size, remove border, and set custom color scale
        fig3.update_layout(geo=dict(showcoastlines=True, coastlinecolor="RebeccaPurple", showland=True, landcolor="LightGray", showframe=False),
                          coloraxis_colorbar=dict(title="", tickvals=[0.5,1,1.5,2], ticktext=['0.5','1','1.5','2']))


        # Show the scatter plot on the map using Streamlit
        st.plotly_chart(fig3, use_container_width=True)     
        
        
   with viz6[1]:  
                  
          cluster_countries = {
         0: ['Albania', 'Angola', 'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Benin', 'Bosnia and Herzegovina', 'Botswana', 'Bulgaria', 'Cameroon', 'Central African Republic', 'China', 'Croatia', 'Cyprus', 'Denmark', 'Djibouti', 'Ecuador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guyana', 'Hungary', 'India', 'Israel', 'Italy', 'Japan', 'Kenya', 'Latvia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Malawi', 'Mexico', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Nigeria', 'Norway', 'Pakistan', 'Poland', 'Portugal', 'Romania', 'Rwanda', 'Singapore', 'Slovenia', 'Somalia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Togo', 'Ukraine', 'United Kingdom', 'United States', 'Vietnam', 'Zambia', 'Zimbabwe'],
         1: ['Afghanistan', 'Algeria', 'Armenia', 'Bahrain', 'Botswana', 'Burkina Faso', 'Canada', 'Chad', 'Cyprus', 'Djibouti', 'Eritrea', 'Estonia', 'Iraq', 'Israel', 'Jordan', 'Kazakhstan', 'Kuwait', 'Lebanon', 'Lesotho', 'Libya', 'Mali', 'Mauritania', 'Mongolia', 'Morocco', 'Namibia', 'Niger', 'Nigeria', 'Oman', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Senegal', 'Somalia', 'Spain', 'Syrian Arab Republic', 'Tajikistan', 'Tunisia', 'Turkmenistan', 'Ukraine', 'United Arab Emirates', 'Uzbekistan'],
         2: ['Albania', 'Argentina', 'Austria', 'Barbados', 'Belgium', 'Belize', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei Darussalam', 'Burundi', 'Central African Republic', 'Chile', 'Colombia', 'Comoros', 'Croatia', 'Cuba', 'Denmark', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Equatorial Guinea', 'Finland', 'France', 'Gabon', 'Germany', 'Ghana', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Indonesia', 'Ireland', 'Italy', 'Jamaica', 'Kenya', 'Latvia', 'Liberia', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malaysia', 'Mozambique', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Norway', 'Papua New Guinea', 'Paraguay', 'Poland', 'Puerto Rico', 'Rwanda', 'Sierra Leone', 'Singapore', 'Slovenia', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland', 'Trinidad and Tobago', 'Uganda', 'United Kingdom', 'Uruguay', 'Vietnam']
            }              
          cluster_data = []
          for cluster_label, countries in cluster_countries.items():
              for country in countries:
                  cluster_data.append({'Country': country, 'Cluster': cluster_label})

          cluster_df = pd.DataFrame(cluster_data)

          cluster_mean = {0: 0.46, 1: 0.27, 2: 0.62}  # Mean values for each cluster

          # Load a world map
          world_map = px.data.gapminder().query("year == 2007")

          # Merge cluster data with the world map data
          merged_data = world_map.merge(cluster_df, how='left', left_on='country', right_on='Country')

          # Filter out rows with null clusters
          merged_data = merged_data.dropna(subset=['Cluster'])
          
          

          # Create the scatter plot on the map
          fig4 = px.scatter_geo(merged_data,
                               locations="iso_alpha",  # ISO alpha-3 country codes
                               color=merged_data['Cluster'].map(cluster_mean),
                               color_continuous_scale=['blue', 'darkgreen'],  # Adjust color scale
                               hover_data=["country", "Cluster"],
                               projection="natural earth",
                               title="Countries Clustered by Normalized difference vegetation index NDVI",
                               color_continuous_midpoint=0.3  # Set midpoint for color scale
                               )

          # Update layout to adjust figure size, remove border, and set custom color scale
          fig4.update_layout(geo=dict(showcoastlines=True, coastlinecolor="RebeccaPurple", showland=True, landcolor="LightGray", showframe=False),
                            coloraxis_colorbar=dict(title="", tickvals=[0.1,0.3,0.6], ticktext=['0.1','0.3','0.6']))


          # Show the scatter plot on the map using Streamlit
          st.plotly_chart(fig4)          
    
if menu_label == "Crop Index Model":

       df = pd.read_csv('/Users/apple/Desktop/Crop_Model_df.csv')
       
      # Load the saved model
       rf_model_crop = joblib.load('/Users/apple/Desktop/rf_model_CROP.joblib')
       
       feature_importances = rf_model_crop.feature_importances_
            

# Streamlit app
       st.title('Crop Production Index Prediction')
       st.sidebar.header('Adjust Input Features')
       
       # Get feature importances
       selected_features = df.columns
       
       # Get the top 10 features by importance
       top_feature_indices = feature_importances.argsort()[::-1][:10]
       top_features = selected_features[top_feature_indices]

       input_values = {}
       # Create input sliders for selected features
       for feature in top_features:
         if feature == 'Air Temp (Kelvin)':
        # Set the max value to a higher value than 100
           input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=df['Air Temp (Kelvin)'].max())
         elif feature =='GDP per capita (current US$)':
            input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=df['GDP per capita (current US$)'].max())
    
         else:
           input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=100.0)

       crop_production_prediction = np.array([0.00])
       
       # Create a "Predict" button
       if st.sidebar.button('Predict'):   
         
           input_df = pd.DataFrame([input_values], columns=top_features)
      
           crop_production_prediction = rf_model_crop.predict(input_df)
              

# Display prediction and input values
       prediction_text = f"<h3 style='display: inline; color: darkblue;'>Predicted Crop Production Index: {crop_production_prediction[0]:.2f}</h3>"
       st.markdown(prediction_text, unsafe_allow_html=True)



# Create a summary table with input values and prediction
       summary_data = {'Input Feature': list(input_values.keys()), 'Value': list(input_values.values())}
       summary_data['Input Feature'].append('Predicted Crop Production Index')
       summary_data['Value'].append(crop_production_prediction[0])
       summary_df = pd.DataFrame(summary_data)
 
       st.write('#### Summary Table')
       st.write(summary_df)  

        # Create a horizontal bar chart for feature importances
       if st.button('Feature Importance Scores'):
        
           feature_importance_df = pd.read_csv('/Users/apple/Desktop/selected_feature_importances_crop.csv')
           feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=True)

           fig_feature_importance = px.bar(feature_importance_df, x='Importance', y='Feature', orientation='h',
                                        title='', labels={'Importance': ''})

           fig_feature_importance.update_traces(marker_color='darkblue', texttemplate='%{x:.2f}', textposition='outside')
           fig_feature_importance.update_layout(xaxis_title='', yaxis_title='', xaxis=dict(showgrid=False, tickvals=[]), autosize=False,  # Disable automatic resizing
    width=800,       # Set the width of the plot to your preferred value
    height=400     )
        
           st.plotly_chart(fig_feature_importance, use_column_width=True)
           
         # Create a button to trigger the display of evaluation metrics
       if st.button('Evaluation Metrics'):
           r_squared = 0.7964976676149953
           mean_absolute_error = 6.765787318982373
           root_mean_squared_error = 9.680757032587229

        # Display the evaluation metrics with two decimal places
           st.write(f"R-squared: {r_squared:.2f}")
           st.write(f"Mean Absolute Error: {mean_absolute_error:.2f}")
           st.write(f"Root Mean Squared Error: {root_mean_squared_error:.2f}")
      
if menu_label == "Water Stress Model":      
       df = pd.read_csv('/Users/apple/Desktop/Water_Model_df.csv')
     # Load the saved model
       rf_model_waterstress = joblib.load('/Users/apple/Desktop/new_rf_model_water.joblib')
       scaler = joblib.load('/Users/apple/Desktop/scaler_model_water.joblib')
# Streamlit app
       st.title('Water Stress Prediction')
       st.sidebar.header('Adjust Input Features')
       

       feature_importances = rf_model_waterstress.feature_importances_
       # Get feature importances
       selected_features = df.columns
       
       # Get the top 10 features by importance
       top_feature_indices = feature_importances.argsort()[::-1][:12]
       top_features = selected_features[top_feature_indices]


       # Create input sliders for selected features
       input_values = {}
       for feature in top_features:
          if feature =='GDP per capita (current US$)':
              input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=df['GDP per capita (current US$)'].max())
      
          else:
              input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=100.0)

        # Initialize the initial predicted water stress value
       water_stress_prediction = np.array([0.00])
     
        
      # Create a "Predict" button
       if st.sidebar.button('Predict'):   
        
         input_df = pd.DataFrame([input_values], columns=top_features)
        
         water_stress_prediction = rf_model_waterstress.predict(input_df)
        

# Display prediction and input values
       st.markdown(f"<h3 style='text-align: left; color: darkblue;'>Predicted Water Stress: {water_stress_prediction[0]:.2f}</h3>", unsafe_allow_html=True)

      # Determine the alert message and color based on predicted value
       alert_message = ""
       alert_color = ""
       if water_stress_prediction[0] < 10:
          alert_message = "Low Stress (< 10%)"
          alert_color = "gray"
       elif 10 <= water_stress_prediction[0] < 20:
         alert_message = "Low to Medium Stress (10-20%)"
         alert_color = "darkyellow"
       elif 20 <= water_stress_prediction[0] < 40:
         alert_message = "Medium to High Stress (20-40%)"
         alert_color = "orange"
       elif 40 <= water_stress_prediction[0] < 80:
         alert_message = "High Stress (40-80%)"
         alert_color = "red"
       else:
         alert_message = "Extremely High Stress (> 80%)"
         alert_color = "darkred"

# Display the alert message in the specified color
       alert_text = f"<h3 style='background-color: {alert_color}; padding: 10px; color: white;'>{alert_message}</h3>"
       st.markdown(alert_text, unsafe_allow_html=True)

# Create a summary table with input values and prediction
       summary_data = {'Input Feature': list(input_values.keys()), 'Value': list(input_values.values())}
       summary_data['Input Feature'].append('Predicted Water Stress')
       summary_data['Value'].append(water_stress_prediction[0])
       summary_df = pd.DataFrame(summary_data)

       st.write('#### Summary Table')
       st.write(summary_df)
       
       if st.button('Feature Importance Scores'):
      
         feature_importance_df = pd.read_csv('/Users/apple/Desktop/selected_feature_importances_water.csv')
         feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=True)

         fig_feature_importance = px.bar(feature_importance_df, x='Importance', y='Feature', orientation='h',
                                      title='', labels={'Importance': ''})

         fig_feature_importance.update_traces(marker_color='darkblue', texttemplate='%{x:.4f}', textposition='outside')
         fig_feature_importance.update_layout(xaxis_title='', yaxis_title='', xaxis=dict(showgrid=False, tickvals=[]),autosize=False,  # Disable automatic resizing
                            width=900,       # Set the width of the plot to your preferred value
                           height=400   )
      
         st.plotly_chart(fig_feature_importance)
         
       # Create a button to trigger the display of evaluation metrics
       if st.button('Evaluation Metrics'):
         r_squared = 0.9947271654606119
         mean_absolute_error = 8.059529503965676
         root_mean_squared_error = 31.831932354800326

      # Display the evaluation metrics with two decimal places
         st.write(f"R-squared: {r_squared:.2f}")
         st.write(f"Mean Absolute Error: {mean_absolute_error:.2f}")
         st.write(f"Root Mean Squared Error: {root_mean_squared_error:.2f}")

    
if menu_label == "Agri Model":   
    df = pd.read_csv('/Users/apple/Desktop/Agri_df.csv')
    rf_model_agri = joblib.load('/Users/apple/Desktop/new_rf_model_agri.joblib')
    sfm_model = joblib.load('/Users/apple/Desktop/new_sfm_model_agri.joblib')
    
    feature_importances = rf_model_agri.feature_importances_
    
    # Streamlit app
    st.title('Agri Prediction')
    st.sidebar.header('Adjust Input Features')
    
    # Get feature importances
    selected_features = df.columns
    
    # Get the top 10 features by importance
    top_feature_indices = feature_importances.argsort()[::-1][:11]
    top_features = selected_features[top_feature_indices]


    # Create input sliders for selected features
    input_values = {}
    for feature in top_features:
       input_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=100.0)

            # Initialize the initial predicted water stress value
    agri_prediction = np.zeros(4)
         
            
    # Create a "Predict" button
    if st.sidebar.button('Predict'):   
      
         input_df = pd.DataFrame([input_values], columns=top_features)
                
         agri_prediction = rf_model_agri.predict(input_df)[0]

    # Display predictions and input values for each target variable
    target_variables = ['Water Use (mm/day/yr) - Cropland']
        
    for target_var, prediction in zip(target_variables, agri_prediction):
          st.markdown(f"<h3 style='text-align: left; color: darkblue;'>Predicted {target_var}: {prediction:.2f}</h3>", unsafe_allow_html=True)
         
    summary_data = {'Input Feature': list(input_values.keys()), 'Value': list(input_values.values())}

# Iterate over target variables and append predicted values to summary_data
    for target_var, prediction in zip(target_variables, agri_prediction):
       summary_data['Input Feature'].append(f'Predicted {target_var}')
       summary_data['Value'].append(prediction)

# Create a DataFrame from the updated summary_data
    summary_df = pd.DataFrame(summary_data)
    
    st.write('#### Summary Table')
    st.write(summary_df)
    
    # Create a horizontal bar chart for feature importances
    if st.button('Feature Importance Scores'):
    
       feature_importance_df = pd.read_csv('/Users/apple/Desktop/selected_feature_importances_agri.csv')
       feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=True)

       fig_feature_importance = px.bar(feature_importance_df, x='Importance', y='Feature', orientation='h',
                                    title='', labels={'Importance': ''})

       fig_feature_importance.update_traces(marker_color='darkblue', texttemplate='%{x:.3f}', textposition='outside')
       fig_feature_importance.update_layout(xaxis_title='', yaxis_title='', xaxis=dict(showgrid=False, tickvals=[]),autosize=False,  # Disable automatic resizing
                          width=800,       # Set the width of the plot to your preferred value
                         height=400   )
    
       st.plotly_chart(fig_feature_importance)
       
     # Create a button to trigger the display of evaluation metrics
    if st.button('Evaluation Metrics'):
       r_squared = 0.9735509883269858
       mean_absolute_error = 0.19006829745596932
       root_mean_squared_error = 0.4553575083610067

    # Display the evaluation metrics with two decimal places
       st.write(f"R-squared: {r_squared:.2f}")
       st.write(f"Mean Absolute Error: {mean_absolute_error:.2f}")
       st.write(f"Root Mean Squared Error: {root_mean_squared_error:.2f}")
       
       
       
       
if menu_label == "Forecast":
   st.title("Patterns and Projections")
   col1, col2 = st.columns(2)
   with col1:
    st.markdown("""
<div style="text-align: justify;">
        <p>Click the 'Forecast' button to access predictive analytics for key agriculture indicators. Uncover potential trends and projections based on historical data and advanced modeling techniques.</p>   
        <ul>
        </ul>
    </div>
""", unsafe_allow_html=True)   
   with col2:  
    
    with open("/Users/apple/Desktop/analytics.json", "r") as f:
           lottie_json = json.load(f)
           st_lottie(lottie_json, height=400, width=600)
   with col1:
    st.empty()   
    st.empty()
    st.empty()
    st.write("")
    st.write("")
    st.write("")
    
    df = pd.read_csv('/Users/apple/Desktop/New_Forecasting.csv')
    
   # Create a selectbox to choose the country
    countries_list = df['Country'].unique()
    selected_country = st.selectbox('', countries_list)

# Filter data for the selected country and years 2001 to 2022
    selected_data = df[(df['Country'] == selected_country) & (df['Year'].between(2001, 2022))]

# Set the size of the plots
    plot_height = 400
    plot_width = 900

# Plot for 'Water Use (mm/day/yr) - Cropland'
    fig_water_use = px.line(selected_data, x='Year', y='Water Use (mm/day/yr) - Cropland',
                        labels={'': ''}, title=f'{selected_country} - Water Use (mm/day/yr) - Cropland')
    fig_water_use.update_traces(line=dict(color='darkblue'))

# Plot for 'Air Temp (Kelvin)'
    fig_air_temp = px.line(selected_data, x='Year', y='Air Temp (Kelvin)',
                       labels={'': ''}, title=f'{selected_country} - Air Temp (Kelvin)')
    fig_air_temp.update_traces(line=dict(color='darkblue'))

# Plot for 'Vapor pressure deficit VPD'
    fig_vpd = px.line(selected_data, x='Year', y='Vapor pressure deficit VPD',
                  labels={'': ''}, title=f'{selected_country} - Vapor pressure deficit VPD')
    fig_vpd.update_traces(line=dict(color='darkblue'))

# Plot for 'Normalized difference vegetation index NDVI'
    fig_ndvi = px.line(selected_data, x='Year', y='Normalized difference vegetation index NDVI',
                   labels={'': ''}, title=f'{selected_country} - Normalized difference vegetation index NDVI')
    fig_ndvi.update_traces(line=dict(color='darkblue'))

# Add the "Forecast" button
    if st.button('Forecast'):
     # Select the forecast data for the years 2023 to 2031
      forecast_data = df[(df['Country'] == selected_country) & (df['Year'].between(2022, 2025))]


    # Plot forecast data as dashed red lines
      fig_water_use.add_trace(go.Scatter(x=forecast_data['Year'], y=forecast_data['Water Use (mm/day/yr) - Cropland'],
                                       mode='lines', line=dict(color='red', dash='dash'),
                                       name='Water Use (mm/day/yr) - Cropland Forecast'))

      fig_air_temp.add_trace(go.Scatter(x=forecast_data['Year'], y=forecast_data['Air Temp (Kelvin)'],
                                      mode='lines', line=dict(color='red', dash='dash'),
                                      name='Air Temp (Kelvin) Forecast'))

      fig_vpd.add_trace(go.Scatter(x=forecast_data['Year'], y=forecast_data['Vapor pressure deficit VPD'],
                                 mode='lines', line=dict(color='red', dash='dash'),
                                 name='Vapor pressure deficit VPD Forecast'))

      fig_ndvi.add_trace(go.Scatter(x=forecast_data['Year'], y=forecast_data['Normalized difference vegetation index NDVI'],
                                  mode='lines', line=dict(color='red', dash='dash'),
                                  name='NDVI Forecast'))
      
      # Update layout for all plots
    fig_water_use.update_layout(height=plot_height, width=plot_width, xaxis=dict(showgrid=False), yaxis=dict(showgrid=False),xaxis_title='', yaxis_title='')
    fig_air_temp.update_layout(height=plot_height, width=plot_width,xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), xaxis_title='', yaxis_title='')
    fig_vpd.update_layout(height=plot_height, width=plot_width,xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), xaxis_title='', yaxis_title='')
    fig_ndvi.update_layout(height=plot_height, width=plot_width,xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), xaxis_title='', yaxis_title='')

# Show the plots in Streamlit
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.plotly_chart(fig_water_use)
    st.plotly_chart(fig_air_temp)
    st.plotly_chart(fig_vpd)
    st.plotly_chart(fig_ndvi)
      
       
       
       