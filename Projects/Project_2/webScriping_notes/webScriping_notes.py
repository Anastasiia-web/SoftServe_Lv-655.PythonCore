# Web Scraping helps to have notes in 1 sec from w3school site;)
# https://www.w3schools.com/python/python_classes.asp
# documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id51

from bs4 import BeautifulSoup
import requests

url = "https://www.w3schools.com/python/python_classes.asp"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title")
notes_title = title.get_text()

link_to_certification = soup.find("a", id="courses_get_started_btn")
link = link_to_certification.get('href')

article = soup.find_all("p")

exception_1 = "Create a class named MyClass:"
exception_2 = "Start the Exercise"
exception_3 = "We just launchedW3Schools videos"
exception_4 = "If you want to report an error, or if you want to make a suggestion, do not hesitate to send us an e-mail:"
exception_5 = "help@w3schools.com"
exception_6 = "Your message has been sent to W3Schools."

list_exceptions = [exception_1, exception_2, exception_3, exception_4, exception_5, exception_6]

print(notes_title)

for sentence in article:
    ready_notes = sentence.get_text()
    if ready_notes not in list_exceptions:
        print(ready_notes)

print(link)
