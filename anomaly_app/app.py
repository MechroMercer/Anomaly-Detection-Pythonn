import streamlit as st
from src.data_loader import load_data

st.set_page_config(page_title="Anomaly Detection App", layout="centered")

st.title("📊 Anomaly Detection App")
st.write("Upload your dataset (CSV, Excel, or JSON) to begin.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    if file_type == "xlsx":
        file_type = "excel"

    try:
        df = load_data(uploaded_file, file_type)
        st.success("File loaded successfully!")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Failed to load file: {e}")