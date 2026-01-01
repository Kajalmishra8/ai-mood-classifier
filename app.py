import streamlit as st

st.title("🤖 Simple AI Mood Classifier")
st.write("Type how you are feeling, and the AI will analyze it.")

user_text = st.text_input("Enter your thoughts:")

if user_text:
    positive_words = ["happy", "great", "good", "excited", "awesome"]

    if any(word in user_text.lower() for word in positive_words):
        st.success("You seem to be in a POSITIVE mood ✨")
    else:
        st.info("You seem to be NEUTRAL or THOUGHTFUL 🤔")

st.sidebar.header("About")
st.sidebar.write("First Full Stack Python App 🚀")