# resolve Dependencies
import pandas as pd
import os
import pymongo
from pymongo import MongoClient

free_reduced_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'free_reduced_lunch_ny_county.csv')

ny_population_race_breakdown_src = os.path.join(
    '..', 'static', 'data', 'processed', 'population_race_breakdown.csv')

covid_ny_county_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'covid_ny_county.csv')

median_income_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'median_income.csv')

# read data files into frames
free_reduced_df = pd.read_csv(free_reduced_src_path)

population_race_breakdown_df = pd.read_csv(ny_population_race_breakdown_src)

covid_results_df = pd.read_csv(covid_ny_county_src_path)

median_income_df = pd.read_csv(median_income_src_path)

# select and rename columns
population_raw_df = population_race_breakdown_df[['County','overall','white','black','native_american','asian','pacific_islander','other', 'hispanic_latino']].add_suffix('_population')
population_df = population_raw_df.rename(columns={'County_population': 'County'})
medianincome_df = median_income_df[['County','asian','black','hispanic','native_american','other','pacific_islander','white']].add_suffix('_median_income')
df1 = pd.merge(population_df,medianincome_df , how="left", left_on="County", right_on="County_median_income")

# select and rename columns
covid_ny_raw_df = covid_results_df[['County', 'Date', 'Deaths', 'Cases',
                                    '% of Population', '% of Deaths', '% of Cases']].add_prefix('covid_')
covid_ny_df = covid_ny_raw_df.rename(columns={'covid_County': 'identified_county', 'covid_Date': 'covid_date', 'covid_Deaths': 'covid_deaths',
                                              'covid_Cases': 'covid_cases', 'covid_% of Deaths': 'covid_death_%', 'covid_% of Cases': 'covid_cases_%', 'covid_% of Population': 'covid%ofpopulation'})

# perform merge for master analysis collection
df2 = pd.merge(df1, covid_ny_df, how="left",
               left_on="County", right_on="identified_county")

# connect to mongodb
client = MongoClient('mongodb://localhost:27017')

# set db connection
db = client['nycares_db']

# create dictionaries to populate mongo collects

free_as_dict = free_reduced_df.to_dict('records')

population_as_dict = population_race_breakdown_df.to_dict('records')

covid_results_dict = covid_results_df.to_dict('records')

median_income_dict = median_income_df.to_dict('records')

covid_analysis_dict = df2.to_dict('records')

# set reference to collection
frlp_collection = db['free_and_reduced_lunch']
frlp_collection.delete_many({})

population_race_collection = db['population_race_breakdown']
population_race_collection.delete_many({})

covid_results_collection = db['covid_results_by_county']
covid_results_collection.delete_many({})

median_income_collection = db['median_income']
median_income_collection.delete_many({})

covid_master_collection = db['covid_master_analysis']
covid_master_collection.delete_many({})

# insert documents to collections
for record in free_as_dict:
    frlp_collection.insert_one(record)

for record in population_as_dict:
    population_race_collection.insert_one(record)

for record in covid_results_dict:
    covid_results_collection.insert_one(record)

for record in median_income_dict:
    median_income_collection.insert_one(record)

for record in covid_analysis_dict:
    covid_master_collection.insert_one(record)
