import streamlit as st
st.title("welcome to streamlit")
name=st.text_input("input your name")
if name:st.success(f"hello{name}")
age=st.slider("select ur age",1,200)
st.write("age",age)
if st.button("celebrate"):st.balloons()
