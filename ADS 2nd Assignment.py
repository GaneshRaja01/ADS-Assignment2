# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:15:32 2023

@author: rgane
"""

import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt


def read_file(filename):
    """
    This function is designed to read data and provide a pandas dataframe
    object as its output
    """
    #Read csv file by using pandas
    dataframe = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)
    return dataframe


def filter_file(dataframe, column, value, countries, years):
    """
   By using this function, you can filter data and receive a dataframe as well
   as the transpose of the dataframe.
    """
    # Groups data with column value
    filtered_data = dataframe.groupby(column, group_keys=True)
    # Getting the data
    filtered_data = filtered_data.get_group(value)
    # Resets the index
    filtered_data = filtered_data.reset_index()
    #The filtered_data is being modified to the country name as its new index
    filtered_data.set_index('Country Name', inplace=True)
    filtered_data = filtered_data.loc[:, years]
    filtered_data = filtered_data.loc[countries, :]
    # Dataframe drops NAN values
    filtered_data = filtered_data.dropna(axis=1)
    filtered_data = filtered_data.reset_index()
    # Transposing the index of the dataframe
    transposed_data = filtered_data.set_index('Country Name')
    transposed_data = transposed_data.transpose()
    # Returns normal dataframe and transposed dataframe
    return filtered_data, transposed_data


def statis_data(dataframe, col, value, yr, a):
    """
    This function is designed to read a dataframe with multiple indicators
    and then generate a new dataframe that is suitable for 
    constructing a Heat Map.
    """
    # Dataframe's rows are being grouped based on values in the "col" column
    df3 = dataframe.groupby(col, group_keys=True)
    # Getting the data with group_by element
    df3 = df3.get_group(value)
    # Resets the index of the dataframe
    df3 = df3.reset_index()
    df3.set_index('Indicator Name', inplace=True)
    df3 = df3.loc[:, yr]
    #transposing the index of the dataframe
    df3 = df3.transpose()
    df3 = df3.loc[:, a]
    return df3


def line(dataset, title, xlab, ylab):
    """ 
    The purpose of this function is to generate a line plot as its output.
    """
    # DataFrame creates a line plot from the dataset
    dataset.plot.line(figsize=(50, 30), fontsize=60, linewidth=6.0)
    # Sets the location of the y-axis ticks
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    # Sets title and font size for plot
    plt.title(title.upper(), fontsize=70, fontweight='bold')
    # Sets x-label and font size for plot axes
    plt.xlabel(xlab, fontsize=70)
    # Sets y-label and font size for plot axes
    plt.ylabel(ylab, fontsize=70)
    plt.legend(fontsize=60)
    # Saves line plot figure as png
    plt.savefig(title + '.png')
    # Function to show the plot
    plt.show()
    return


def bar(dataset, title, xlab, ylab):
    """ 
    The purpose of this function is to generate a bar plot as its output.
    """
    # Creates a bar plot from the dataset DataFrame
    dataset.plot.bar(x='Country Name', rot=0, figsize=(50, 25),
                     fontsize=50)
    # Sets the location of the y-axis ticks
    plt.yticks([0, 20, 40, 60, 80, 100])
    plt.legend(fontsize=50)
    # Sets title and font size for plot
    plt.title(title.upper(), fontsize=60, fontweight='bold')
    # Sets x-label and font size for plot axes
    plt.xlabel(xlab, fontsize=60)
    # Sets y-label and font size for plot axes
    plt.ylabel(ylab, fontsize=60)
    # Saves bar plot figure as png
    plt.savefig(title + '.png')
    # Function to show the plot
    plt.show()
    return


def heat_map(data):
    """
    This function is used for visualizing the correlation 
    between various indicators.
    """
    plt.figure(figsize=(80, 40))
    sns.heatmap(data.corr(), annot=True, annot_kws={"size": 32})
    plt.title("Brazil's Heatmap".upper(), size=40, fontweight='bold')
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=30)
    plt.yticks(rotation=0, fontsize=30)
    #saving Heatmap image as png
    plt.savefig('Heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    return data


# Creating list of countries and years for plotting bar plot
country1 = ['Malaysia', 'India', 'New Zealand', 'Philippines']
year1 = ['2000', '2005', '2010', '2015', '2020']
# Reads data from csv file
world_data = read_file("climate_change.csv")
world_data1, transdata1 = filter_file(
    world_data, 'Indicator Name', 'CO2 emissions from solid fuel consumption (% of total)', country1, year1)
# Prints filtered data and transposed data
print(world_data1)
print(transdata1)
# Calling bar plot function with indicator as Urban Population
bar(world_data1, 'CO2 emissions from solid fuel consumption (% of total))',
    'Countries', 'Percentage of CO2 emissions')

world_data2, transdata2 = filter_file(
    world_data, 'Indicator Name', 'Access to electricity (% of population)',
    country1, year1)
# Prints filtered data and transposed data
print(world_data2)
print(transdata2)

# Calling another bar plot function with indicator as Access to electricity
bar(world_data2, 'Access to Electricity (% of population)',
    'Countries', 'Percentage of Electricity access')
# Creating list of countries and years for plotting line plot
country2 = ['Malaysia', 'India', 'New Zealand', 'Philippines']
year2 = ['2000', '2005', '2010', '2015', '2020']
world_data3, transdata3 = filter_file(
    world_data, 'Indicator Name', 'Agricultural land (% of land area)',
    country2, year2)
# Prints filtered data and transposed data
print(world_data3)
print(transdata3)

# Calling line plot function with indicator as Agricultural land
line(transdata3, 'Agricultural land (% of land area)',
     'Year', '% of Agricultural land')

world_data4, transdata4 = filter_file(
    world_data, 'Indicator Name',
    'Renewable energy consumption (% of total final energy consumption)',
    country2, year2)
# Prints filtered data and transposed data
print(world_data4)
print(transdata4)

# Calling another line plot function with indicator as Forest land
line(transdata4, 'Renewable energy consumption (% of total final energy consumption)',
     'Year', '% of Renewable energy consumption')

# initializing a variable  year_heat with years
year_heat = ['2000', '2004', '2008', '2012', '2016']
#creating a variable indicators for HeatMap
indicators = ['Renewable energy consumption (% of total final energy consumption)',
              'Agricultural land (% of land area)',
              'CO2 emissions from solid fuel consumption (% of total)',
              'Access to electricity (% of population)', 'Cereal yield (kg per hectare)',
              'Annual freshwater withdrawals, total (% of internal resources)']
dataheat = statis_data(world_data, 'Country Name',
                       'Brazil', year_heat, indicators)
print(dataheat.head())
#Calling a function to create heatmap
heat_map(dataheat)

start = 2000
end = 2020
yeardes = [str(i) for i in range(start, end+1)]
indicator2 = ['Population growth (annual %)',
              'Electricity production from oil sources (% of total)',
              'Electricity production from nuclear sources (% of total)',
              'Electricity production from natural gas sources (% of total)']
descr = statis_data(world_data, 'Country Name',
                    'United Arab Emirates', yeardes, indicator2)
# returns a summary of descriptive statistics for a dataset
stats_summary = descr.describe()
print(stats_summary)
skewness = stats.skew(descr['Population growth (annual %)'])
kurtosis = descr['Electricity production from oil sources (% of total)'].kurtosis(
)
print('Skewness of Population growth in United Arab Emirates : ', skewness)
print('Kurtosis of Electricity production from natural gas in United Arab Emirates : ', kurtosis)
# saves result to a csv file
stats_summary.to_csv('statistics_report.csv')
