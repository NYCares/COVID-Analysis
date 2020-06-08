#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
from flask import Flask, request, render_template, jsonify

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

from bson.json_util import dumps

# Create an instance of our Flask app.
app = Flask(__name__)

# read json master dataset
# json_data = open(os.path.join('.', 'static', 'data', 'processed', 'covid_master_analysis.json'))
# print(json_data)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = dbconn.nycares_db

col = db.covid_master_analysis

# master_data = json.load(json_data)
# print(master_data['25']['County'])

# db.covid_analysis.find_one({"county": "Queens"})

# Define routes
@app.route("/")
def welcome():
    return render_template('index.html')


# @app.route("/test.html/<county>")
# def Visualization(county):
#     for item in master_data:
#         comparison = master_data[item]['County'].lower()
#         if comparison == county.lower():
#             print('Found a match!')
#             print(comparison)
#             data = json.dumps(master_data[item])
#             print(data)
#             return render_template('test.html', data=master_data)


@app.route("/test.html/<county>")
def Visualization(county):
    master_data = db.covid_master_analysis.find_one({"County": f"{county}"})

    population = []
    median_income = []
    covid_incidents = []
    covid_deaths = []
    fl_pct_county = []
    fl_pct_state = []

    population.append(master_data["asian_population"])
    population.append(master_data["black_population"])
    population.append(master_data["hispanic_latino_population"])
    population.append(master_data["native_american_population"])
    population.append(master_data["other_population"])
    population.append(master_data["pacific_islander_population"])
    population.append(master_data["white_population"])

    # median income
    median_income.append(master_data["asian_median_income"])
    median_income.append(master_data["black_median_income"])
    median_income.append(master_data["hispanic_latino_median_income"])
    median_income.append(master_data["native_american_median_income"])
    median_income.append(master_data["other_median_income"])
    median_income.append(master_data["pacific_islander_median_income"])
    median_income.append(master_data["white_median_income"])

    pop_label = ['asian', 'black', 'hispanic',
                 'native american', 'other', 'pacific islander', 'white']

    covid_label = ['covid cases', 'covid deaths']

    covid_incidents.append(master_data["covid_cases"])
    covid_deaths.append(master_data["covid_deaths"])

    print(covid_incidents)
    print(covid_deaths)
    lunch_data = db.free_and_reduced_lunch.find_one({"region": f"{county}"})
    fl_pct_county.append(lunch_data["percent of the"])
    state_data = db.free_and_reduced_lunch.find_one(
        {"region": "New York State"})
    fl_pct_state.append(state_data["percent of state"])

    return render_template('test.html', population=population, pop_label=pop_label, covid_label=covid_label, covid_incidents=covid_incidents, covid_deaths=covid_deaths,  median_income=median_income, fl_pct_county=fl_pct_county, fl_pct_state=fl_pct_state)


if __name__ == '__main__':
    app.run(debug=True)
