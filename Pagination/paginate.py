from bs4 import BeautifulSoup
import requests
import pandas as pd 

source = requests.get("https://scrapethissite.com/pages/forms/?per_page=600").text

soup = BeautifulSoup(source, 'lxml')

name = []
year = []
wins = []
loss = []
OTloss = []
winper = []
gf = []
ga = []
diff = []

teams_tr = soup.find_all("tr", class_="team")

for team in teams_tr:
    team_name = team.find("td", class_="name").text.strip()
    name.append(team_name)
    
    team_year = team.find("td", class_="year").text.strip()
    year.append(team_year)

    team_wins = team.find("td", class_="wins").text.strip()
    wins.append(team_wins)

    team_loss = team.find("td", class_="losses").text.strip()
    loss.append(team_loss)

    team_ot = team.find("td", class_="ot-losses").text.strip()
    OTloss.append(team_ot)
   
    try: 
        team_pct = team.find("td", class_="pct text-success").text.strip()
    except AttributeError:
        team_pct = team.find("td", class_="pct text-danger").text.strip()
    winper.append(team_pct)

    team_gf = team.find("td", class_="gf").text.strip()
    gf.append(team_gf)

    team_ga = team.find("td", class_="ga").text.strip()
    ga.append(team_ga)
    
    try:
        team_diff = team.find("td", class_="diff text-success").text.strip()
    except AttributeError:
        team_diff = team.find("td", class_="diff text-danger").text.strip()
    diff.append(team_diff)


teams = pd.DataFrame({
    "Team Name" : name,
    "Year" : year,
    "Wins" : wins,
    "Losses" : loss,
    "OT Losses" : OTloss,
    "Win %" : winper,
    "Goals For (GF)" : gf,
    "Goals Against (GA)" : ga,
    "+/-": diff
})

teams.to_csv("teams.csv", index=False)
