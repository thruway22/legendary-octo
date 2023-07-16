import streamlit as st
import pandas as pd
from db import db


st.title('Portfolio')
# left, right = st.columns([4,1])
# left.selectbox('portfolio', ['All', 'USD', 'SAR'], label_visibility='collapsed')
# right.button('Add Portfolio')
# df = pd.DataFrame({'names': ['VTI', 'KSA'], 'Hold': [10, 12]})

col_ref = db.collection('portfolios')

pf_name = st.text_input('pf_name')
pf_currency = st.text_input('pf_currency')
submitted = st.button('Add Portfolio')

if submitted:
    data = {'name': pf_name, 'currency': pf_currency}
    col_ref.document(pf_name).set(data)

doc = db.collection('portfolios').stream()
doc_list = []
for i in doc:
    doc_list.append(i.id)
    # st.write(f"{i.id} => {i.to_dict()}")

port = st.selectbox('portfolio', doc_list, label_visibility='collapsed')