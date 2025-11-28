import streamlit as st
from google import generativeai as genai
import requests

st.title("BookBot")

key = st.secrets["key"]
genai.configure(api_key=key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

baseURL = "https://openlibrary.org/search.json?q=subject%3A"

def books(subject):
    url = baseURL + subject
    response = requests.get(url)
    data = response.json()
    docs = data.get("docs", [])[:5]

    bookList = ""
    for book in docs:
        title = book.get("title", "Unknown Title")

        if "author_name" in book:
            author = book["author_name"][0]
        else:
            author = "Unknown Author"

        bookList += title + " by " + author + "\n"

    if bookList == "":
        return "No books found."
    else:
        return bookList

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["speaker"]):
        st.markdown(message["content"])

userText = st.chat_input("Enter a book subject (ex. fantasy, romance, history):")

if userText:
    st.session_state.messages.append({"speaker": "user", "content": userText})

    with st.chat_message("user"):
        st.markdown(userText)

    with st.chat_message("chatbot"):
        placeholder = st.empty()

        memory = ""
        for m in st.session_state.messages:
            memory += m["speaker"] + ": " + m["content"] + "\n"

        apiRec = books(userText)

        prompt = (
            "You are a chatbot that recommends books based on subjects entered.\n"
            "Prior Conversation:\n" + memory +
            "\nBook Recommendation:\n" + apiRec +
            "\nSubject: " + userText
        )

        try:
            response = model.generate_content(prompt)
            reply = response.text
        except Exception as e:
            reply = "Error: " + str(e)

        placeholder.markdown(reply)

    st.session_state.messages.append({"speaker": "chatbot", "content": reply})

