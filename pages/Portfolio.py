import streamlit as st
import pandas as pd


st.title('Portfolio')
st.selectbox('portfolio'. ['All', 'USD', 'SAR'])
df = pd.DataFrame({'names': ['VTI', 'KSA'], 'Hold': [10, 12]})

st.data_editor(df, num_rows='dynamic')