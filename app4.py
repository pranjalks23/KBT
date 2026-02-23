import streamlit as st 

st.title("Simple Chatpot")
Question=st.text_input("Ask me Anything")

if st.button("Send"):
    st.write("You asked",Question)
    st.write("Chatbot is in process will reply soon")