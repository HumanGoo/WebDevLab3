import streamlit as st
import requests as r

st.title("Library")

baseURL  = "https://openlibrary.org/search.json?q="


Query = st.text_input("Search for any Book by title, author, and more!", placeholder= "I'm looking for...")

if Query:
    request = r.get(baseURL + Query)
    data = request.json()
    for result in data['docs']:
        st.header(result["title"])
        authors = ", ".join(result["author_name"])
        st.write(f'by {authors}')
        st.divider()
