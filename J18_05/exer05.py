#!/usr/bin/env python

import csv
import json

import requests

CITY_DATA_JSON_URL = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6'
OUTFILE = 'cities.csv'
KEYS_TO_WRITE = ['city', 'state', 'population','rank']

# Get data from URL and decode JSON into list of dicts
result = requests.get(CITY_DATA_JSON_URL)
city_data = json.loads(result.text)

# Write out CSV file with header row
with open(OUTFILE, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    row = ['City', 'State name', 'City population', 'City size rank']
    writer.writerow(row)
    for city in city_data:
        row = [city[k] for k in KEYS_TO_WRITE]
        writer.writerow(row)