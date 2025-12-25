import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Cleaner",
    layout="centered"
)

st.title("📊DATA CLEANER WEB-APP📊")
st.write("Upload a CSV file to clean/remove missing values and duplicates.")
uploaded_file=st.file_uploader("Upload your data")

if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        df_clean=df.dropna().drop_duplicates()
        st.dataframe(df_clean)
        st.download_button("Download Clean CSV",df_clean.to_csv(index=False))