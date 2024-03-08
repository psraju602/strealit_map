import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

# Create a container to hold the map
map_container = st.empty()

for seconds in range(200):
    with map_container.container():
        

        df = pd.DataFrame({
            "col1": np.random.randn(1000) / 50 + 37.76,
            "col2": np.random.randn(1000) / 50 + -122.4,
            "col3": np.random.randn(1000) * 100,
            "col4": np.random.rand(1000, 4).tolist()
        })
    
        fig_col1= st.columns(1)
        with fig_col1:
            '''
            data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
 
            fig = px.choropleth(data, locations='iso_alpha', color='gdpPercap', hover_name='country',
                                projection='natural earth', title='GDP per Capita by Country')
            st.write(fig)
            '''
            st.markdown("### First Chart")
            # Update the content of the container with the map
            fig = map(df,
              latitude='col1',
              longitude='col2',
              size='col3',
              color='col4')
            st.write(fig)
            
             
 
        time.sleep(1)
        
    
