import streamlit as st 
st.markdown("""
<style>
            .stButton > button
            {
            background-color:green;
            color:"white";
            border-radius:50%;
            }
</style>


""",unsafe_allow_html=True)


st.title("Welcome to the basic streamlit app")
age=st.slider("Select your Age",1,100)
city=st.selectbox("Select your City",["Delhi","Mumbai","Nashik","Pune"])

if st.button("Show Details"):
    st.write("Age:",age)
    st.write("City:", city)