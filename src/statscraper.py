# from bs4 import BeautifulSoup
# import requests
# from csv import writer

# base_link = "https://www.espn.com/nba/player/gamelog/_/id/"
# first_name = " "
# id_number = 1
# file = open("playerIDs.txt", "w")
# while id_number < 6605:
#     link = base_link + str(id_number)
#     response = requests.get(link)
#     soup = BeautifulSoup(response.text, "html.parser")
#     if soup.find(class_ = "truncate min-w-0 fw-light") is not None:
#         first_name = soup.find(class_ = "truncate min-w-0 fw-light").text
#         last_name = soup.find(class_ = "truncate min-w-0").text
#         line = first_name + " " + last_name + ", " + str(id_number) + '\n'
#         file.write(line)
#     id_number = id_number + 1
#     print(str(id_number))

# file.close()

import requests
from bs4 import BeautifulSoup

# from core.views import get_name
# from core.views import get_date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#Configure chrome driver
chromedriver_PATH = "../chromedriver.exe"
driver = webdriver.Chrome(executable_path= chromedriver_PATH)
driver.get("http://google.com")

#Read request data
# target_playername = get_name()
# target_date = get_date()
# print(target_playername)
# print(target_date)

#Navigate to target player url
searchbar = driver.find_element_by_name('q')
# searchbar.send_keys("espn game by game stats " + str(target_playername))
searchbar.send_keys(Keys.RETURN)
driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()
driver.quit()

#Get url of target player
target_url = driver.current_url

#Start scraping stats
response = requests.get(str(target_url))
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