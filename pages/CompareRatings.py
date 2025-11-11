import streamlit as st
import requests as r
import pandas as pd

#Compare Ratings Page 

st.title("Compare Book Ratings! 📚")
st.write("Choose books from the drop-down menu and compare ratings between these five popular reads!")

st.image("Images/Books.jpg")

option = st.multiselect("Select Titles", ["Harry Potter and the Sorcerer's Stone", "1984", "To Kill a Mockingbird", "Moby Dick", "The Lord of the Rings"])

baseURL = "https://openlibrary.org/search.json?q="

ratingsStored = []

# may need to make this dynamic 

if option:
    for book in option:
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
            


