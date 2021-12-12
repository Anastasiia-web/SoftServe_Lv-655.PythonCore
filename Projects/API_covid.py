# sourse code
# https://github.com/realpython/materials/blob/master/consuming-apis-python/covid.py

# API documentation Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc

# Initial code with bug incorrect Endpoint

# import requests

# # The datetime package is useful to manipulate dates.
# from datetime import date, timedelta

# # To fetch the latest total confirmed cases number you need to pass a 24h
# # window to the API. That's why you need to pass both yesterday's date
# # and today's.
# today = date.today()
# yesterday = today - timedelta(days=1)

# # Pick a country slug from the list: https://api.covid19api.com/countries
# country = "germany"

# endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"  # Incorrect Endpoint https://api.covid19api.com/country/{country}/status/confirmed
# params = {"from": str(yesterday), "to": str(today)}

# # The response will be a list of results per day, in your case only 1 result.
# response = requests.get(endpoint, params=params).json()

# # Finally, you need to traverse through the response and increment the
# # `total_confirmed` variable with the total number of confirmed cases
# # available that day, which is in the field `Cases`.
# total_confirmed = 0
# for day in response:
#     cases = day.get("Cases", 0)
#     total_confirmed += cases

# print(f"Total Confirmed Covid-19 cases in {country}: {total_confirmed}")

#__________________________________________________________________________

import requests

from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)

country = "Poland"
########country = input('Country?')

endpoint_last_day = requests.get(
    f"https://api.covid19api.com/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z",
    params = {"from": str(yesterday), "to": str(today)}
).json()

# print(endpoint_last_day.status_code)

total_confirmed = 0
for day in endpoint_last_day:
    cases = day.get("Cases", 0)
    total_confirmed += cases

print(f"Last Day confirmed Covid-19 cases in {country}: {total_confirmed}")

endpoint_total_statistics = requests.get(
    f"https://api.covid19api.com/total/country/{country}", 
    params={'q': 'requests+language:python'}
).json()[-1]

# print(endpoint_total_statistics.status_code)

total_confirmed_cases = endpoint_total_statistics['Confirmed']
total_death = endpoint_total_statistics['Deaths'] 

print(f"In Total confirmed Covid-19 cases in {country}: {total_confirmed_cases}")
print(f"In Total death due to confirmed Covid-19 cases in {country}: {total_death}")