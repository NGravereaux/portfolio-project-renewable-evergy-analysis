import pandas as pd
import numpy as np
import seaborn as sns
import re
import plotly.express as px
from scipy.stats import pearsonr


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


# H1.4. correlation index visualizaton:
def create_scatter_plot_with_trendline(df):
    # Calculate the Pearson correlation coefficient
    r, _ = pearsonr(df['gdp'], df['%_of_renewable'])

    # Create scatter plot with trendline
    fig = px.scatter(
        df,
        x="gdp",
        y="%_of_renewable",
        color="year",
        hover_name="country_name",
        trendline="ols",
        template="simple_white",
        title='Correlation between GDP per capita and % of Renewable energy production in EU countries in 2010-2023'
    )

    # Extract the trendline results

    # Add annotation for the correlation coefficient
    fig.add_annotation(
        x=0.05,
        y=0.95,
        xref="paper",
        yref="paper",
        text=f'r = {r:.2f}',
        showarrow=False,
        font=dict(size=12, color='red')
    )

    # Update layout
    fig.update_layout(
        xaxis_title="GDP per capita, USD",
        yaxis_title="% Renewable Energy Production, GWh",
        legend_title_text="Year"
    )

    # Show the figure
    fig.show()


# H1.4. bar chart: the average % of renewable energy adoption for each country in 2010-2023
def create_bar_chart_with_target(df):
    # Calculating the average % of renewable energy for each country over all years
    average_renewable_per_country = df.groupby(
        'country_name')['%_of_renewable'].mean().reset_index()

    # Sorting the DataFrame by '%_of_renewable' in ascending order
    average_renewable_per_country = average_renewable_per_country.sort_values(
        by='%_of_renewable', ascending=True)

    # Plotting the bar chart with country on the x-axis using Plotly Express
    fig = px.bar(average_renewable_per_country,
                 y='%_of_renewable',
                 x='country_name',
                 color="country_name",
                 hover_name="country_name",
                 template="simple_white",
                 title='Average Percentage of Renewable Energy by Country (All Years)',
                 labels={'%_of_renewable': 'Average % of Renewable Energy for all years',
                         'country_name': 'Country Name'},
                 text='%_of_renewable',
                 width=800, height=500)  # Adjusting the width and height

    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')

    # Adding the target line at 42%
    fig.add_shape(type='line',
                  x0=-0.5, y0=42, x1=len(average_renewable_per_country)-0.5, y1=42,
                  line=dict(color='Red', dash='dash'))

    # Adding target label
    fig.add_annotation(x=len(average_renewable_per_country)-0.5, y=42,
                       text='Target: 42%',
                       showarrow=False,
                       xshift=10, yshift=10,
                       font=dict(color='Red'))

    fig.show()
