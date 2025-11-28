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





key = st.secrets["key"]
genai.configure(api_key=key)

st.slider("Book Length",min_value=10, max_value=1000)
st.checkbox("asfdklksd")


content = st.text_input("What Kind of Book Are You Looking For?")

model = genai.GenerativeModel('models/gemini-2.5-flash') #this is the free model of google gemini


if content:
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

