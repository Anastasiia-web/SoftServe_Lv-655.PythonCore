# sourse code
# https://github.com/realpython/materials/blob/master/consuming-apis-python/covid.py

# API documentation Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc
# country slug from the list: https://api.covid19api.com/countries

# Initial code with bug incorrect Endpoint

# import requests

# from datetime import date, timedelta

# today = date.today()
# yesterday = today - timedelta(days=1)

# country = "germany"

# endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"
# params = {"from": str(yesterday), "to": str(today)}

# response = requests.get(endpoint, params=params).json()

# total_confirmed = 0
# for day in response:
#     cases = day.get("Cases", 0)
#     total_confirmed += cases

# print(f"Total Confirmed Covid-19 cases in {country}: {total_confirmed}")
#__________________________________________________________________________
# Done in scope of the Project:
# 1. Bug fix (Incorrect Endpoint)
# 2. Additional requests were added:
#    * second API endpoint (endpoint_last_day.status_code)
#    * Json file to provide country's population number (source code https://github.com/samayo/country-json/blob/master/src/country-by-population.json)

import requests                                                                
from datetime import date, timedelta
import json

today = date.today()
yesterday = today - timedelta(days=1)

country = input('Country? ').capitalize()

json_file_path = "underReconstruction\countries_list.json"

with open(json_file_path, 'r') as j:
    contries_list = json.loads(j.read())

    for x in contries_list:
        if x['country'] == country:
            index_countries_list = contries_list.index(x)
            population = contries_list[index_countries_list]['population']

endpoint_last_day = requests.get(
    f"https://api.covid19api.com/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z",
    params = {"from": str(yesterday), "to": str(today)}
).json()

endpoint_total_statistics = requests.get(
    f"https://api.covid19api.com/total/country/{country}", 
    params={'q': 'requests+language:python'}
).json()[-1]

total_confirmed = 0
for day in endpoint_last_day:
    cases = day.get("Cases", 0)
    total_confirmed += cases

total_confirmed_cases = endpoint_total_statistics['Confirmed']
total_death = endpoint_total_statistics['Deaths'] 

print(f"Population in {country}: {population}")
print(f"Last Day confirmed Covid-19 cases in {country}: {total_confirmed}")
print(f"Total confirmed Covid-19 cases in {country}: {total_confirmed_cases}")
print(f"Total death due to confirmed Covid-19 cases in {country}: {total_death}")

for_notes = f"{today}  \n{country}      |  population           |  {population} \n             | last day confirmed    |     {total_confirmed} \n"

file = open("statistics.txt", "a")
file.write(for_notes)
file.close()
