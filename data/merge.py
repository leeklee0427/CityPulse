"""
File: merge.py
Author: Yanting HU (yantingh), Daochen LI (daochenl)
Description: Merge all cleaned data and write to csv
"""

import pandas as pd

def standardize_city_name(city_name):
    if '-' in city_name:
        return city_name.replace('-', ' ')
    return city_name

if __name__ == "__main__":
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
    merged_df = pd.merge(df1, df2, on=['City', 'State'], how='outer')
    merged_df = pd.merge(merged_df, df3, on=['City', 'State'], how='outer')
    merged_df = pd.merge(merged_df, df4, on=['City', 'State'], how='outer')
    merged_df = pd.merge(merged_df, df5, on=['City', 'State'], how='outer')
    merged_df = pd.merge(merged_df, df6, on=['City', 'State'], how='outer')
    merged_df = pd.merge(merged_df, df7, on=['City', 'State'], how='outer')

    # write merged data to csv
    filename = './data/merged_data.csv'
    print("Writing merged data to " + filename)
    merged_df.to_csv(filename, index=False)