import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.anomaly_detection import detect_anomalies

from pyod.models.iforest import IForest
from pyod.models.knn import KNN
from pyod.models.auto_encoder import AutoEncoder

def get_model(name: str, contamination: float):
    if name == "IsolationForest":
        return IForest(contamination=contamination)
    elif name == "KNN":
        return KNN(contamination=contamination)
    elif name == "AutoEncoder":
        return AutoEncoder(contamination=contamination)
    else:
        st.error("Unsupported model selected.")
        return None

def main():
    st.title("Anomaly Detection Application")

    uploaded_file = st.file_uploader("Upload your data file (CSV, Excel, JSON)", type=['csv', 'xlsx', 'json'])

    if uploaded_file is not None:
        # Determine file type from extension
        file_type = uploaded_file.name.split('.')[-1]

        # Load data
        df = load_data(uploaded_file, file_type)

        if df is not None:
            st.write("### Raw Data Preview")
            st.dataframe(df.head())

            # Clean data
            clean_df = clean_data(df)
            st.write("### Cleaned Data Preview")
            st.dataframe(clean_df.head())

            # Model selection
            model_choice = st.selectbox(
                "Choose anomaly detection model",
                ["IsolationForest", "KNN", "AutoEncoder"]
            )
            contamination = st.slider("Contamination (expected anomaly proportion)", 0.01, 0.5, 0.1)

            if st.button("Run Anomaly Detection"):
                model = get_model(model_choice, contamination)
                if model is not None:
                    try:
                        result = detect_anomalies(clean_df, model, contamination)
                        st.write("### Anomaly Detection Results")
                        st.dataframe(result.head())
                    except Exception as e:
                        st.error(f"Error during anomaly detection: {e}")

if __name__ == "__main__":
    main()