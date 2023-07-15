import streamlit as st
import pandas as pd


st.title('Portfolio')
left, right = st.columns([4,1])
left.selectbox('portfolio', ['All', 'USD', 'SAR'], label_visibility='collapsed')
right.button('Add Portfolio')
df = pd.DataFrame({'names': ['VTI', 'KSA'], 'Hold': [10, 12]})

st.data_editor(df, num_rows='dynamic')