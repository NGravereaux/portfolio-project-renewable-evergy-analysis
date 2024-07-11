import pandas as pd
import numpy as np
import seaborn as sns
import re


# H1: Perform initial data cheking:
def initial_data_checking(df):
    # Print the shape of the DataFrame (number of rows and columns)
    print("\nShape of the DataFrame:\n")
    print(df.shape)

# Print the count of duplicate rows
    print("\nDuplicate Rows Number:\n")
    print(df.duplicated().sum())

# Print summary statistics for numerical columns
    print("\nSummary Statistics:\n")
    print(df.describe())


# H1: check unique and missing values:
def unique_and_missing_values_dtype(df):
    # Non-null counts and data types
    non_null_counts = df.notnull().sum()
    dtypes = df.dtypes

    # Count of unique values
    unique_count = df.nunique()

    # Percentage of unique values
    unique_percentage = (df.nunique() / len(df)) * 100

    # Count of missing values
    missing_count = df.isnull().sum()

    # Percentage of missing values
    missing_percentage = df.isnull().mean() * 100

    # Combine into a DataFrame
    summary = pd.DataFrame({
        'non-Null_count': non_null_counts,
        'dtype': dtypes,
        'unique_values': unique_count,
        '%_unique': unique_percentage.round(2).astype(str) + '%',
        'missing_values': missing_count,
        '%_missing': missing_percentage.round(2).astype(str) + '%'
    })

    return summary


# H1:separate categorical and numerical columns for 1st Dataset : Global_electriciy_production
def separate_columns_h1(df1):
    categorical_cols = df1[['country_name',
                            'date', 'parameter', 'product', 'unit']]
    numerical_cols = df1[['value']]

    print("\nCategorical Columns:\n")
    print(categorical_cols.head())  # Using head() to show the first few rows
    print("\nNumerical Columns:\n")
    print(numerical_cols.head())  # Using head() to show the first few rows


# H1: analyze_numerical cols:
def analyze_numerical_h1(df):
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns

    # Perform descriptive analysis on numerical columns
    numerical_desc = df[numerical_cols].describe()

    # Display the resulting DataFrame
    print("\nNumerical Columns Analysis:")

    return numerical_desc


# H1:  analyze_categorical cols:
def analyze_categorical_h1(df):
    # Select categorical columns
    categorical_cols = df.select_dtypes(include=['object', 'category'])

    # Perform descriptive analysis on categorical columns
    categorical_desc = categorical_cols.describe()

    return categorical_desc


# H1: format column titles:
def format_column_titles_h1(df):
    # Define a function to clean a single column name
    def clean_column(name):
        name = name.strip()  # Remove leading and trailing spaces
        # Replace non-alphanumeric characters with underscores
        name = re.sub(r'[^0-9a-zA-Z]+', '_', name)
        # Replace multiple underscores with a single underscore
        name = re.sub(r'_+', '_', name)
        name = name.lower()  # Convert to lowercase
        return name.strip('_')  # Remove leading and trailing underscores

    # Apply the clean_column function to all column names in the DataFrame
    df.columns = [clean_column(col) for col in df.columns]
    return df.columns
