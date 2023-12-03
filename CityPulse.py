"""
File: CityPulse.py
Author: Daochen LI (daochenl)
Description: CityPulse complete application
"""

from crawlers import average_household_income, cost_of_living, employment_rate, health_care_index, pollution_index, recreation, safety_index
from data import data_processing
from gui import ui


if __name__ == "__main__":
    """
    imports crawlers, data processing and ui
    """
    
    print("Citypulse complete application")
    
    # Obtaining data
    average_household_income.fetch_income()
    employment_rate.fetch_employment()
    cost_of_living.crawl_cost()
    recreation.crawl_recreation()
    health_care_index.crawl_health()
    pollution_index.crawl_pollution()
    safety_index.crawl_safety_index()

    # Processing data
    data_processing.process_data()

    # User interface
    ui.launch()

    