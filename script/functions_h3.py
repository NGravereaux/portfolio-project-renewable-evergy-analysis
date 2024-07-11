import pandas as pd
import numpy as np
import seaborn as sns

# additional
import matplotlib.pyplot as plt
from adjustText import adjust_text
import plotly.express as px
from scipy.stats import pearsonr

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