from pymongo import MongoClient
import glob
import csv
import json
import os
print('loading mongo...')

client = MongoClient('localhost', 27017)
db = client['nycares_db']
db.covid_county.drop()
coll_covid_county = db['covid_county']
srcFile = os.path.join('..', 'static', 'data', 'clean',
                       'covid_ny_county.json')

with open(srcFile) as f:
    coll_covid_county.insert_one(json.load(f))

client.close()

print('Loading complete.')
