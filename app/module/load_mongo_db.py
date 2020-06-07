# resolve Dependencies
import pandas as pd
import os
import pymongo
from pymongo import MongoClient

free_reduced_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'free_reduced_lunch_ny_county.csv')

commute_by_county_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'commute_by_county.csv')

ny_population_race_breakdown_src = os.path.join(
    '..', 'static', 'data', 'processed', 'population_race_breakdown.csv')

covid_ny_county_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'covid_ny_county.csv')

covid_ny_results_county_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'covid_ny_results_county.csv')

covid_cases_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'covid_confirmed.csv')

covid_deaths_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'covid_deaths.csv')

djia_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'dji_avg.csv')

county_lkp_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'county_id_lookup.csv')

median_income_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'median_income.csv')

population_by_county_src_path = os.path.join(
    '..', 'static', 'data', 'processed', 'population_by_county.csv')

# read data files into frames
free_reduced_df = pd.read_csv(free_reduced_src_path)

commute_by_county_df = pd.read_csv(commute_by_county_src_path)

population_race_breakdown_df = pd.read_csv(ny_population_race_breakdown_src)

covid_cases_time_series_df = pd.read_csv(covid_cases_src_path)

covid_deaths_time_series_df = pd.read_csv(covid_deaths_src_path)

dow_jones_index_df = pd.read_csv(djia_src_path)

covid_results_df = pd.read_csv(covid_ny_county_src_path)

covid_cumulative_df = pd.read_csv(covid_ny_results_county_src_path)

county_lookup_df = pd.read_csv(county_lkp_src_path)

median_income_df = pd.read_csv(median_income_src_path)

county_population_df = pd.read_csv(population_by_county_src_path)
# build a single master dataframe using a select set of columns from each
# dataframe

# select and rename columns
population_raw_df = population_race_breakdown_df[[
    'County', 'overall', 'white', 'black', 'native_american', 'asian', 'pacific_islander', 'other']].add_suffix('_population')
population_df = population_raw_df.rename(
    columns={'County_population': 'County'})
medianincome_df = median_income_df[['county', 'asian', 'black', 'hispanic_latino', 'mixed_race',
                                    'native_american', 'other', 'pacific_islander', 'white']].add_suffix('_median_income')
df1 = pd.merge(population_df, medianincome_df, how="left",
               left_on="County", right_on="county_median_income")

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

commute_as_dict = commute_by_county_df.to_dict('records')

population_as_dict = population_race_breakdown_df.to_dict('records')

covid_cases_as_dict = covid_cases_time_series_df.to_dict('records')

covid_deaths_as_dict = covid_deaths_time_series_df.to_dict('records')

dow_jones_as_dict = dow_jones_index_df.to_dict('records')

covid_results_dict = covid_results_df.to_dict('records')

covid_cumulative_dict = covid_cumulative_df.to_dict('records')

county_lookup_dict = county_lookup_df.to_dict('records')

median_income_dict = median_income_df.to_dict('records')

county_population_dict = county_population_df.to_dict('records')

covid_analysis_dict = df2.to_dict('records')

# set reference to collection
frlp_collection = db['free_and_reduced_lunch']
frlp_collection.delete_many({})

commute_collection = db['commute_by_county']
commute_collection.delete_many({})

population_race_collection = db['population_race_breakdown']
population_race_collection.delete_many({})

covide_cases_collection = db['covid_cases_time_series']
covide_cases_collection.delete_many({})

covid_deaths_collection = db['covid_deaths_time_series']
covid_deaths_collection.delete_many({})

djia_collection = db['dow_jones_index']
djia_collection.delete_many({})

covid_results_collection = db['covid_results_by_county']
covid_results_collection.delete_many({})

covid_cumulative_collection = db['covid_cumulative_results']
covid_cumulative_collection.delete_many({})

county_lookup_collection = db['county_lookup']
county_lookup_collection.delete_many({})

median_income_collection = db['median_income']
median_income_collection.delete_many({})

county_population_collection = db['county_population']
county_population_collection.delete_many({})

covid_master_collection = db['covid_master_analysis']
covid_master_collection.delete_many({})

# insert documents to collections
for record in free_as_dict:
    frlp_collection.insert_one(record)

for record in commute_as_dict:
    commute_collection.insert_one(record)

for record in population_as_dict:
    population_race_collection.insert_one(record)

for record in covid_cases_as_dict:
    covide_cases_collection.insert_one(record)

for record in covid_deaths_as_dict:
    covid_deaths_collection.insert_one(record)

for record in dow_jones_as_dict:
    djia_collection.insert_one(record)

for record in covid_results_dict:
    covid_results_collection.insert_one(record)

for record in covid_cumulative_dict:
    covid_cumulative_collection.insert_one(record)

for record in county_lookup_dict:
    county_lookup_collection.insert_one(record)

for record in median_income_dict:
    median_income_collection.insert_one(record)

for record in county_population_dict:
    county_population_collection.insert_one(record)

for record in covid_analysis_dict:
    covid_master_collection.insert_one(record)
