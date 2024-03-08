import streamlit as st
import pandas as pd
import numpy as np

i=1
while i<=10:
    df = pd.DataFrame({
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist()
    })


    st.map(df,
        latitude='col1',
        longitude='col2',
        size='col3',
        color='col4')
    i = i+1
