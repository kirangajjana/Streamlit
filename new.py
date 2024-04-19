import streamlit as st
import time as t
 #title
st.sidebar.title("welcome kiran gajjana")
st.sidebar.text_input("please enter your name")
st.sidebar.text_input("please enter your password")
st.sidebar.button("Submit")
st.sidebar.balloons()
st.title("welcome kiran gajjana")
#header
st.header("Kiran Gajjana")
#subheader
# st.subheader("Tech Mahindra")
#information details
st.info(" new information  is added here")
#warning
st.warning("come on time")
#write
st.write("Full Name")
st.checkbox('login')
#button
st.button('Click')
#radio button
st.radio("enter your gender",["male","female","Prefer not to say"])
#selectbox
st.selectbox("pick any on e of the course you want to opt",["Machine Learning","Deep Learning","Natural Language Processing"])
#multiselect
st.multiselect("Choose any content",["machine Learning","Deep Learning","Generative AI"])
#select slider
st.select_slider("rating",["bad","good","outstanding"])
#slider
st.slider("enter your number",0,30)
#number input
st.number_input("enter your input",0,100)
#text input
st.text_input("enter your username")
#date input
st.date_input("opening date")
#time input
st.time_input("input time")
#text area
st.text_area("hello welcome to kiran gajjana page")
#file uploader
st.file_uploader("upload your file")
#color picker
st.color_picker("color")
with st.spinner("just wait"):
    t.sleep(5)
st.balloons()    

