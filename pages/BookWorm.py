import streamlit as st
import requests as r
from google import generativeai as genai
import time
from datetime import date
currentDate = date.today()
currentYear = currentDate.year

import os
# compare ratings 

st.title("BookWorm")

baseURL  = "https://openlibrary.org/search.json?q=subject%3A"

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
if st.checkbox("Looking for a Specific Author"):
    author = st.text_input("Author")


content = st.text_input("What Kind of a Book Are You Looking For? i.e Fiction, Thriller, Happy, Educational, Mars etc.", 
                        placeholder= "Tags")
st.write("What Year do You Want Your Book to be Published In?")
start, end = st.columns(2)
with start:
    timelineStart = st.number_input("Starting Publishing Year", min_value=1200 , max_value= currentYear,step=10,value=1900)
with end:
    timelineEnd = st.number_input("Ending Publishing Year", max_value=1300, max_value = currentYear, step=10, value= currentYear)


model = genai.GenerativeModel('models/gemini-2.5-flash') #this is the free model of google gemini
if st.button("Give Me a Book!"):
    query = ""
    response = r.get(baseURL+"&mode=everything")
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

