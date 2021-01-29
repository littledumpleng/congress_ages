#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Lauren Eng
Directory ID: 114761033
Date: 2020-12-17
Assignment: Final Program
"""

"""
Create a program that processes data queried from the ProPublica Congress API and creates a visualization of that data using matplotlib.
The graph will display the average ages of the membership of each category for the requested sessions of Congress.
There should be six separate plots: House, Senate, Democrat, Republican, male, female.

Example input: "python3 congress_data.py key.txt 112-114"
"""

import requests
import sys
from matplotlib import pyplot as plt


def get(url, key): 
    headers = {"X-API-KEY": key}
    url = "http://api.propublica.org/congress/v1" + url #querying version 1 of API # + url is variable
    print(f"Querying {url}...")
    data = requests.get(url, headers = headers).json() #gets full-text html of url's webpage. pass in headers dictionary containing API key. converts to json
    return data['results']

class Member():
    def __init__(self, **kwargs): #keyword argument - provides a name to the variable as you pass it into the function
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.gender = kwargs.get('gender')
        self.party = kwargs.get('party')

    def calculate_age(self, year):
        if #sys number specified for: 
            member_age = year - self.date_of_birth
        for number in session_range.values(): #.values() returns a list object containing dictionary values
            congresses.append(member_age) #list of congressional sessions

#Optional Session()
class Session():
    
    sessions = { "102": 1991, "103": 1993, "104": 1995, "105": 1997, "106": 1999,
             "107": 2001, "108": 2003, "109": 2005, "110": 2007, "111": 2009,
             "112": 2011, "113": 2013, "114": 2015, "115": 2017, "116": 2019
             } #class variable - available on all instances of Session()
    
    def __init__(self, number, sessions): #number of sessions
        self.number = str(number) #102 = 102
        self.year = sessions[self.number]
        self.all_members = [] #members of each session

#         for chamber in ('house', 'senate'):
#             #call the get function with the appropriate url string
#             response = get(f"/{self.number}/{chamber}/members.json") # NO VALUE FOR KEY ARGUMENT?
#             for ppdata in response['members']: #what does this do
#                 session_member = Member(**ppdata) #what does this do
#                 session_member.age = session_member.calculate_age(self.year) #store age on member object
#                 self.all_members.append(session_member)
    
    def member_ages_filter_by(self, criterion):
        if criterion == "house":
            return [session_member.age for session_member in self.all_members if session_member.chamber == 'house']
        if criterion == "senate":
            return [session_member.age for session_member in self.all_members if session_member.chamber == 'senate']
        if criterion == "democrat":
            return [session_member.age for session_member in self.all_members if session_member.party == 'D']
        if criterion == "republican":
            return [session_member.age for session_member in self.all_members if session_member.party == 'R']
        if criterion == "male":
            return [session_member.age for session_member in self.all_members if session_member.gender == 'M']
        if criterion == "female":
            return [session_member.age for session_member in self.all_members if session_member.gender == 'F']

if __name__ == "__main__":
    #two arguments: key, session_range
    keypath = sys.argv[1]
    session_range = sys.argv[2]

    # verify that variables are valid
    range_split = session_range.split("-")

    start_range = int(range_split[0])
    end_range = int(range_split[1])

    if ((start_range < 102) or (start_range > 116)):
        print("Invalid session input. Please try again.")
    else:
        calculate_age()
        member_ages_filter_by()

    # f = open("key.txt", "r")
    # apiKey = f.read()

    # for congress in range(start_range, end_range):
    #     # year = insert year here
    #     for chamber in ('house', 'senate'):
    #         url = f"/{congress}/{chamber}/members.json"
    #         results = get(url, apiKey)


    plots = {"House": [],
            "Senate": [],
            "Democrat": [],
            "Republican": [],
            "Male": [],
            "Female": [],
            }

    years = []
    
    #query all of the endpoints for the requested range of sessions
    for number in session_range: #the number of the congress within the session_range
        session = Session(number)
        years.append(session.year)

        years.append(session.year)
        for criterion, average_ages in plots.items():
            ages = session.member_ages_filter_by(criterion)
            plots[criterion].append(sum(ages)/len(ages)) #plot the criterion average


    #GRAPH
    plt.plot(plots['House'], years, label = "House of Representatives")
    plt.plot(plots['Senate'], years, label = "Senate")
    plt.plot(plots['Democrat'], years, label = "Democrat")
    plt.plot(plots['Republican'], years, label = "Republican")
    plt.plot(plots['Male'], years, label = "Male")
    plt.plot(plots['Female'], years, label = "Female")

    plt.title(f'Average Ages of Congressional Membership from Sessions {start_range} to {end_range}')
    plt.xlabel('Years')
    plt.ylabel('Age')
    plt.legend(loc = 'upper left')
    plt.show()


            





# GRAPH
    # for criterion, value in plots.items():
    #     plt.plot(years, value, label = key)


#NOTES
    # put years or congresses on x-axis 


#OTHER
    # for s in session_range:
    #     if s not in sessions: #WHY ISN'T SESSIONS PASSING
    #         print("Invalid session input. Please try again.")

    # with open('key.txt') as handle:
    #     key = handle.read().strip() #strips trailing \n characters


#QUESTIONS
    #how to see all of the available headings for ppdata?
    #what to put in command-line? (criterion convert to lowercase?)