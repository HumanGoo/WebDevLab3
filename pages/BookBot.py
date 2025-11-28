import streamlit as st
from google import generativeai as genai
import requests

#code for AI bot BookBot

st.title("BookBot")

st.text("This is BookBot, your reading assistant! Enter a book title to get a summary, reasons to read it, and recommendations for similar books.")

key = st.secrets["key"]
genai.configure(api_key=key)
model = genai.GenerativeModel("models/gemini-2.5-flash")

baseURL = "https://openlibrary.org/search.json?title="

def books(title):
    try:
        url = baseURL + title
        response = requests.get(url)
        data = response.json()
        docs = data.get("docs", [])[:3]
    except:
        return "Could not get book data."

    bookList = ""
    for book in docs:
        name = book.get("title", "Unknown Title")
        if "author_name" in book:
            author = book["author_name"][0]
        else:
            author = "Unknown Author"
        bookList += name + " by " + author + "\n"

    if bookList == "":
        return "No books found."
    return bookList

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["speaker"]):
        st.markdown(message["content"])

userText = st.chat_input("Enter a book title:")

if userText:
    st.session_state.messages.append({"speaker": "user", "content": userText})

    with st.chat_message("user"):
        st.markdown(userText)

    with st.chat_message("chatbot"):
        placeholder = st.empty()

        memory = ""
        for mem in st.session_state.messages:
            memory += mem["speaker"] + ": " + mem["content"] + "\n"

        apiRec = books(userText)

        prompt = (
            "You are BookBot. The user will enter a book title. "
            "Summarize each book in 2-4 sentences, explain why someone should read it in 2 sentences, and recommend similar books.\n\n"
            "Conversation:\n" + memory +
            "\nBooks Found:\n" + apiRec +
            "\nUser Entered:\n" + userText
        )

        try:
            reply = model.generate_content(prompt).text
        except:
            reply = "Error."

        placeholder.markdown(reply)

    st.session_state.messages.append({"speaker": "chatbot", "content": reply})
