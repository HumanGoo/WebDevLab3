import streamlit as st
import requests as r

# compare ratings 

st.title("BookWorm")

baseURL  = "https://openlibrary.org/search.json?q="

st.write("This is the page for which we are implementing our chatbot, BookWorm")
#Query = st.text_input("Search for any Book by title, author, and more!", placeholder= "I'm looking for...")
