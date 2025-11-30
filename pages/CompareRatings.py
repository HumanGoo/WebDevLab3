import streamlit as st
import requests as r
import pandas as pd
from datetime import datetime

current_year = datetime.now().year
st.title("Compare Ratings and Number of Pages for Books")
st.write("Looking for your next read? Compare **book ratings** and **page numbers** between books in the same genre.")

st.image("Images/fantasyBook.jpg")

if "ratingsStored" not in st.session_state:
    st.session_state.ratingsStored = []
if 'subject' not in st.session_state:
    st.session_state.subject = ""

subjectList = [None,"Fantasy","Arts","Young_Adult_Fiction","Science_Fiction","Biography","Romance","Horror","Plays"]
subject = st.selectbox("Select a Subject:", subjectList, placeholder= None)

bookTitles = []
if subject:
    st.session_state.subject = subject.lower()
    baseURL = f"https://openlibrary.org/subjects/{st.session_state.subject}.json?limit=100"
    response = r.get(baseURL)
    data = response.json()
    for book in data.get("works", []):
        title = book.get("title", "Unknown Title")
        if "Novels" not in title:
            bookTitles.append(title)

chooseTitles = st.multiselect("Select Titles:", bookTitles)

rateOrPage = st.selectbox("Choose to compare ratings or number of pages", ["Ratings", "Number of Pages", "Age"])

if chooseTitles:
    
    st.session_state.ratingsStored = []
    for book in chooseTitles:
        newURL = f"https://openlibrary.org/search.json?q={book}&fields=*,availability&limit=1"
        response = r.get(newURL)
        data = response.json()
        docs = data.get("docs", [])
        
        if docs:
            doc = docs[0]
            title = doc.get("title", book)
            
            if rateOrPage == "Ratings":
                ratingNum = doc.get("ratings_average", 0)
                st.session_state.ratingsStored.append({"Book": title, "Rating": ratingNum or 0})
            elif rateOrPage == "Number of Pages":
                pageNum = doc.get("number_of_pages_median", 0)
                st.session_state.ratingsStored.append({"Book": title, "Pages": pageNum or 0})
            else:
                PublishYear = doc.get("publish_year",0)
                ageNum = current_year - PublishYear[0]
                st.session_state.ratingsStored.append({"Book": title, "Age": ageNum or 0})

if st.session_state.ratingsStored:
    with st.container(): 
        df = pd.DataFrame(st.session_state.ratingsStored)
        df = df.set_index("Book")
        st.subheader(f"{rateOrPage} Bar Graph")
        st.bar_chart(df)
