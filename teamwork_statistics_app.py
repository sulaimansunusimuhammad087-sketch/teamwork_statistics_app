# streamlit_app.py
# Teamwork Statistics App powered by Sulaiman (Sir Mean) DS
# Streamlit web app for university statistics

import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="Teamwork Statistics App", layout="wide")

# Welcome message
st.title("Teamwork Statistics App")
st.markdown("""
**Developer:** Sulaiman Sunusi (Sir Mean) DS  
**Purpose:** Complete statistics app for university students
""")

# --------------------
# Data Input
# --------------------
st.header("Data Input")
data_source = st.radio("Choose Data Source:", ["Manual Input", "Random Data"])

data_list = []

if data_source == "Manual Input":
    data_str = st.text_area("Enter numbers separated by comma, space, or newline:")
    if st.button("Add Data"):
        try:
            data_list = [float(x) for x in data_str.replace("\n", " ").replace(",", " ").split() if x.strip() != ""]
            st.success(f"Added {len(data_list)} numbers.")
        except Exception as e:
            st.error(f"Error parsing numbers: {e}")
elif data_source == "Random Data":
    n = st.number_input("Number of random numbers:", min_value=1, value=30)
    start = st.number_input("Start value:", value=0.0)
    end = st.number_input("End value:", value=10.0)
    if st.button("Generate Random Data"):
        data_list = list(np.random.uniform(start, end, n))
        st.success(f"Generated {n} random numbers between {start} and {end}.")

if len(data_list) > 0:
    st.subheader("Current Data")
    st.write(data_list)
    data_array = np.array(data_list)
else:
    data_array = np.array([])

# --------------------
# Basic Stats
# --------------------
if len(data_array) > 0:
    st.header("Basic Statistics")
    st.write(f"Mean: {np.mean(data_array):.4f}")
    st.write(f"Median: {np.median(data_array):.4f}")
    st.write(f"Variance: {np.var(data_array, ddof=1):.4f}")
    st.write(f"Std Dev: {np.std(data_array, ddof=1):.4f}")
    st.write(f"Min: {np.min(data_array)}, Max: {np.max(data_array)}, Range: {np.max(data_array)-np.min(data_array)}")

# --------------------
# Info
# --------------------
st.write("💡 This app works fully in your browser. Share it with friends!")
