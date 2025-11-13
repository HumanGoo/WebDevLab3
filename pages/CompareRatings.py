import streamlit as st
import requests as r
import pandas as pd

st.title("Compare Ratings and Number of Pages for Fantasy Books")
st.write("Looking for your next read? Compare **book ratings** and **page numbers** between fantasy books.")

st.image("Images/fantasyBook.jpg")

if "ratingsStored" not in st.session_state:
    st.session_state.ratingsStored = []

baseURL = "https://openlibrary.org/subjects/fantasy.json?limit=100"
response = r.get(baseURL)
data = response.json()

bookTitles = []
for book in data.get("works", []):
    title = book.get("title", "Unknown Title")
    bookTitles.append(title)

chooseTitles = st.multiselect("Select Fantasy Titles:", bookTitles)

rateOrPage = st.selectbox("Choose to compare ratings or number of pages", ["Ratings", "Number of Pages"])

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
            else:
                pageNum = doc.get("number_of_pages_median", 0)
                st.session_state.ratingsStored.append({"Book": title, "Pages": pageNum or 0})

if st.session_state.ratingsStored:
    df = pd.DataFrame(st.session_state.ratingsStored)
    df = df.set_index("Book")
    st.subheader(f"{rateOrPage} Bar Graph")
    st.bar_chart(df)
