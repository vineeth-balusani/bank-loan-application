import streamlit as st
import pandas as pd
import data_preprocessing
from datetime import datetime

st.title("Bank Loan Application Prediction")
st.write("-An ML application that predicts whether the loan can be sanctioned or not")

test_file = st.file_uploader("Please upload the file to obtain results")

if test_file is not None:
    test_file_df = pd.DataFrame()
    file_format = test_file.name.split(".")[-1]
    if (file_format == "csv" or file_format == "xls" or file_format == "xlsx"):
        if (file_format=="csv"):
            test_file_df = pd.read_csv(test_file)
        else:
            test_file_df = pd.read_excel(test_file)
        st.header("Information about the uploaded data:")
        st.write("Number of records - ", test_file_df.shape[0])
        st.write("Number of columns - ", test_file_df.shape[1])
        test_df = data_preprocessing.data_preprocessing(test_file_df)
        st.header("Ready to download results")
        st.write("Thank you for using the application. Click on the button below to download the results")
        st.download_button("Download Results", test_df.to_csv(index=False), file_name='Predictions_'+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'.csv', mime='text/csv')
    else:
        st.write("Only csv, xls and xlsx are acceptable formats for file upload")

