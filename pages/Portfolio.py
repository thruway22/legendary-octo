import streamlit as st
import pandas as pd


st.write('portfolio')

# df = pd.DataFrame({'Courses': pd.Series(dtype='str'),
#                    'Fee': pd.Series(dtype='int'),
#                    'Duration': pd.Series(dtype='str'),
#                    'Discount': pd.Series(dtype='float')})

df = pd.DataFrame({'Ticker', 'Holdings'})

st.data_editor(df)