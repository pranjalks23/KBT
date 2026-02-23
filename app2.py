import streamlit as st 

st.title("Welcome ti the basic streamlit app")
age=st.slider("Select your Age",1,100)
city=st.selectbox("Select your City",["Delhi","Mumbai","Nashik","Pune"])

if st.button("Show Details"):
    st.write("Age:",age)
    st.write("City:", city)