"""
File: safety_index.py
Author: Daochen LI (daochenl)
Date: 2023-11-11
Description: Scrape city and safety index data from Numbeo.com
Website: https://www.numbeo.com/crime/rankings_current.jsp
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
        writer.writerow(['City', 'State', 'Safety Index']) # write the header
        writer.writerows(data) # write raw data to file

if __name__ == "__main__":

    # Define the URL of the website you want to scrape
    url = 'https://www.numbeo.com/crime/rankings_current.jsp'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser') # parse the HTML content of the page using BeautifulSoup
        
        table_list = soup.findAll('table') # get a list of all table tags
        print('there are', len(table_list), 'tables')
        
        table = table_list[1] # get second table with the data

        with open("./data/raw/safety_index_raw.txt", 'w') as file:
            file.write(str(table)) # write the string to the file

        rows = table.findAll('tr')
        print('there are', len(rows), 'table rows')

        headers = rows[0].findAll('th') # row 0 contains column headers
        print('there are', len(headers), 'columns')

        # print headers
        # for h in headers:
        #     print(h.div.get_text(strip=True))

        safety_index_dict = {}
        for row in rows[1:]:
            row_data = row.findAll('td')

            city = row_data[1].contents[0].contents[0] # retrieve city
            safety_index = row_data[3].contents[0] # retrieve safety index of city
            
            safety_index_dict[city] = safety_index

        # for city, safety_index in safety_index_dict.items():
        #     print("City:", city)
        #     print("Safety Index:", safety_index)
        
        # Keep only cities in the United States
    
        city_state_safety = []
        for city, safety_index in safety_index_dict.items():
            city_parts = city.split(",")
            if "United States" in city:
                filtered_city = city_parts[0] + city_parts[1]
                #safety_index_dict_[filtered_city] = safety_index
                city_state_safety.append([city_parts[0].strip(), city_parts[1].strip(), safety_index])

        # for city, safety_index in safety_index_dict_.items():
        #         print("City: ", city)
        #         print("Safety Index: ", safety_index)

        # safety_index_list = [[key, value] for key, value in safety_index_dict_.items()]
        
        filename = "./data/clean/safety_index.csv"
        print("Writing to " + filename)
        write_csv(filename, city_state_safety)
    
    else:
        print("Failed to retrieve the web page. Status code: ", response.status_code)

        