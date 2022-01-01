from bs4 import BeautifulSoup
import requests
import lines_to_exclude as lte

url = "https://www.w3schools.com/python/python_classes.asp"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title")
notes_title = title.get_text()

link_to_certification = soup.find("a", id="courses_get_started_btn")
link = link_to_certification.get('href')

article = soup.find_all("p")

print(notes_title)

for sentence in article:
    ready_notes = sentence.get_text()
    if ready_notes not in lte.list_exceptions:
        print(ready_notes)
