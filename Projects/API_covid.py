# sourse code
# https://github.com/realpython/materials/blob/master/consuming-apis-python/covid.py

# API documentation Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc
# country slug from the list: https://api.covid19api.com/countries
#https://github.com/samayo/country-json/blob/master/src/country-by-population.json
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

# With fixing bug (Incorrect Endpoint) and additional requests

# import requests

# from datetime import date, timedelta

# today = date.today()
# yesterday = today - timedelta(days=1)

# country = input('Country? ')

# endpoint_last_day = requests.get(
#     f"https://api.covid19api.com/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z",
#     params = {"from": str(yesterday), "to": str(today)}
# ).json()

# # print(endpoint_last_day.status_code)

# total_confirmed = 0
# for day in endpoint_last_day:
#     cases = day.get("Cases", 0)
#     total_confirmed += cases

# print(f"Last Day confirmed Covid-19 cases in {country}: {total_confirmed}")

# endpoint_total_statistics = requests.get(
#     f"https://api.covid19api.com/total/country/{country}", 
#     params={'q': 'requests+language:python'}
# ).json()[-1]

# # print(endpoint_total_statistics.status_code)

# total_confirmed_cases = endpoint_total_statistics['Confirmed']
# total_death = endpoint_total_statistics['Deaths'] 

# print(f"In Total confirmed Covid-19 cases in {country}: {total_confirmed_cases}")
# print(f"In Total death due to confirmed Covid-19 cases in {country}: {total_death}")

#_____________________
# LAST WORKING VERSION
import requests                                                                # print(endpoint_last_day.status_code)
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)

country = input('Country? ').capitalize()

import json                # ПОДКЛЮЧЕНИЕ ФАЙЛА Json to Python

json_file_path = "Projects\countries_list.json"

with open(json_file_path, 'r') as j:
    contries_list = json.loads(j.read())

    for x in contries_list:
        countries_list = x['country']

    for x in contries_list:
        if x['country'] == country:
            index_countries_list = contries_list.index(x)
            population = contries_list[index_countries_list]['population']

print(f"Population in {country}: {population}")


#+++++++++++++++++++++++++

# WORKING WITH JSON FILE + API
# import requests                                                                # print(endpoint_last_day.status_code)
# from datetime import date, timedelta

# today = date.today()
# yesterday = today - timedelta(days=1)

# country = input('Country? ')

# import json                # ПОДКЛЮЧЕНИЕ ФАЙЛА Json to Python

# json_file_path = "Projects\countries_list.json"

# with open(json_file_path, 'r') as j:
#     contries_list = json.loads(j.read())
#     print(type(contries_list))
#     for x in contries_list:
#         print(x['population'])
#     if contries_list[1]['country'] == country:
#         print(x['population'])
#     else:
#         print('N')
#     for x in contries_list:
#         print(contries_list.index(x))


#     for x in contries_list:
#         if x['country'] == country:
#             print(contries_list.index(x))
#             index_countries_list = contries_list.index(x)
#             print(contries_list[index_countries_list]['population'])

# with open(json_file_path, 'r') as j:   WORKING WITH JSON FILE  печаем население для 0 индекса
#     contents = json.loads(j.read())
#     print(type(contents))
#     print(contents[0]['population'])

    # for x in contents:
    #     print(x['population'])         WORKING WITH JSON FILE  печаем все населения в списке


# endpoint_last_day = requests.get(
#     f"https://api.covid19api.com/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z",
#     params = {"from": str(yesterday), "to": str(today)}
# ).json()

# endpoint_total_statistics = requests.get(
#     f"https://api.covid19api.com/total/country/{country}", 
#     params={'q': 'requests+language:python'}
# ).json()[-1]

# total_confirmed = 0
# for day in endpoint_last_day:
#     cases = day.get("Cases", 0)
#     total_confirmed += cases

# total_confirmed_cases = endpoint_total_statistics['Confirmed']
# total_death = endpoint_total_statistics['Deaths']

# print(f"Last Day confirmed Covid-19 cases in {country}: {total_confirmed}")
# print(f"In Total confirmed Covid-19 cases in {country}: {total_confirmed_cases}")
# print(f"In Total death due to confirmed Covid-19 cases in {country}: {total_death}")


# # + НУЖНО ДОБАВИТЬ + json file
# https://github.com/samayo/country-json/blob/master/src/country-by-population.json

# if status != 200:
#     print("An error has occured. [Status code", status, "]")
# else:
#     data = response.json() #Only convert to Json when status is OK.
#     if not data["elements"]:
#         print("Empty JSON")
#     else:
#         "You can extract data here"

# # ИЛИ
# # this is the https request for data in json format
# response_json = requests.get() 

# # only proceed if I have a 200 response which is saved in status_code
# if (response_json.status_code == 200):  
#      response = response_json.json() #converting from json to dictionary using json library


# Working Json
# {   "User1": {
#         "country": "Afghanistan",
#         "population": 37172386
#     }
# }
# with
# import json                # ПОДКЛЮЧЕНИЕ ФАЙЛА Json to Python

# json_file_path = "Projects\countries_list.json"

# with open(json_file_path, 'r') as j:
#     contents = json.loads(j.read())
#     if contents["User1"]["country"] == country:
#         print(contents["User1"]["population"])


# {
#     "1": {
#         "country": "Afghanistan",
#         "population": 37172386
#     },
#     "2": {
#         "country": "Albania",
#         "population": 2866376 
#     }
# }
