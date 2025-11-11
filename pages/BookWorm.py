import streamlit as st
import requests as r

st.title("Library")

baseURL  = "https://openlibrary.org/search.json?q="


Query = st.text_input("Search for any Book by title, author, and more!", placeholder= "I'm looking for...")

if Query:
    request = r.get(baseURL + Query)
    data = request.json()
    st.write(data)