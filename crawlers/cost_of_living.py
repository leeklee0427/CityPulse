"""
File: cost_of_living.py
Author: Yanting HU (yantingh), Daochen LI (daochenl)
Description: Retrieve city and cost of living (in percentage compared to national average) from Salary.com
Note: This might take a few longer than other crawlers
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
        writer.writerow(['City', 'State', 'Cost']) # write the header
        writer.writerows(data) # write all rows in the list data


def crawl_cost():
    
    print("Crawling cost...")

    cities_states = {
        'tampa':'fl', 'orlando':'fl', 'austin':'tx', 'san-antonio':'tx', 'charlotte':'nc', 
        'raleigh':'nc', 'columbus':'oh', 'boston':'ma', 'portland':'or', 'kansas-city':'mo', 
        'pittsburgh':'pa', 'sacramento':'ca', 'san-diego':'ca', 'dallas':'tx', 'tucson':'az',
        'seattle':'wa', 'minneapolis':'mn', 'denver':'co', 'atlanta':'ga', 'salt-lake-city':'ut',
        'honolulu':'hi', 'miami':'fl', 'albuquerque':'nm', 'san-jose':'ca', 'philadelphia':'pa',
        'phoenix':'az', 'las-vegas':'nv', 'houston':'tx', 'chicago':'il', 'washington':'dc', 
        'san-francisco':'ca', 'new-york':'ny', 'los-angeles':'ca'
        }

    # URL template with placeholders for city and state
    template = 'https://www.salary.com/research/cost-of-living/{}-{}'

    city_state_cost_of_living = []

    # Loop through all city-state pairs
    for city, state in cities_states.items():

        url = template.format(city, state)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            percent_span = soup.find('span', class_='percent-color')
            
            if percent_span:
                percent_value = percent_span.get_text(strip=True).split()[0].rstrip('%') # Percentage symbol removed
                
                # Add the city, state, and percent value to the list
                city_state_cost_of_living.append([city.title(), state.upper(), percent_value])

            else:
                print(f'Percent value not found for {city.title()}, {state.upper()}.')
        else:
            print(f'Request failed for {city.title()}, {state.upper()}, Status Code:', response.status_code)

    # Write clean data to csv
    filename = './data/clean/cost_of_living.csv'
    print("Writing to " + filename)
    write_csv(filename, city_state_cost_of_living)


if __name__ == "__main__":
    crawl_cost()
    
