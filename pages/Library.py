import streamlit as st
import requests as r

st.title("Library")

baseURL  = "https://openlibrary.org/search.json?q="
imageURL = "https://covers.openlibrary.org/b/id/"


Query = st.text_input("Search for any Book by title, author, and more!", placeholder= "I'm looking for...")

if Query:
    count = 1
    pageNumber = f"&page={count}"
    request = r.get(baseURL + Query + pageNumber)
    data = request.json()
    amount = f"{data['numFound']:,}"
    col1, col2, filler = st.columns([3,4,1])
    resultHits = len(data['docs'])
    with col1:
        st.write(f"{amount} hits")
    with col2:
        st.write(f"*showing {resultHits} out of {amount} results*")

    for result in data['docs']:
        col1, col2 = st.columns([1,2])
        with col1:
            try:
                st.image(f'{imageURL}{result["cover_i"]}-M.jpg')
            except:
                st.image("Images/Message_Not_Found.jpg")
        with col2:  
            st.header(result["title"])
            try:
                authors = ", ".join(result["author_name"])
            except:
                authors = "Unknown"
            st.subheader(f'by {authors}')
            st.write(f"First published in {result['first_publish_year']}")
        st.divider()
