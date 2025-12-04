# teamwork_statistics_app.py
# Teamwork Statistics App powered by Sulaiman (Sir Mean) DS
# Streamlit web app for university statistics

import streamlit as st
import numpy as np
import pandas as pd
from fpdf import FPDF
import tempfile

# --------------------
# App Config & Welcome
# --------------------
st.set_page_config(page_title="Teamwork Statistics App", layout="wide")

st.title("Teamwork Statistics App")
st.markdown("""
**Welcome to Teamwork Statistics App!** 🎉  

**Developer:** Sulaiman Sunusi (Sir Mean) DS  
**Purpose:** Complete statistics app for university students  
**Note:** This app works fully in your browser and is safe to use.
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
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Mean", f"{np.mean(data_array):.4f}")
    col2.metric("Median", f"{np.median(data_array):.4f}")
    col3.metric("Variance", f"{np.var(data_array, ddof=1):.4f}")
    col4.metric("Std Dev", f"{np.std(data_array, ddof=1):.4f}")
    
    st.write(f"Min: {np.min(data_array)}, Max: {np.max(data_array)}, Range: {np.max(data_array)-np.min(data_array)}")

# --------------------
# Graphs (using Streamlit built-in charts)
# --------------------
if len(data_array) > 0:
    st.header("Graphs")
    graph_type = st.selectbox("Select Graph Type:", ["Line Chart", "Area Chart", "Bar Chart"])
    df = pd.DataFrame({"Values": data_array})
    if graph_type == "Line Chart":
        st.line_chart(df)
    elif graph_type == "Area Chart":
        st.area_chart(df)
    elif graph_type == "Bar Chart":
        st.bar_chart(df)

# --------------------
# PDF Report
# --------------------
st.header("PDF Report")
if st.button("Generate PDF Report"):
    if len(data_array) == 0:
        st.warning("No data to generate report.")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Teamwork Statistics App Report", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.ln(10)
        pdf.multi_cell(0, 8, f"Developer: Sulaiman Sunusi (Sir Mean) DS")
        pdf.multi_cell(0, 8, f"Data: {data_list}")
        pdf.multi_cell(0, 8, f"Mean: {np.mean(data_array):.4f}")
        pdf.multi_cell(0, 8, f"Median: {np.median(data_array):.4f}")
        pdf.multi_cell(0, 8, f"Variance: {np.var(data_array, ddof=1):.4f}")
        pdf.multi_cell(0, 8, f"Std Dev: {np.std(data_array, ddof=1):.4f}")
        pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf.output(pdf_file.name)
        st.success(f"PDF report generated: {pdf_file.name}")
        st.download_button("Download PDF", pdf_file.name)

st.write("💡 This app works fully in your browser. Share it with friends!")
