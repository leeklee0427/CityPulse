"""
File: employment_rate.py
Author: Louie SUN (hongyuns), Daochen LI (daochenl)
Description: Retrieve city and employment rate data from Census using API

Website:
https://data.census.gov
https://www.census.gov/library/reference/code-lists/ansi.html#place
"""

import json
import pandas as pd
import requests

url_raw = ("https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,"
           "DP03_0004PE&for=place:*&in=state:*&key=f8579687edb9f7e019a2b54348ff323abd3a0a53")

def format_specific_cities(df):
    city_replacements= {
        'Indianapolis (balance)': 'Indianapolis', 'Urban Honolulu CDP': 'Honolulu', 'Boise City': 'Boise',
        'St. Louis': 'Saint Louis'
    }
    for original, new_format in city_replacements.items():
        df['City'] = df['City'].str.replace(original, new_format, regex=False)

    return df

def split_name(name):
    city, state_name = name.split(", ")
    return pd.Series([city.strip(), state_name.strip()])

def convert_state_name_to_abbreviation(state_name):
    return cities_states.get(state_name, state_name)

def format_city_names(df):
    df['City'] = df['City'].str.replace(" city", "", regex=False)
    return df

def fetch_data(place_code, state_code):
    df = pd.read_csv("./data/raw/employment_rate_raw.csv")
    filtered_df = df.loc[(df['state'] == int(state_code)) & (df['place'] == int(place_code))].copy()
    split_names = filtered_df['NAME'].str.split(", ", expand=True)
    filtered_df['City'] = split_names[0].str.strip()
    filtered_df['State'] = split_names[1].str.strip()
    filtered_df.rename(columns={'DP03_0004PE': 'Employment'}, inplace=True)
    #filtered_df.rename(columns={'DP03_0063E': 'Average Household Income'}, inplace=True)
    filtered_df.drop(columns=['state', 'place'], inplace=True)
    filtered_df = filtered_df.drop(columns=['NAME', 'Unnamed: 0'])
    column_order = ['City', 'State'] + [col for col in filtered_df.columns if col not in ['City', 'State']]
    filtered_df = filtered_df[column_order]
    filtered_df['State'] = filtered_df['State'].apply(convert_state_name_to_abbreviation)
    filtered_df = format_city_names(filtered_df)
    return filtered_df

if __name__ == "__main__":

    cities_states = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', 'District of Columbia': 'DC'
    }
    
    response_raw = requests.get(url_raw)

    if response_raw.status_code == 200:
        try:
            data_raw = response_raw.json()
            df_raw = pd.DataFrame(data_raw[1:], columns=data_raw[0])
            df_raw.to_csv("./data/raw/employment_rate_raw.csv")
        except json.JSONDecodeError:
            print("Error decoding JSON")
    else:
        print("Error fetching data:", response_raw.status_code)

    locations = {
        "mem": ("48000", "47"),
        "ba": ("4000", "24"),
        "de": ("22000", "26"),
        "al": ("02000", "35"),
        "sa": ("65000", "29"),
        "oa": ("53000", "06"),
        "mi": ("53000", "55"),
        "new": ("55000", "22"),
        "chi": ("14000", "17"),
        "phi": ("60000", "42"),
        "atl": ("04000", "13"),
        "hou": ("35000", "48"),
        "san": ("67000", "06"),
        "was": ("50000", "11"),
        "ind": ("36003", "18"),
        "por": ("60545", "23"),
        "las": ("40000", "32"),
        "min": ("43000", "27"),
        "sea": ("63000", "53"),
        "tuc": ("77000", "04"),
        "pho": ("55000", "04"),
        "mia": ("45000", "12"),
        "los": ("44000", "06"),
        "dal": ("19000", "48"),
        "col": ("19000", "13"),
        "ny": ("51000", "36"),
        "sac": ("64000", "06"),
        "orl": ("53000", "12"),
        "sana": ("65000", "48"),
        "hon": ("71550", "15"),
        "den": ("20000", "08"),
        "tam": ("71000", "12"),
        "aus": ("05000", "48"),
        "sand": ("66000", "06"),
        "bos": ("07000", "25"),
        "boi": ("08830", "16"),
        "sal": ("67000", "49"),
        "charlotte": ("12000", "37"),
        "raleigh": ("55000", "37"),
        "columbus": ("18000", "39"),
        "portland": ("59000", "41"),
        "kansas": ("38000", "29"),
        "pittsburgh": ("61000", "42"),
        "sanjose": ("68000", "06"),
        "madison": ("48000", "55")
    }

    combined_data = pd.concat([fetch_data(code[0], code[1]) for code in locations.values()], ignore_index=True)
    combined_data = format_specific_cities(combined_data)
    
    filename = './data/clean/employment_rate.csv'
    combined_data.to_csv(filename, index=False)

