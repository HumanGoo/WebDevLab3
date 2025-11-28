import streamlit as st
import requests as r
from google import generativeai as genai
import time
from datetime import date
currentDate = date.today()
currentYear = currentDate.year
aList = []
aNum = 1000
for i in range(0,aNum+1,10):
    aList.append(i)

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
author = ""
try:
    key = st.secrets["key"]
    genai.configure(api_key=key)
except:
    st.error("LLM Key Not Found")

#length = st.slider("Desired Book Length",min_value=10, max_value=1000)
if st.checkbox("Looking for a Specific Author"):
    author = st.text_input(label="",placeholder="Author")
else:
    author = ""


content = st.text_input("What Kind of a Book Are You Looking For? i.e Fiction, Thriller, Happy, Educational, Mars etc.", 
                        placeholder= "Tags")
start, end = st.select_slider(
    "Select a range of your desired book's page length",
    options=aList,
    value=(0, aNum),
)

model = genai.GenerativeModel('models/gemini-2.5-flash') #this is the free model of google gemini

if st.button("Give Me a Book!"):
    query = content.strip().replace(" ","").lower()
    query += f"+number_of_pages%3A%5B{start}+TO+{end}%5D"
    if author:
        query+= f"+author:{author}"
    data = r.get(baseURL+query+"&mode=everything&sort=readinglog")
    aDict = data.json()
    #st.write(baseURL+query+"&mode=everything&sort=readinglog")
    bList = []
    try:
        aDict["docs"][i]["title"]
        for i in range(0,101):
            bList.append(aDict["docs"][i]["title"])
    except:
        for i in aDict["docs"]:
            #st.write(i["title"])
            bList.append(i["title"])
    #st.write(bList)
    
    fullContent = f"""
    You are a librarian managing a catalogue of books: {bList}. 
    From this list of books titles, I want a book that is around {start} to {end} pages long, and satisfies the following
    tags: {content}. After choosing the right book for me, start your response with "I reccommend this book". Then give paragraph summary 
    of the book and then give me reasons as to why I should read this book.
    """

    
    response = model.generate_content(fullContent)
    text = response.text
    

try:
    def stream_data():
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
    st.write_stream(stream_data) #dont forget to print your response!
except:
    pass

