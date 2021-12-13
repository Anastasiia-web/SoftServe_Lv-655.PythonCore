# https://realpython.com/beautiful-soup-web-scraper-python/#pass-a-function-to-a-beautiful-soup-method

import requests
from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for parsing structured data

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text) # HTML
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

results = soup.find(id="ResultsContainer")

print(results.prettify())   # better reading

job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()