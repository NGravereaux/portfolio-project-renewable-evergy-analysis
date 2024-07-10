import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Get Solar Radiation Classification Dictionnary for all EU Countries
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