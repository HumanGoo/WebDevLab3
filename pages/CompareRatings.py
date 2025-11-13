import streamlit as st
import requests as r
import pandas as pd

#Compare Ratings Page

#Add Session Sattes 

st.title("Compare Book Ratings! 📚")
st.write("Choose books from the drop-down menu and compare ratings between these five popular reads!")

st.image("Images/Books.jpg")

if "selectedBooks" not in st.session_state:
    st.session_state.selectedBooks = ["hello"]
    
bookTitles = st.session_state.selectedBooks

#option = st.multiselect("Select Titles", ["Harry Potter and the Sorcerer's Stone", "1984", "To Kill a Mockingbird", "Moby Dick", "The Lord of the Rings"])

baseURL = "https://openlibrary.org/search.json?q="
response = r.get(baseURL)
data = response.json()
docs = data.get("docs", [])

'''
#make list session sate
for doc in docs:
    title = doc.get("title", "")
    if title:
        if title not in titles:
            bookTitles.append(title)
'''
selectBooks = st.multiselect("Select Books to Compare", bookTitles)

pagesorrate = st.selectbox("How would you like to compare?", ["Number of Pages", "Ratings"])

'''
ratingsStored = []

for book in [book1, book2]:
    if book:
        newURL = f"https://openlibrary.org/search.json?q={book}&fields=*,availability&limit=1"
        data = r.get(newURL).json()

        if data.get("docs"):
            docs = data["docs"][0]
            title = docs.get("ratings_average", 0)
            pages = docs.get("number_of_pages_median", 0)

        if pagesorrate == "Ratings":
            results.append({"Book": title, "Ratings":rating

        
"""
        newURL = baseURL + book + "&fields=*,availability&limit=1"
        response = r.get(newURL)
        data = response.json()

        if data.get("docs"):
            docs = data.get("docs")[0]
            title = docs.get("title", "")
            rating = docs.get("ratings_average", None)

            if rating == None:
                rating = 0
                ratingsStored.append({"Book":book, "Rating":0})
            else:
                ratingsStored.append({"Book": title, "Rating":rating})


    df = pd.DataFrame(ratingsStored)
    df = df.set_index("Book")

    st.subheader("Ratings Bar Graph")
    st.bar_chart(df)
"""           
'''

