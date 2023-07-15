import streamlit as st
import pandas as pd


df = pd.DataFrame({'names': ['VTI', 'KSA'], 'Hold': [10, 12]})

st.data_editor(df, num_rows='dynamic')