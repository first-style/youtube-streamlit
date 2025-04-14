import streamlit as st
import numpy as up
import pandas as pd

st.title('Streamlit Study')

st.write('DataFrame')

df = pd.DataFrame({
        '1列目': [1, 2, 3, 4],
        '2列目': [10, 20, 30, 40],

})