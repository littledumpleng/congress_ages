#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Lauren Eng
Directory ID: 114761033
Date: 2020-12-14
Assignment: Homework 5
"""

""" 
Read a CSV file on energy production into a list of dictionaries.
Allow the user to specify which state's data they're interested in. 
The program should plot the MWH production values for wind and solar energy over time.
Command-line example: python3 hw5_template.py energy.csv MD 
"""

import csv
import sys
from matplotlib import pyplot as plt

datafile = sys.argv[1]
state = sys.argv[2].upper()
with open(datafile) as handle: #read file into a list of dictionaries
    reader = csv.DictReader(handle)
    
    wind_energy = []
    solar_energy = [] 
    wind_years = []
    solar_years = []
    for row in reader:
        if (row['State'] == state):
            # if (anything besides Total Electric Power Industry is True): skip
            if (row['Type of Producer'] == 'Total Electric Power Industry'):     
                if (row['Energy Source'] == "Wind"):
                    wind_energy.append(float(row['Megawatthours']))
                    wind_years.append(int(row['Year']))
                elif (row['Energy Source'] == "Solar Thermal and Photovoltaic"):
                    solar_energy.append(float(row['Megawatthours']))
                    solar_years.append(int(row['Year']))

    print("wind_energy", wind_energy)
    print("solar_energy", solar_energy)
    plt.title(f'Wind and Solar Energy Production in {state}')
    plt.plot(wind_years, wind_energy, label = "Wind")
    plt.plot(solar_years, solar_energy, label = "Solar")
    plt.title(f'Wind Energy Production in {state}')
    plt.xlabel('Years')
    plt.ylabel('Megawatthours')
    plt.legend(loc = 'upper left')
    plt.show()
