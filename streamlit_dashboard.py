import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="My Simple Dashboard", layout="wide")


st.title("Interactive Streamlit Dashboard")
st.write("Welcome! Select a tool from the sidebar to get started.")


st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to:", ["Home", "Number Checker", "Data Visualization"])


if option == "Home":
    st.header("Home")
    st.write("This is a simple human-readable dashboard created with Python and Streamlit.")
    st.info("Use the sidebar menu to explore different features.")


elif option == "Number Checker":
    st.header("Positive / Negative Number Checker")
    st.write("Enter a number below to check if it is positive, negative, or zero.")

    user_number = st.number_input("Enter a number:", value=0.0, step=1.0)
    

    if st.button("Check Number"):
        if user_number > 0:
            st.success(f"The number {user_number} is POSITIVE (+).")
        elif user_number < 0:
            st.error(f"The number {user_number} is NEGATIVE (-).")
        else:
            st.warning(f"The number is ZERO (0).")


elif option == "Data Visualization":
    st.header("Simple Data Visualization")
    st.write("Here is a chart with some random data.")
    
   
    data_size = st.slider("Select number of data points:", min_value=10, max_value=100, value=50)
    
  
    chart_data = pd.DataFrame(
        np.random.randn(data_size, 3),
        columns=['A', 'B', 'C']
    )
    
 
    st.line_chart(chart_data)
    
    st.write("Data Table:")
    st.dataframe(chart_data)


