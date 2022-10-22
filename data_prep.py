# Aim is to develop the data pre-processing app using streamlit for processing missing values

# File Upload - Missing Value Treatment - Download the processed File
# File-Upload -> Temp Location -> Missing Value Treatment -> Download the processed file
# Outlier Treatment


import streamlit as st
import pandas as pd
import os

# Title of the Web App
st.title("Data Pre Processing App")

# For windows
# temp = "\\temp.csv"

temp = "/temp.csv"

path = os.getcwd()
path = path + temp


# Function to upload the file
def file_upload():
    file = st.sidebar.file_uploader("Upload your file", type=["csv", "xlsx"])
    if st.sidebar.button("Upload"):
        if file and file.name.endswith("csv"):
            df = pd.read_csv(file)
            # Store the df in temp location
            df.to_csv(path)
            st.write(df)
        elif file and file.name.endswith("xlsx"):
            df = pd.read_excel(file)
            # Store the df in temp location
            df.to_csv(path)
            st.write(df)


# Function to treat the missing values
def missing_value_treatment_using_mean():
    df = pd.read_csv(path)
    processed_df = df.fillna(df.mean())
    st.write(processed_df)
    processed_df.to_csv(path, index=False)


# Function to treat the missing values using median
def missing_value_treatment_using_median():
    df = pd.read_csv(path)
    processed_df = df.fillna(df.median())
    st.write(processed_df)
    processed_df.to_csv(path, index=False)


# Function to treat the missing values using mode
def missing_value_treatment_using_mode():
    df = pd.read_csv(path)
    processed_df = df.fillna(df.mode())
    st.write(processed_df)
    processed_df.to_csv(path, index=False)


def outlier_treatment_using_iqr():
    df = pd.read_csv(path)
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    # Treatment
    df = df[~((df < (q1 - 1.5 * iqr)) | (df > (q3 + 1.5 * iqr))).any(axis=1)]
    st.write(df)
    df.to_csv(path, index=False)


# Function to download the file
# DataFrame is not a file we need to convert it into a file using df.to_csv()
def download_file():
    df = pd.read_csv(path)
    st.sidebar.download_button(
        label="Download the file",
        data=df.to_csv(index=False),
        file_name="Processed_file.csv",
        mime="text/csv",
    )


# Function to provide all the main options
def main_options():
    main_option_list = ["Missing Value Treatment", "Outlier Treatment", "Feature Scaling", "Download"]
    main_choice = st.sidebar.radio("Select the option", main_option_list)
    return main_choice


def missing_value_treatment_options():
    missing_value_treatment_list = ["Mean", "Median", "Mode"]
    missing_value_treatment_choice = st.sidebar.radio("Select the option", missing_value_treatment_list)
    if missing_value_treatment_choice == "Mean":
        if st.sidebar.button("Process using Mean"):
            missing_value_treatment_using_mean()

    if missing_value_treatment_choice == "Median":
        if st.sidebar.button("Process using Median"):
            missing_value_treatment_using_median()

    if missing_value_treatment_choice == "Mode":
        if st.sidebar.button("Process using Mode"):
            missing_value_treatment_using_mode()


def outlier_treatment_option():
    outlier_treatment_option_list = ["IQR", "Z-Score"]
    outlier_treatment_option_choice = st.sidebar.selectbox("Select the option", outlier_treatment_option_list)
    if outlier_treatment_option_choice == "IQR":
        if st.sidebar.button("Process using IQR"):
            outlier_treatment_using_iqr()
    elif outlier_treatment_option_choice == "Z-Score":
        st.write("Z-Score")


def main():
    file_upload()
    main_choice = main_options()

    if main_choice == "Missing Value Treatment":
        missing_value_treatment_options()

    elif main_choice == "Outlier Treatment":
        outlier_treatment_option()

    elif main_choice == "Feature Scaling":
        st.write("Feature Scaling")

    elif main_choice == "Download":
        download_file()


main()
