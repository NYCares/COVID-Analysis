import glob
import csv
import json
import os
import pandas as pd
import pymongo
from pymongo import MongoClient


def convertCsvToJson(srcId, srcFile, jsonFilePath):

    # data dictionary container for data file
    data = {}

    # loop through and read the data from the csv
    with open(srcFile) as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        # print(csvReader)
        for row in csvReader:
            id = row[srcId]
            data[id] = row

        # A quick check on the header
        # csv_header = next(csvReader)
        # print(f"CSV Header: {csv_header}")

        # for row in csvReader:
        #     print(row[0])
    # 'ï»¿ID'
    # create new json file and write data to the file
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


printPath = os.path.join('..', 'static', 'data', 'processed',
                         '*.csv')


# Print csv's in folder C:\Users\admin\
for csvFileName in glob.iglob(os.path.join('..', 'static', 'data', 'processed', '*.csv')):

    # create a name for the json output file
    jsonFileName = csvFileName.replace('.csv', '.json')

    try:

        convertCsvToJson('id', csvFileName, jsonFileName)
        print(f'{csvFileName} has been processed..')

    except:

        print(f'... skipping file: {csvFileName}')


# Covid State Data
# create variable to hold path to the covid ny county results csv source file
srcFile = os.path.join('..', 'static', 'data', 'processed',
                       'covid_ny_results_county.csv')

# create variable to hold path to the covid ny county results json file
jsonFilePath = os.path.join('..', 'static', 'data', 'processed',
                            'covid_ny_results_county.json')

# execute conversion with given parameters
convertCsvToJson('testdate', srcFile, jsonFilePath)


# create variable to hold path to the covid ny state results csv source file
srcFile = os.path.join('..', 'static', 'data', 'processed',
                       'covid_ny_state_results.csv')

# create variable to hold path to the covid ny state results json file
# jsonFilePath = os.path.join('..', 'static', 'data', 'processed',
# 'covid_ny_state_results.json')

# execute conversion with given parameters
# convertCsvToJson('testdate', srcFile, jsonFilePath)


# Dow Jones Index
# create variable to hold path to the free lunch csv source file
srcFile = os.path.join('..', 'static', 'data', 'processed',
                       'dji_avg.csv')

# create variable to hold path to the free lunch json file
jsonFilePath = os.path.join('..', 'static', 'data', 'processed',
                            'dow_jones_index.json')


# execute conversion with given parameters
convertCsvToJson('Date', srcFile, jsonFilePath)


# # Load to Mongo DB
# def loadMongoDB():
#     free_reduced_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'free_reduced_lunch_ny_county.csv')

#     commute_by_county_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'commute_by_county.csv')

#     ny_population_race_breakdown_src = os.path.join(
#         '..', 'static', 'data', 'processed', 'population_race_breakdown.csv')

#     covid_ny_county_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'covid_ny_county.csv')

#     covid_ny_results_county_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'covid_ny_results_county.csv')

#     covid_cases_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'covid_confirmed.csv')

#     covid_deaths_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'covid_deaths.csv')

#     djia_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'dji_avg.csv')

#     county_lkp_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'county_id_lookup.csv')

#     median_income_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'median_income.csv')

#     population_by_county_src_path = os.path.join(
#         '..', 'static', 'data', 'processed', 'population_by_county.csv')
#     # read data files into frames
#     free_reduced_df = pd.read_csv(free_reduced_src_path)

#     commute_by_county_df = pd.read_csv(commute_by_county_src_path)

#     population_race_breakdown_df = pd.read_csv(
#         ny_population_race_breakdown_src)

#     covid_cases_time_series_df = pd.read_csv(covid_cases_src_path)

#     covid_deaths_time_series_df = pd.read_csv(covid_deaths_src_path)

#     dow_jones_index_df = pd.read_csv(djia_src_path)

#     covid_results_df = pd.read_csv(covid_ny_county_src_path)

#     covid_cumulative_df = pd.read_csv(covid_ny_results_county_src_path)

#     county_lookup_df = pd.read_csv(county_lkp_src_path)

#     median_income_df = pd.read_csv(median_income_src_path)

#     county_population_df = pd.read_csv(population_by_county_src_path)

#     # set connect driver to mongodb
#     client = MongoClient('mongodb://localhost:27017')

#     # set db connection
#     db = client['nycares_db']

#     # create dictionaries to populate mongo collects
#     free_as_dict = free_reduced_df.to_dict('records')

#     commute_as_dict = commute_by_county_df.to_dict('records')

#     population_as_dict = population_race_breakdown_df.to_dict('records')

#     covid_cases_as_dict = covid_cases_time_series_df.to_dict('records')

#     covid_deaths_as_dict = covid_deaths_time_series_df.to_dict('records')

#     dow_jones_as_dict = dow_jones_index_df.to_dict('records')

#     covid_results_dict = covid_results_df.to_dict('records')

#     covid_cumulative_dict = covid_cumulative_df.to_dict('records')

#     county_lookup_dict = county_lookup_df.to_dict('records')

#     median_income_dict = median_income_df.to_dict('records')

#     county_population_dict = county_population_df.to_dict('records')

#     # set reference to collection
#     frlp_collection = db['free_and_reduced_lunch']
#     frlp_collection.delete_many({})

#     commute_collection = db['commute_by_county']
#     commute_collection.delete_many({})

#     population_race_collection = db['population_race_breakdown']
#     population_race_collection.delete_many({})

#     covide_cases_collection = db['covid_cases_time_series']
#     covide_cases_collection.delete_many({})

#     covid_deaths_collection = db['covid_deaths_time_series']
#     covid_deaths_collection.delete_many({})

#     djia_collection = db['dow_jones_index']
#     djia_collection.delete_many({})

#     covid_results_collection = db['covid_results_by_county']
#     covid_results_collection.delete_many({})

#     covid_cumulative_collection = db['covid_cumulative_results']
#     covid_cumulative_collection.delete_many({})

#     county_lookup_collection = db['county_lookup']
#     county_lookup_collection.delete_many({})

#     median_income_collection = db['median_income']
#     median_income_collection.delete_many({})

#     county_population_collection = db['county_population']
#     county_population_collection.delete_many({})

#     # insert documents to collections
#     frlp_collection.insert_one({"index": "region", "data": free_as_dict})

#     commute_collection.insert_one({"index": "County", "data": commute_as_dict})

#     population_race_collection.insert_one(
#         {"index": "County", "data": population_as_dict})

#     covide_cases_collection.insert_one(
#         {"index": "County", "data": covid_cases_as_dict})

#     covid_deaths_collection.insert_one(
#         {"index": "County", "data": covid_deaths_as_dict})

#     djia_collection.insert_one({"index": "region", "data": dow_jones_as_dict})

#     covid_results_collection.insert_one(
#         {"index": "county", "data": covid_results_dict})

#     covid_cumulative_collection.insert_one(
#         {"index": "county", "data": covid_cumulative_dict})

#     county_lookup_collection.insert_one(
#         {"index": "County", "data": county_lookup_dict})

#     median_income_collection.insert_one(
#         {"index": "County", "data": median_income_dict})

#     county_population_collection.insert_one(
#         {"index": "County", "data": county_population_dict})


print('All Done!')
