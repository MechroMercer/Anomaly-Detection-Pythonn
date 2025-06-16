import pandas as pd

def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

def preprocess_data(df):
    numeric_df = df.select_dtypes(include=["number"]).copy()

    numeric_df = numeric_df.fillna(numeric_df.mean())

    return numeric_df