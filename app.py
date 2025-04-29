import streamlit as st
import pandas as pd

st.title("Product Matching Review App")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    df['Status'] = df.get('Status', 'Unchecked')

    for i in range(len(df)):
        col1, col2 = st.columns(2)
        with col1:
            st.write(df.iloc[i])
        with col2:
            if st.button(f"Correct {i}"):
                df.at[i, 'Status'] = 'Correct'
            if st.button(f"Incorrect {i}"):
                df.at[i, 'Status'] = 'Incorrect'

    st.download_button("Download Results", df.to_csv(index=False), "matched_results.csv")
