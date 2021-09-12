import requests
import streamlit as st

DOCUMENTS_URL = 'http://localhost:8000/documents'

st.header("Add documents")

with st.form(key='add_doc_form'):
    author = st.text_input(label='Author')
    date = st.text_input(label='Date')
    body = st.text_input(label='Body')
    submitted = st.form_submit_button(label='Add document')
    if submitted:
        res = requests.post(DOCUMENTS_URL, json={'author': author, 'date': date, 'body': body})

st.header("Document search")

search_string = st.text_input("Search documents", "")

res = requests.get(DOCUMENTS_URL, params={'search_string': search_string}).json()

for doc in res:
    st.text(doc['body'])
