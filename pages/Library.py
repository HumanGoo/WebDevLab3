import streamlit as st
import requests as r
from math import ceil

st.title("Library")

baseURL  = "https://openlibrary.org/search.json?q="
imageURL = "https://covers.openlibrary.org/b/id/"


if 'query' not in st.session_state:
    st.session_state.query = ""
Query = st.text_input("Search for any Book by title, author, and more!", value= st.session_state.query, placeholder= "I'm looking for...")
st.session_state.query = Query
if 'count' not in st.session_state:
    st.session_state.count = 1
count = st.session_state.count
if Query:
    
    pageNumber = f"&page={st.session_state.count}"
    request = r.get(baseURL + Query + pageNumber)
    data = request.json()
    amount = f"{data['numFound']:,}"
    col1, col2, filler = st.columns([3,4,2])
    resultHits = len(data['docs']) + (100 * (count-1))
    firstEntry = 1+(100 * (count-1))
    maxPage = ceil(data['numFound']/100)
    with col1:
        st.write(f"{amount} hits")
    with col2:
        if len(data['docs']):
            firstEntry = 1+(100 * (count-1))
        else:
            firstEntry = 0
        st.write(f"*showing {firstEntry} - {resultHits} out of {amount} results*")
    with filler:
        try:
            newcount = st.number_input(f"Page {st.session_state.count} out of {maxPage}", min_value=0, max_value=maxPage,value=st.session_state.count,
                                        step=1)
        except:
            newcount = count
        st.session_state.count = newcount
        if st.session_state.count != count:
            st.rerun()
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
