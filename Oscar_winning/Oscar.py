### Importing libraries ###
from bs4 import BeautifulSoup
import requests
import os

link = "https://scrapethissite.com/pages/ajax-javascript/?ajax=true&year=201"

links = []
for i in range(6):
    links.append(link + str(i))

reqs = (requests.get(link) for link in links)


for i,r in enumerate(reqs):
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find("p").text
    if not os.path.exists(f"Oscar_winning/async{i}.json"):
        with open(f"Oscar_winning/async{i}.json", 'w') as f:
            f.write(data)

    
