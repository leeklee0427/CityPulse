"""
File: pollution_index.py
Author: Daochen LI (daochenl)
Date: 2023-11-11
Description: Scrape city and pollution exp index data from Numbeo.com
Website: https://www.numbeo.com/pollution/rankings_current.jsp
"""

import csv
import requests
from bs4 import BeautifulSoup

def write_csv(filename, data):
    """
    Write data to a CSV file with a specific format.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'State', 'Pollution']) # write the header
        writer.writerows(data) # write all rows in the list data

def crawl_pollution():
    
    print("Crawling pollution...")
    
    # Define the URL of the website you want to scrape
    url = 'https://www.numbeo.com/pollution/rankings_current.jsp'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser') # parse the HTML content of the page using BeautifulSoup
        
        table_list = soup.findAll('table') # get a list of all table tags
        #print('there are', len(table_list), 'tables')
        
        table = table_list[1] # get second table with the data

        with open("./data/raw/pollution_index_raw.txt", 'w') as file:
            file.write(str(table)) # write raw data to file

        rows = table.findAll('tr')
        #print('there are', len(rows), 'table rows')

        headers = rows[0].findAll('th') # row 0 contains column headers
        #print('there are', len(headers), 'columns')

        # print headers
        # for h in headers:
        #     print(h.div.get_text(strip=True))

        pollution_index_dict = {}
        for row in rows[1:]:
            row_data = row.findAll('td')

            city = row_data[1].contents[0].contents[0] # retrieve city
            pollution_index = row_data[3].contents[0] # retrieve exp pollution index of city

            pollution_index_dict[city] = pollution_index

        # for city, index in pollution_index_dict.items():
        #     print("City:", city)
        #     print("Exp Pollution Index:", index)
        
        # Keep only cities in the United States
        # pollution_index_dict_ = {}
        city_state_pollution = []
        for city, index in pollution_index_dict.items():
            city_parts = city.split(",")
            if "United States" in city:
                filtered_city = city_parts[0] +  city_parts[1]
                # pollution_index_dict_[filtered_city] = index
                city_state_pollution.append([city_parts[0].strip(), city_parts[1].strip(), index])

        # for city, index in pollution_index_dict_.items():
        #         print("City: ", city)
        #         print("Exp Pollution Index: ", index)

        # pollution_index_list = [[key, value] for key, value in pollution_index_dict_.items()]
        
        filename = "./data/clean/pollution_index.csv"
        print("Writing to " + filename)
        write_csv(filename, city_state_pollution)
    
    else:
        print("Failed to retrieve the web page. Status code: ", response.status_code)


if __name__ == "__main__":
    crawl_pollution()

