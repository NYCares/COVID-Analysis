import glob
import csv
import json
import os


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


# Print csv's in folder C:\Users\admin\
for csvFileName in glob.iglob(os.path.join('..', 'data', 'clean', '*.csv')):

    # create a name for the json output file
    jsonFileName = csvFileName.replace('.csv', '.json')

    try:
        convertCsvToJson('County', csvFileName, jsonFileName)
        print(f'{csvFileName} has been processed..')

    except:

        print(f'... skipping file: {csvFileName}')

# create variable to hold path to the free lunch csv source file
srcFile = os.path.join('..', 'data', 'clean',
                       'free_reduced_lunch_ny_county.csv')

# create variable to hold path to the free lunch json file
jsonFilePath = '../data/clean/free_reduced_lunch_ny_county.json'

# execute conversion with given parameters
convertCsvToJson('Region', srcFile, jsonFilePath)

print('Done.')

