import requests                                                                
from datetime import date, timedelta
import json

today = date.today()
yesterday = today - timedelta(days=1)

country = input('Country? ').capitalize()

json_file_path = "Projects\Project_1\API_covid_statistics\src\countries_list.json"

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
