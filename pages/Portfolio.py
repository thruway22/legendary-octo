import streamlit as st
import pandas as pd
from db import db


st.title('Portfolio')
# left, right = st.columns([4,1])
# left.selectbox('portfolio', ['All', 'USD', 'SAR'], label_visibility='collapsed')
# right.button('Add Portfolio')
# df = pd.DataFrame({'names': ['VTI', 'KSA'], 'Hold': [10, 12]})

ref = db.collection('portfolios')
docs = ref.stream()

portfolios = []
for i in docs:
    portfolios.append(i.id)
portfolios.append('Add New...')   

portfolio = st.selectbox('portfolio', portfolios, label_visibility='collapsed')

name = ref.document(portfolio).get().to_dict()['name']
currency = ref.document(portfolio).get('currency')

portfolio_name = st.text_input('pf_name', name)
portfolio_currency = st.text_input('pf_currency', currency)
submitted = st.button('Update')

if submitted:
    data = {'name': portfolio_name, 'currency': portfolio_currency}
    ref.document(portfolio).set(data)


    # st.write(f"{i.id} => {i.to_dict()}")
