import streamlit as st
import requests as r
from google import generativeai as genai
import os
# compare ratings 

st.title("BookWorm")

baseURL  = "https://openlibrary.org/search.json?q="

st.write("This is the page for which we are implementing our chatbot, BookWorm.")


#key = st.secrets["key"]
key = "AIzaSyBbnNqSuyibRfXsxQBLNwfTV2tJ-_GUg40"


genai.configure(api_key=key)
content = st.text_input("hello")

model = genai.GenerativeModel('models/gemini-2.5-flash') #this is the free model of google gemini
try:
    response = model.generate_content(content) #enter your prompt here!
    st.write(response.text) #dont forget to print your response!
except:
    pass

#Query = st.text_input("Search for any Book by title, author, and more!", placeholder= "I'm looking for...")


#print(genai.GenerativeModel("gemini-1.5-flash"))