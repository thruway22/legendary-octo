import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import pandas as pd
import yfinance as yf
import auxload as aux

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="port-test-69ded")

# Create a reference to the Google post.
doc_ref = db.collection("assets").document("1")

# Then get the data at that reference.
doc = doc_ref.get()

st.title('Test')

st.button('Add Asset')

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   aux.lead()

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())



