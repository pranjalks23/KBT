import streamlit as st 


st.markdown("""
<style>
            .stButton > button
            {
            background-color:blue;
            color:"white";
            border-radius:20%;
            }

            .stTextInput > text_input
            {
            background-color:light-blue;
            }
</style>


""",unsafe_allow_html=True)


st.title("Form")
first=st.text_input("Enter First Name:")
last=st.text_input("Enter Last Name:")
age=st.number_input("Enter Age:" ,format="%d")
phone=st.number_input("Enter Phone No.",format="%d")
email=st.text_input("Enter Email:")

if st.button("Submit"):
    st.write("Submitted Successfully")