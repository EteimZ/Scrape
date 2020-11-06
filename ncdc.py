#Scraping Tabular data
import pandas as pd
import requests

data = requests.get("https://covid19.ncdc.gov.ng/report/")

df = pd.read_html(data.text)
df = pd.concat(df) #Converting the data from list to dataframe.
print(df.head())
