# PACKAGES FOR HYPOTHESIS 1
import pandas as pd
import numpy as np
import seaborn as sns
import re
import plotly.express as px
from scipy.stats import pearsonr

# PACKAGES FOR HYPOTHESIS 2
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# PACKAGES FOR HYPOTHESIS 3
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr



#### FUNCITONS FOR HYPOTHESIS 1 ###

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




### FUNCTIONS FOR HYPOTHESIS 2 ###

# H2: Get Solar Radiation Classification Dictionnary for all EU Countries
def get_solar_class_dict():
    """Classifcation according to the average annual global solar radiation [kWh/m2] (period 1994-2016)"""
    eu_countries_solar_radiation_classification_dict = {
    'Austria': '2: low',
    'Belgium': '2: low',
    'Bulgaria': '3: medium',
    'Croatia': '3: medium',
    'Cyprus': '5: very high',
    'Czech Republic': '2: low',
    'Denmark': '1: very low',
    'Estonia': '2: low',
    'Finland': '1: very low',
    'France': '3: medium',
    'Germany': '2: low',
    'Greece': '4: high',
    'Hungary': '3: medium',
    'Ireland': '1: very low',
    'Italy': '4: high',
    'Latvia': '2: low',
    'Lithuania': '2: low',
    'Luxembourg': '2: low',
    'Malta': '5: very high',
    'Netherlands': '2: low',
    'Poland': '2: low',
    'Portugal': '4: high',
    'Romania': '3: medium',
    'Slovak Republic': '2: low',
    'Slovenia': '3: medium',
    'Spain': '5: very high',
    'Sweden': '1: very low'}
    return eu_countries_solar_radiation_classification_dict

# H2: Get Dictionary to translate Country Codes in Country Names
def get_country_codes_dict():
    country_codes_dict = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DE': 'Germany',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'EL': 'Greece',
    'ES': 'Spain',
    'FI': 'Finland',
    'FR': 'France',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IT': 'Italy',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'MT': 'Malta',
    'NL': 'Netherlands',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'SE': 'Sweden',
    'SI': 'Slovenia',
    'SK': 'Slovak Republic'}
    return country_codes_dict


def get_clean_demographic_data():
    
    # Load demographic data (Population and Area)
    df_pop = pd.read_csv("../data/eu_country_population.csv")
    df_area = pd.read_csv("../data/eu_country_area.csv")
    
    # Rename columns
    df_pop = df_pop.rename(columns={'OBS_VALUE': "population"})
    df_area = df_area.rename(columns={'OBS_VALUE': "area_[km2]"})
    
    # Drop the row for EU27
    df_pop = df_pop[df_pop['geo'] != "EU27_2020"]
    df_area = df_area[df_area['geo'] != "EU27_2020"]
    
    return df_pop, df_area


def merge_pop_and_area(df_pop, df_area):
    
    # Create dataframe with one row per country and aggregate demographic information
    df_countries = df_pop[['geo', 'population']].merge(df_area[['geo', 'area_[km2]']], how='inner', on='geo')
    country_codes_dict = get_country_codes_dict() # Get dictionary translating country codes to country names
    df_countries = df_countries.rename(columns={'geo': 'country_code'}) # Rename country code column
    df_countries['country_name'] = df_countries['country_code'].map(country_codes_dict) # Create column with country names
    
    return df_countries


def additional_columns_per_country(df_countries, df_main):
    
    # Add data about solar radiation classification
    eu_countries_solar_radiation_classification_dict = get_solar_class_dict() # Get dictionary with classification info
    df_countries['solar_class'] = df_countries['country_name'].map(eu_countries_solar_radiation_classification_dict)

    # Add data from df_main (solar electricity production)
    df_pivot = df_main.loc[(df_main["product"] == "Solar") & (df_main["year"] > 2013)].pivot_table(index="country_name", values="value", aggfunc="mean")*365
    df_countries = df_countries.merge(df_pivot, how='inner', on='country_name')
    df_countries = df_countries.rename(columns={'value': 'solar_power_[GWh]'})

    # Add data from df_main (total electricity production))
    df_pivot = df_main.loc[(df_main["product"] == "Electricity") & (df_main["year"] > 2013)].pivot_table(index="country_name", values="value", aggfunc="mean")*365
    df_countries = df_countries.merge(df_pivot, how='inner', on='country_name')
    df_countries = df_countries.rename(columns={'value': 'total_annual_electricity_[GWh]'})

    # Calculate solar power intensity (production per area)
    df_countries['solar_power_intensity_[GWh_per_km2]'] = df_countries['solar_power_[GWh]'] / df_countries["area_[km2]"]
    df_countries['solar_power_intensity_[GWh_per_1000_capita]'] = df_countries['solar_power_[GWh]'] / df_countries["population"] * 1000
    df_countries['solar_share_in_total_electricity_[%]'] = df_countries['solar_power_[GWh]'] / df_countries["total_annual_electricity_[GWh]"] * 100
    
    return df_countries


def get_color_dict():
    color_dict = {
    '1: very low': '#00FF00',
    '2: low': '#ADFF2F',
    '3: medium': '#FFFF00',
    '4: high': '#FFA500',
    '5: very high': '#FF0000'
    }
    return color_dict


def create_solar_radiation_map(df_countries, color_dict):
    fig = px.choropleth(df_countries.sort_values('solar_class'), 
                        locations='country_name', 
                        locationmode='country names',
                        color='solar_class', # categorize colors by solar class
                        color_discrete_map=color_dict, # apply specified colors to color categories
                        title='Country Categorization by Solar Radiation',
                        projection='natural earth',
                        scope='europe',
                        labels={'solar_class': 'Radiation Category'}) # Legend label

    fig.update_layout(height=600, width=800, showlegend=True, # set size of the figure
                    title={'y': 0.83, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'}) # place title in center of the map
    fig.show()


def create_solar_bar_chart_categories(df_countries, color_dict):
    df_pivot_class = df_countries.pivot_table(index="solar_class", values=["solar_power_intensity_[GWh_per_km2]"], aggfunc="mean")

    fig = px.bar(df_pivot_class, x=df_pivot_class.index, y="solar_power_intensity_[GWh_per_km2]",
                color=df_pivot_class.index,
                color_discrete_map=color_dict,
                title='Average Annual Solar Net Electricity Production per Area')

    fig.update_layout(height=500, width=800, showlegend=False,
                    title={'y': 0.85, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'})

    fig.update_xaxes(title_text="Solar Radiation Category")
    fig.update_yaxes(title_text="GWh/km²")

    fig.show()


def create_solar_bar_chart_countries(df_countries, color_dict):
    fig = px.bar(df_countries.sort_values(['solar_class', 'solar_power_intensity_[GWh_per_km2]']), x='country_name', y='solar_power_intensity_[GWh_per_km2]',
             color='solar_class',
             color_discrete_map=color_dict,
             labels={'solar_class': 'Radiation Category', 'country_code': "Country Code", 'solar_power_intensity_[GWh_per_km2]': 'Solar Electricity Production per km²'},
             title='Average Annual Solar Net Electricity Production per Area')

    fig.update_yaxes(range=[0, 7], title="GWh/km²")
    fig.update_xaxes(title_text="")
    fig.update_layout(height=450, width=800, showlegend=True,
                    title={'y': 0.85, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
                    legend={'y': 0.9, 'x': 0.15, 'xanchor': 'center', 'yanchor': 'top'})
    fig.update_xaxes(tickangle=-45)

    fig.show()


### FUNCTIONS FOR HYPOTHESIS 3 ###

# Clean main dataframe for hypothesis 3's analysis
def clean_RE_production(df):

    # filter only renewable energies products
    renewable_products = ["Total Renewables (Hydro, Geo, Solar, Wind, Other)", "Other Renewables"]

    df = df[df["product"].isin(renewable_products)].reset_index(drop=True)

    # change year into integer and filter the year into past 10 years
    df["year"].astype(int)
    df = df[(df["year"] > 2012) & (df["year"] < 2024)]
    df["value"] = df["value"].round(0).astype(int)

    # group the dataframe based on country_name and year
    df = df.groupby(["country_name", "year"])["value"].sum().reset_index()

    # rename value column with its unit for clearer understanding
    df = df.rename(columns={"value":"value_(GWh)"})
    
    # filter the dataframe with countries who have RnD budget
    countries_with_RnD_budget = ['Austria', 'Belgium', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Hungary', 'Ireland', 'Italy', 'Netherlands', 'Poland', 'Portugal', 'Slovak Republic', 'Spain', 'Sweden']

    df_RE_production = df[df["country_name"].isin(countries_with_RnD_budget)].reset_index(drop=True).round(0)

    return df_RE_production

# Clean R&D budget dataframe
def clean_RnD_budget(data_url):

    # read the excel file
    df_RnD = pd.read_excel(data_url)
    df = df_RnD.copy()

    # drop column of 2012
    df = df.drop(columns=2012)

    # drop rows which have more than 5 NaNs in the columns
    na_counts_per_row = df.isna().sum(axis=1)
    df = df[na_counts_per_row <= 5].reset_index(drop=True)

    # fill the NaN value with the value of left row
    df = df.apply(lambda row: row.ffill(axis=0), axis=1)
    df = df.rename(columns = {"Country ": "country_name"})

    # convert the dataframe into a long format for the visualization
    df = pd.melt(df, id_vars=["country_name"], var_name="year", value_name= 'budget')
    df["year"] = pd.to_numeric(df["year"])

    # rename budget column with its unit for clearer understanding
    df_RnD_budget = df.rename(columns={"budget":"budget_(million_Euro)"})
    
    return df_RnD_budget

# clean Population dataframe
def clean_population(data_url):

    # read the csv file
    df_population_original = pd.read_csv(data_url)
    df_population = df_population_original.copy()

    # drop unnecessary columns
    df_population = df_population.drop(columns=["DATAFLOW","LAST UPDATE","freq","indic_de","TIME_PERIOD","OBS_FLAG"])

    # rename column names
    df_population = df_population.rename(columns={"OBS_VALUE":"population"})
    
    # drop outlier
    df_population = df_population[df_population['geo'] != "EU27_2020"]

    # rename country code with country's full name using map
    country_codes_dict = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DE': 'Germany',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'EL': 'Greece',
    'ES': 'Spain',
    'FI': 'Finland',
    'FR': 'France',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IT': 'Italy',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'MT': 'Malta',
    'NL': 'Netherlands',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'SE': 'Sweden',
    'SI': 'Slovenia',
    'SK': 'Slovak Republic'}
    
    df_population["country_name"] = df_population["geo"].map(country_codes_dict)

    return df_population

# Merge RE production and population dataframe
def RE_production_per_capita(df_RE_production, df_population):

    # merge Renewable Energy production dataframe with population dataframe
    df_RE_production_per_capita = df_RE_production.merge(df_population, on='country_name', how='left')

    # convert data type in value column into int64
    df_RE_production_per_capita['value_(GWh)'] = df_RE_production_per_capita['value_(GWh)'].astype(np.int64)

    # create a new column to show value per capita as a result of calculation
    df_RE_production_per_capita["value_(kWh/capita)"] = (df_RE_production_per_capita["value_(GWh)"] * 1000000 / df_RE_production_per_capita["population"]).round(0).astype(np.int64) # result will be in kWh/capita

    return df_RE_production_per_capita

# Merge R&D production and population dataframe
def RnD_budget_per_capita(df_RnD_budget, df_population):
     
    # merge R&D budget dataframe with population dataframe
    df_RnD_budget_per_capita = df_RnD_budget.merge(df_population, on='country_name', how='left')

    # create a new column to show budget per capita as a result of calculation
    df_RnD_budget_per_capita["budget_(Euro/capita)"] = (df_RnD_budget_per_capita["budget_(million_Euro)"] * 1000000 / df_RnD_budget_per_capita["population"]).round(0).astype(np.int64) # result will be in Euro/capita

    return df_RnD_budget_per_capita

# Visualize correlation of RE production and R&D budget
def visualize_hypothesis_3(df_RE_production_per_capita, df_RnD_budget_per_capita):

    # merge df_RE_production dataframe with df_RnD_budget dataframe
    df = pd.merge(df_RE_production_per_capita, df_RnD_budget_per_capita, on=["country_name", "year", "geo", "population"])

    # find r for the trendline
    r, _ = pearsonr(df['budget_(Euro/capita)'], df['value_(kWh/capita)'])

    # create a scatter plot with trendline
    fig = px.scatter(
        df, 
        x="budget_(Euro/capita)", 
        y="value_(kWh/capita)", 
        color="year", 
        hover_name="country_name",
        trendline="ols", 
        template="simple_white", 
        title='RE Production vs R&D Budget per Capita in The Past 10 years'
    )

    # Extract the trendline results
    trendline = fig.data[1]  # The trendline is the second trace (index 1)

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

    fig.update_layout(
        xaxis_title="R&D Budget (Euro/capita)",
        yaxis_title="Renewable Energy Production (kWh/capita)",
        legend_title_text="Year"
    )

    return fig.show()

# Visualize RE production in the past 10 years 

def visualize_RE_production(df_RE_production_per_capita):
    
    # initialize the plot
    plt.figure(figsize=(10,6))

    # plot each country's data
    sns.lineplot(data=df_RE_production_per_capita, x=df_RE_production_per_capita["year"], y=df_RE_production_per_capita["value_(kWh/capita)"], hue=df_RE_production_per_capita["country_name"], marker='o')

    plt.title('Renewable Energy Adoption per Capita in The Past 10 years')
    plt.xlabel('Year')
    plt.ylabel('Energy production (kWh/capita)')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Set x-axis ticks to show every year
    plt.xticks(ticks=range(df_RE_production_per_capita['year'].min(), df_RE_production_per_capita['year'].max() + 1))

    # Adjusting text annotations
    texts = []
    for country in df_RE_production_per_capita['country_name'].unique():
        # Select the last year data point for each country to place the annotation
        subset = df_RE_production_per_capita[df_RE_production_per_capita['country_name'] == country]
        x = subset['year'].max()
        y = subset[subset['year'] == x]['value_(kWh/capita)'].values[0]
        texts.append(plt.text(x, y, country, fontsize=9, ha='right'))

    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

    return plt.show()


# Visualize R&D budget in the past 10 years

def visualize_RnD_budget(df_RnD_budget_per_capita):
    
    # initialize the plot
    plt.figure(figsize=(10,6))

    # plot each country's data
    sns.lineplot(data=df_RnD_budget_per_capita, x=df_RnD_budget_per_capita["year"], y=df_RnD_budget_per_capita["budget_(Euro/capita)"], hue=df_RnD_budget_per_capita["country_name"], marker='o')

    plt.title('R&D Budget per Capita in The Past 10 years')
    plt.xlabel('Year')
    plt.ylabel('Budget (Euro/capita)')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Set x-axis ticks to show every year
    plt.xticks(ticks=range(df_RnD_budget_per_capita['year'].min(), df_RnD_budget_per_capita['year'].max() + 1))

    # Adjusting text annotations
    texts = []
    for country in df_RnD_budget_per_capita['country_name'].unique():
        # Select the last year data point for each country to place the annotation
        subset = df_RnD_budget_per_capita[df_RnD_budget_per_capita['country_name'] == country]
        x = subset['year'].max()
        y = subset[subset['year'] == x]['budget_(Euro/capita)'].values[0]
        texts.append(plt.text(x, y, country, fontsize=9, ha='right'))

    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

    return plt.show()