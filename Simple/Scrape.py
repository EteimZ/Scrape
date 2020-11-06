#This was my first attempt to scrape a website
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://scrapethissite.com/pages/simple/').text

soup = BeautifulSoup(source, 'lxml')

with open("Country.csv","w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Country", "Capital", "Population", "Area"])

    for _ in soup.section.find_all('div', class_="col-md-4 country"):
        country = _.find("h3").text.strip()
        capital = _.find("span", class_="country-capital").text
        pop = _.find("span", class_="country-population").text
        area = _.find("span", class_="country-area").text
        csv_writer.writerow([country, capital, pop, area])
