import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

key = "ENTER KEY"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Streamlit App of VGU")
st.text("Welcome to our dashboard")
st.header("I am a header")
st.write("you can write", 10 + 5)

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120)
course = st.selectbox("Enter your course:", ["B-TECH", "BCA", "MCA"])
st.write("Your name is:", name, " | Your age is:", age, "| Course:", course)

data = {"Name": ["A", "B", "C", "D"], "Marks": [10, 20, 20, 10]}
df = pd.DataFrame(data)
st.subheader("Student Marks Table")
st.dataframe(df)

chart_data = pd.DataFrame({"Marks": [10, 20, 20, 10]})
st.subheader("Line Chart")
st.line_chart(chart_data)
st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Subject-wise Pie Chart")
subject = ["Python", "C++", "Java"]
marks = [20, 10, 5]
fig, ax = plt.subplots()
ax.pie(marks, labels=subject, autopct='%1.1f%%')
st.pyplot(fig)

st.subheader("Chatbot Assistant")
user_query = st.text_input("Ask something:")
if user_query:
    response = model.generate_content(user_query)
    st.write("Bot:", response.text)

if st.button("Click me"):

    st.success("Button Clicked!")
