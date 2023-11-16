"""
File: employment_rate.py
Author: Louie SUN (hongyuns), Daochen LI (daochenl)
Description: Retrieve city and employment rate data from Census using API
Website: https://data.census.gov
"""

import json
import pandas as pd
import requests

url_raw = ("https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,"
           "DP03_0004PE&for=place:*&in=state:*&key=f8579687edb9f7e019a2b54348ff323abd3a0a53")

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
    filtered_df.rename(columns={'DP03_0004PE': 'Employment Rate'}, inplace=True)
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

    mem_data = fetch_data("48000", "47")
    ba_data = fetch_data("4000", "24")
    de_data = fetch_data("22000", "26")
    al_data = fetch_data("02000", "35")
    sa_data = fetch_data("65000", "29")
    oa_data = fetch_data("53000", "06")
    mi_data = fetch_data("53000", "55")
    new_data = fetch_data("55000", "22")
    chi_data = fetch_data("14000", "17")
    phi_data = fetch_data("60000", "42")
    atl_data = fetch_data("04000", "13")
    hou_data = fetch_data("35000", "48")
    san_data = fetch_data("67000", "06")
    was_data = fetch_data("50000", "11")
    ind_data = fetch_data("36003", "18")
    por_data = fetch_data("60545", "23")
    las_data = fetch_data("40000", "32")
    min_data = fetch_data("43000", "27")
    sea_data = fetch_data("63000", "53")
    tuc_data = fetch_data("77000", "04")
    pho_data = fetch_data("55000", "04")
    mia_data = fetch_data("45000", "12")
    los_data = fetch_data("44000", "06")
    dal_data = fetch_data("19000", "48")
    col_data = fetch_data("19000", "13")
    ny_data = fetch_data("51000", "36")
    sac_data = fetch_data("64000", "06")
    orl_data = fetch_data("53000", "12")
    sana_data = fetch_data("65000", "48")
    hon_data = fetch_data("71550", "15")
    den_data = fetch_data("20000", "08")
    tam_data = fetch_data("71000", "12")
    aus_data = fetch_data("05000", "48")
    sand_data = fetch_data("66000", "06")
    bos_data = fetch_data("07000", "25")
    boi_data = fetch_data("08830", "16")
    sal_data = fetch_data("67000", "49")

    combined_data = pd.concat([mem_data, ba_data, de_data, al_data, sa_data, oa_data, mi_data, new_data, chi_data,
                            phi_data, atl_data, hou_data, san_data, was_data, ind_data, por_data,
                            las_data, min_data, sea_data, tuc_data, pho_data, mia_data, los_data,
                            dal_data, col_data, ny_data, sac_data, orl_data, sana_data, hon_data,
                            den_data, tam_data, aus_data, sand_data, bos_data, boi_data, sal_data], ignore_index=True)

    filename = './data/clean/employment_rate.csv'
    combined_data.to_csv(filename, index=False)

