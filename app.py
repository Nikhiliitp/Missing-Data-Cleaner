import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from io import BytesIO

st.set_page_config(page_title="Missing Data Cleaner", layout="wide")
st.title("🧹 Missing Data Cleaner")

st.sidebar.header("Upload & Options")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Method selection
method = st.sidebar.selectbox("Choose fill method for numeric columns", ["mean", "median", "mode"])

# State
if "df" not in st.session_state:
    st.session_state.df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df.copy()
    st.subheader("📊 Preview of Uploaded Dataset")
    st.write(df.head())

    # Missing values summary
    st.subheader("🔍 Missing Values per Column")
    missing_counts = df.isnull().sum()
    st.write(missing_counts)

    # Chart with fixed aspect ratio
    fig, ax = plt.subplots(figsize=(12, 6))  # ✅ ~1800x900px
    missing_counts.plot(kind="bar", ax=ax, title="Missing Values per Column")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    st.pyplot(fig, use_container_width=True)  # ✅ Fit inside container

    # Cleaning process
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if method == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif method == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    elif method == "mode":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mode().iloc[0])

    # Fill categorical with mode
    cat_cols = df.select_dtypes(exclude=["number"]).columns
    if len(cat_cols) > 0:
        df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    st.subheader("✅ Cleaned Dataset Preview")
    st.write(df.head())

    # Download cleaned CSV
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="💾 Download Cleaned CSV",
        data=buffer,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )
else:
    st.info("👈 Please upload a CSV file to begin.")
