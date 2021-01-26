import requests
from bs4 import BeautifulSoup
from urlscraper import playername
from urlscraper import date

response = requests.get('https://www.espn.com/nba/player/gamelog/_/id/6606/damian-lillard')

target_date = date

soup = BeautifulSoup(response.text, 'html.parser')
season = soup.find_all(class_='filled Table__TR Table__TR--sm Table__even') + soup.find_all(class_="Table__TR Table__TR--sm Table__even")
for game in season:
    statline = game.find_all(class_="Table__TD")
    date = statline[0].text
    if '/' in date:
        if target_date in date:
            target_statline = statline

player_statline = {
    "date": target_statline[0].text, 
    "team_played": target_statline[1].text, 
    "score": target_statline[2].text, 
    "minutes": target_statline[3].text, 
    "field_goals": target_statline[4].text, 
    "fg_percentage": target_statline[5].text, 
    "three_pointers": target_statline[6].text, 
    "three_point_percentage": target_statline[7].text, 
    "free_throws": target_statline[8].text, 
    "ft_percentage": target_statline[9].text, 
    "rebounds": target_statline[10].text, 
    "assists": target_statline[11].text, 
    "blocks": target_statline[12].text, 
    "steals": target_statline[13].text, 
    "personal_fouls": target_statline[14].text, 
    "turnovers": target_statline[15].text,
    "points": target_statline[16].text,
}

print(player_statline)