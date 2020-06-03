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


printPath = os.path.join('..', 'static', 'data', 'clean',
                         '*.csv')


# Print csv's in folder C:\Users\admin\
for csvFileName in glob.iglob(os.path.join('..', 'static', 'data', 'clean', '*.csv')):

    # create a name for the json output file
    jsonFileName = csvFileName.replace('.csv', '.json')

    try:

        convertCsvToJson('id', csvFileName, jsonFileName)
        print(f'{csvFileName} has been processed..')

    except:

        print(f'... skipping file: {csvFileName}')


# Covid State Data
# create variable to hold path to the covid ny county results csv source file
srcFile = os.path.join('..', 'static', 'data', 'clean',
                       'covid_ny_results_county.csv')

# create variable to hold path to the covid ny county results json file
jsonFilePath = os.path.join('..', 'static', 'data', 'clean',
                            'covid_ny_results_county.json')

# execute conversion with given parameters
convertCsvToJson('testdate', srcFile, jsonFilePath)


# create variable to hold path to the covid ny state results csv source file
srcFile = os.path.join('..', 'static', 'data', 'clean',
                       'covid_ny_state_results.csv')

# create variable to hold path to the covid ny state results json file
jsonFilePath = os.path.join('..', 'static', 'data', 'clean',
                            'covid_ny_state_results.json')

# execute conversion with given parameters
convertCsvToJson('testdate', srcFile, jsonFilePath)


# Dow Jones Index
# create variable to hold path to the free lunch csv source file
srcFile = os.path.join('..', 'static', 'data', 'clean',
                       'dji_avg.csv')

# create variable to hold path to the free lunch json file
jsonFilePath = os.path.join('..', 'static', 'data', 'clean',
                            'dow_jones_index.json')


# execute conversion with given parameters
convertCsvToJson('Date', srcFile, jsonFilePath)


#print('json files generated...')

print('All Done!')
