from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Third party imports
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# from selenium.webdriver.chrome.options import Options
import time

data = None

@api_view(['GET'])
def get(request):
    global data 
    data = request.data
    return Response(statscraper())

def get_id():
    file = open("playerIDs.txt", "r", encoding='utf-8')
    for line in file:
        if data['player'] in line:
            return line.split(", ")[1]
    return str(-1)
def get_name():
    return data['player']

def get_date():
    return data['date']

def get_season():
    return data['season']

def statscraper():

    #Get requested player's ID
    target_id = get_id()

    #Read request data
    target_playername = get_name()
    target_date = get_date()
    target_season = get_season()
    size = len(target_season)
    target_season = target_season[size-4] + target_season[size-3] + target_season[size-2] + target_season[size-1] 
    print(target_playername)
    print(target_date)
    print(target_season)
    print(target_id)

    #Configure chrome driver
    # chromedriver_PATH = "../chromedriver.exe"
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--disable-extensions")
    # driver = webdriver.Chrome(executable_path=chromedriver_PATH)
    # driver.get("http://google.com")

    #Navigate to target player url
    # searchbar = driver.find_element_by_name('q')
    # searchbar.send_keys(str(target_playername) + " Game by Game Stats and Performance nba")
    # searchbar.send_keys(Keys.RETURN)
    # driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()
    
    #Get url of target player
    target_url = "https://www.espn.com/nba/player/gamelog/_/id/" + str(target_id)
    if(target_season != '2021'):
        target_url = target_url + "/type/nba/year/" + target_season
    print(target_url)
    #Quit driver
    # driver.quit()

    #Start scraping stats
    response = requests.get(str(target_url))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    season = soup.find_all(class_='filled Table__TR Table__TR--sm Table__even') + soup.find_all(class_="Table__TR Table__TR--sm Table__even")
    target_statline = None
    for game in season:
        statline = game.find_all(class_="Table__TD")
        date = statline[0].text
        if '/' in date:
            if target_date in date:
                target_statline = statline

    #If no result found return an error
    if target_statline is None:
        error = {   "status" : 400,
            "developerMessage" : "Scraped data did not contain a match",
            "userMessage" : "The requested player likely did not play on the given date", 
            "errorCode" : "01",
        }
        return error
    #If stats found with no error return statline
    else: 
        player_statline = {
            "statline" : {
                "points": target_statline[16].text,
                "rebounds": target_statline[10].text,
                "assists": target_statline[11].text,
                "steals": target_statline[13].text,
                "blocks": target_statline[12].text,
                "turnovers": target_statline[15].text,
                "minutes": target_statline[3].text,
                "field_goals": target_statline[4].text,
                "three_pointers": target_statline[6].text,  
                "free_throws": target_statline[8].text, 
                "fg_percentage": target_statline[5].text,
                "three_point_percentage": target_statline[7].text, 
                "ft_percentage": target_statline[9].text, 
                "personal_fouls": target_statline[14].text, 
            },
            "date": target_statline[0].text, 
            "team_played": target_statline[1].text, 
            "score": target_statline[2].text, 
        }
        return player_statline