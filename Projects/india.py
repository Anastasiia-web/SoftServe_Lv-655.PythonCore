# https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)
# https://en.wikipedia.org/wiki/India
# https://en.wikipedia.org/wiki/India
import requests
from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for parsing structured data
country = input('C? ')
URL = "https://en.wikipedia.org/wiki/{country}"
page = requests.get(URL)

# print(page.text) # HTML
soup = BeautifulSoup(page.content, "html.parser")
print(soup)

# results = soup.find(id="ResultsContainer")

# print(results.prettify())   # better reading

# job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)