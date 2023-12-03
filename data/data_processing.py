"""
File: data_processing.py
Author: Yanting HU (yantingh), Daochen LI (daochenl)
Description: Merge all data, fill na, and write data to multiple files
"""

import pandas as pd
from tabulate import tabulate

def standardize_city_name(city_name):
    if '-' in city_name:
        return city_name.replace('-', ' ')
    return city_name

def process_data():

    print("Processing data...")

    ### Merging data
    # dataframes for merge
    df1 = pd.read_csv('./data/clean/average_household_income.csv')
    df2 = pd.read_csv('./data/clean/employment_rate.csv')
    df3 = pd.read_csv('./data/clean/cost_of_living.csv')
    df4 = pd.read_csv('./data/clean/safety_index.csv')
    df5 = pd.read_csv('./data/clean/health_care_index.csv')
    df6 = pd.read_csv('./data/clean/pollution_index.csv')
    df7 = pd.read_csv('./data/clean/recreation.csv')

    # standardize city names
    df1['City'] = df1['City'].apply(standardize_city_name)
    df2['City'] = df2['City'].apply(standardize_city_name)
    df3['City'] = df3['City'].apply(standardize_city_name)
    df4['City'] = df4['City'].apply(standardize_city_name)
    df5['City'] = df5['City'].apply(standardize_city_name)
    df6['City'] = df6['City'].apply(standardize_city_name)
    df7['City'] = df7['City'].apply(standardize_city_name)

    # merge
    df = pd.merge(df1, df2, on=['City', 'State'], how='outer')
    df = pd.merge(df, df3, on=['City', 'State'], how='outer')
    df = pd.merge(df, df4, on=['City', 'State'], how='outer')
    df = pd.merge(df, df5, on=['City', 'State'], how='outer')
    df = pd.merge(df, df6, on=['City', 'State'], how='outer')
    df = pd.merge(df, df7, on=['City', 'State'], how='outer')

    # write df to csv
    merged_path = './data/display/merged_data.csv'
    print("Writing merged data to " + merged_path)
    df.to_csv(merged_path, index=False)


    ### Filling na
    # Fill Cost column with Median
    df['Cost'].fillna(df['Cost'].median(), inplace=True)

    # Fill other columns with Mean
    for column in ['Safety', 'Medical', 'Pollution', 'Recreation']:
        df[column].fillna(df[column].mean(), inplace=True)
    #print(df)


    ### Write data
    # Write cleaned data to csv
    cleaned_path = './data/display/cleaned_data.csv'
    print("Writing cleaned data to " + cleaned_path)
    df.to_csv(cleaned_path, index=False)

    # Use tabulate to display the table
    data_dict_list = df.to_dict(orient='records') # Convert DataFrame to a list of dictionaries
    table = tabulate(data_dict_list, headers="keys", tablefmt="grid")
    #print(table)
    
    # Write tabulated data to txt
    tabulated_path = './data/display/tabulated_data.txt'
    print("Writing cleaned data to " + tabulated_path)
    with open(tabulated_path, 'wt') as fout:
        fout.write(table)

    print("Data is all set")


if __name__ == "__main__":
    process_data()

