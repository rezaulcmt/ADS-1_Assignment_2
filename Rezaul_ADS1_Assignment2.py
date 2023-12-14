# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:42 2023

@author: Md Rezaul Karim
Student ID: 22094702
"""

# Import  libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from file
data = pd.read_excel('climate.xlsx')

# Display summary statistics of the dataset
print(data.describe())


def line_plot(data):
    """Select data for a specific county ('Botosani') and plot annual precipitation over the years
Args:
    data (pandas dataframe): data
"""

    # Select data for the Botosani county or country from the given dataset
    county_data = data[data['County/Country'] == 'Botosani']
    # Plotting the annual precipitation over the specified period
    plt.plot(county_data['Period'], county_data['Annual'])
    plt.xlabel('Year')
    plt.ylabel('Annual Precipitation')
    plt.title('Annual Precipitation in Botosani (1901-1930)')
    plt.xticks(rotation=45)
    plt.show()


def bar_plot(data):
    """Select data for a specific month ('Jan') and plot precipitation by County/Country using a bar plot
Args:
    data (pandas dataframe): data
"""
    month = 'Jan'

    # Selecting the first 8 rows of the DataFrame and show the precipitation in january
    selected_data = data.head(8)

    # create the bar chart for the selected countries
    selected_data.plot(kind='bar', x='County/Country', y=month, legend=None)
    plt.xlabel('County/Country')
    plt.ylabel(f'Precipitation in {month}')
    plt.title(f'Precipitation in {month} by County/Country')
    plt.xticks(rotation=45)
    plt.show()


def hist_plot(data):
    """Plot a histogram of the distribution of annual precipitation
Args:
    data (pandas dataframe):data
"""

    data['Annual'].hist(bins=20)
    plt.xlabel('Annual Precipitation')
    plt.ylabel('Frequency')
    plt.title('Distribution of Annual Precipitation')
    plt.show()


# Call 3 types of plot to show
line_plot(data)
bar_plot(data)
hist_plot(data)
