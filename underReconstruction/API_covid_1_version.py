# import from countries_list.json
import requests                                                                # print(endpoint_last_day.status_code)
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)

country = input('Country? ')

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

print(f"Last Day confirmed Covid-19 cases in {country}: {total_confirmed}")
print(f"In Total confirmed Covid-19 cases in {country}: {total_confirmed_cases}")
print(f"In Total death due to confirmed Covid-19 cases in {country}: {total_death}")


