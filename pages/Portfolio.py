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

if portfolio == 'Add New...':
    name = ''
    currency = ''
    del_button = False
else:
    name = ref.document(portfolio).get().to_dict()['name']
    currency = ref.document(portfolio).get().to_dict()['currency']
    del_button = True

portfolio_name = st.text_input('pf_name', name)
portfolio_currency = st.text_input('pf_currency', currency)

submitted = st.button('Update', use_container_width=True)
removed = st.button('Del', use_container_width=True, disabled=del_button)

if submitted:
    data = {'name': portfolio_name, 'currency': portfolio_currency}
    ref.document(portfolio_name).set(data)
    st.experimental_rerun()

if removed:
    ref.document(portfolio_name).delete()
    st.experimental_rerun()


    # st.write(f"{i.id} => {i.to_dict()}")
