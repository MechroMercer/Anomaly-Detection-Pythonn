import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_boxplot(df, feature):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=feature, ax=ax)
    ax.set_title(f"Boxplot for {feature}")
    st.pyplot(fig)

def plot_scatter(df, anomaly_column, feature_x, feature_y):
    if anomaly_column not in df.columns:
        st.error(f"Column '{anomaly_column}' not found in DataFrame.")
        return
    fig, ax = plt.subplots()
    palette = {0: "blue", 1: "red"} if df[anomaly_column].nunique() <= 2 else "deep"
    sns.scatterplot(data=df, x=feature_x, y=feature_y, hue=anomaly_column, palette=palette, ax=ax)
    ax.set_title(f"Scatterplot: {feature_x} vs {feature_y}")
    st.pyplot(fig)