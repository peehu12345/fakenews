import streamlit as st

st.title("Fake News Detector")
st.write("Enter a News Article below to check whether it is fake or real.")

news_input = st.text_area("News Article:", "")

if st.button("Check News"):
    if news_input.strip():
        st.success("Pretend analysis: This News is Real!")  # Dummy response
    else:
        st.warning("Please enter some text to analyze.")
