import streamlit as st

with st.sidebar:
    st.sidebar.page_link("Home_Page.py", label="🏠Home Page🏠")
    st.sidebar.page_link("pages/Library.py", label="📚Library📖")
    st.sidebar.page_link("pages/CompareRatings.py", label="📊Book Comparisons📈")
    st.sidebar.page_link("pages/BookWorm.py", label="📚BookWorm Recommendations🐛")
    st.sidebar.page_link("pages/BookBot.py", label="🤖BookBot™")

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 14, Web Development - Section E")
st.image("Images/Library.jpeg",)
st.subheader("Eugene Li, Danielle Beaucejour")



st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Library**: Look up your favorite Book!
2. **Compare Books**: Compare two different books on different attributes.
4. **BookWorm**: Chat with an avid reading fan. 

""")

