import streamlit as st

st.title("Simple Input App")
name=st.text_input("Enter your Name")

if st.button("Submit"):
    st.write("Hello ", name)