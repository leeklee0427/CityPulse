"""
File: recreation.py
Author: Yanting HU (yantingh), Daochen LI (daochenl)
Description: Retrieve city and recreation total score data from WalletHub.com
"""

import csv
from bs4 import BeautifulSoup
import requests


def write_csv(filename, data):
    """
    Write data to a CSV file with a specific format.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'State', 'Recreation']) # write the header
        writer.writerows(data) # write all rows in the list data

cities_states = {'tampa':'fl', 'orlando':'fl', 'austin':'tx', 'san-antonio':'tx', 'charlotte':'nc', 
                'raleigh':'nc', 'columbus':'oh', 'boston':'ma', 'portland':'or', 'kansas-city':'mo', 
                'pittsburgh':'pa', 'sacramento':'ca', 'san-diego':'ca', 'dallas':'tx', 'tucson':'az',
                'seattle':'wa', 'minneapolis':'mn', 'denver':'co', 'atlanta':'ga', 'salt-lake-city':'ut',
                'honolulu':'hi', 'miami':'fl', 'albuquerque':'nm', 'san-jose':'ca', 'philadelphia':'pa',
                'phoenix':'az', 'las-vegas':'nv', 'houston':'tx', 'chicago':'il', 'washington':'dc', 
                'san-francisco':'ca', 'new-york':'ny', 'los-angeles':'ca'}

cities = []
states = []
scores = []

city_state_recreation = []

url = 'https://wallethub.com/edu/best-worst-cities-for-recreation/5144'
response = requests.get(url)

if response.status_code == 200:
    print("HTTP request successful.")
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    # Loop through each row and extract the city, state, and corresponding score
    for row in rows:
        data = row.find_all('td')
        if data: # Check if there is data
            city_state = data[1].get_text().strip()
            score = data[2].get_text().strip()

            # Split city and state
            city, state = city_state.split(', ')

            # Add the data to the respective lists
            cities.append(city)
            states.append(state)
            scores.append(score)

    cities_states_ = {c.replace("-", " ").lower(): s for c, s in cities_states.items()}
    filtered_cities = [c for c in cities if c.lower() in cities_states_.keys()]

    for city in filtered_cities:
        i = cities.index(city)
        state = states[i]
        score = scores[i]
        city_state_recreation.append([city, state.upper(), score])
    
    # Write the result to a CSV file
    filename = './data/clean/recreation.csv'
    print("Writing to " + filename)
    write_csv(filename, city_state_recreation)

else:
    print("Failed to retrieve the page")