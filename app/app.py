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

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = dbconn.nycares_db

col = db.covid_master_analysis

# Define routes
@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/results.html/<county>")
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

    median_income.append(master_data["asian_median_income"])
    median_income.append(master_data["black_median_income"])
    median_income.append(master_data["hispanic_median_income"])
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
    lunch_data = db.free_and_reduced_lunch.find_one(
        {"region": f"{county} County"})
    fl_pct_county.append(lunch_data["percent of the county"])
    state_data = db.free_and_reduced_lunch.find_one(
        {"region": "New York State"})
    fl_pct_state.append(state_data["percent of state"])

    return render_template('results.html', population=population, pop_label=pop_label, covid_label=covid_label, covid_incidents=covid_incidents, covid_deaths=covid_deaths,  median_income=median_income, fl_pct_county=fl_pct_county, fl_pct_state=fl_pct_state)


# @app.route("/team.html")
# def About():
#     return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)
