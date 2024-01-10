#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:48:58 2024

@author: saikiranakula
"""
import pandas as pd
import matplotlib.pyplot as plt

# Assuming the data is in an Excel file named 'IG1.xlsx'
file_name = 'IG1.xlsx'  # Replace with the actual path
my = pd.read_excel(file_name)

# Define two colors for the bars
colors = ['skyblue', 'coral']

# Plotting the horizontal bar graph with two colors
plt.figure(figsize=(10, 6))
bars = plt.barh(my['CountryName'], my['Year[2020]'], color=colors)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Adding special effects
plt.title('Access to Electricity - 2020', fontsize=17, fontweight='bold')
plt.xlabel('Access to Electricity (% of Population)', fontsize=17)
plt.ylabel('Country', fontsize=17)

# Adding data values on each bar
for bar in bars:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center', color='black')

plt.savefig('22098314.png',dpi=300)


# Assuming the data is in an Excel file named 'IG 2.xlsx'
file_name = 'IG 2.xlsx'  # Replace with the actual path
my = pd.read_excel(file_name)

# Set a color palette for better visibility of multiple lines
colors = plt.cm.tab10.colors

# Plotting the line plot
plt.figure(figsize=(10, 6))

# Iterate over unique countries and plot a line for each
for i, country in enumerate(my['CountryName'].unique()):
    country_set = my[my['CountryName'] == country]
    plt.plot(country_set['Year'], country_set['Electricity production from oil sources(% of total)'],
             label=country, color=colors[i], marker='o', linestyle='-', linewidth=2)

plt.title('Sources (% of Total)', fontsize=17, fontweight='bold')
plt.xlabel('Year', fontsize=17)
plt.ylabel('Electricity Production (% of Total)', fontsize=17)
plt.legend()

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.5)

# Add a background color for better contrast
plt.axhspan(0, 100, facecolor='lightgray', alpha=0.1)


plt.savefig('22098314.png',dpi=300)


# Assuming the data is in an Excel file named 'IG 3.xlsx'
file_name = 'IG 3.xlsx'  # Replace with the actual path
my = pd.read_excel(file_name)

# Define two colors for the bars
colors = ['teal', 'yellow']

# Plotting the horizontal bar graph with two colors
plt.figure(figsize=(10, 6))
hbars = plt.barh(my['CountryName'], my['Year [2014]'], color=colors)

# Add grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adding data values on each bar
for bar in hbars:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), ha='left', va='center', color='black')

plt.savefig('22098314.png',dpi=300)

# Adding labels and title
plt.xlabel('Electric power transmission and distribution losses (% of output)',fontsize=16)
plt.title('Electric Power Transmission and Distribution Losses - 2014',fontsize=16, fontweight='bold')
plt.ylabel('Country',fontsize=16)

plt.savefig('22098314.png',dpi=300)


# Assuming the data is in an Excel file named 'IG 4r.xlsx'
file_name = 'IG4.xlsx'
my = pd.read_excel(file_name)

# Filter the data for a specific country (India in this case)
data_set = my[my['Country'] == 'India']

# Separate the data into labels and corresponding values
labels = data_set['Indicator Name']
values = data_set['Year[2014]']

# Define colors for the pie chart
colors = plt.cm.Paired.colors

# Explode a specific slice (e.g., 'Coal')
explode = [0.1 if label == 'Coal' else 0 for label in labels]

# Plotting the pie chart with special effects
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, shadow=True, explode=explode)

# Adding a legend
plt.legend(labels, loc='upper right', bbox_to_anchor=(1, 0.9))

# Adding a title
plt.title('Energy Consumption Distribution in India - 2014', fontsize=17, fontweight='bold')

plt.savefig('22098314.png',dpi=300)