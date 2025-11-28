import streamlit as st
import requests as r
from google import generativeai as genai
import time
import numpy as np
import pandas as pd

import os
# compare ratings 

st.title("BookWorm")

baseURL  = "https://openlibrary.org/search.json?q="

st.write("Welcome to BookWorm! Find the right book for you.")

"""
Find a book based on the filters passed through, and then have the LLM
explain why it is the right book for the person
"""

"""
PLANNED FILTERS:
length of book
genre/subject?
vibes of book
"""


key = st.secrets["key"]
genai.configure(api_key=key)

length = st.slider("Desired Book Length",min_value=10, max_value=1000)
subject = st.text_input("Subject/Genre")
if st.checkbox("Looking for a Specific Author"):
    author = st.text_input("Author")


content = st.text_input("What Kind of Book Are You Looking For?")


model = genai.GenerativeModel('models/gemini-2.5-flash') #this is the free model of google gemini
if st.button("Give Me a Book!"):
    response = model.generate_content(content)
    text = response.text

try:
    def stream_data():
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
    st.write_stream(stream_data) #dont forget to print your response!
except:
    pass

