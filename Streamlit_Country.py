import streamlit as st
import pandas as pd
import numpy as np
import time

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
        
        # Update the content of the container with the map
        st.map(df,
            latitude='col1',
            longitude='col2',
            size='col3',
            color='col4')
        time.sleep(3)
        
    
