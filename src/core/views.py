from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

#Third party imports
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup

#Holds request data
data = None

#API endpoint function
@api_view(['GET'])
def get_data(request):
    global data 
    data = request.data
    return Response(statscraper())

#Searches requested player's id from playerIDs.txt
def get_id():
    file = open("../src/playerIDs.txt", "r", encoding='utf-8')
    for line in file:
        if data['player'] in line:
            return line.split(", ")[1]
    return str(-1)

#Returns requested date
def get_date():
    if (data['date'])[0] == '0':
        data['date'] = (data['date'])[1 :]
    if (data['date'])[-2] == '0':
        data['date'] = (data['date'])[0 : -2] + data['date'][-1]
    return data['date']

#Returns requested season
def get_season():
    return data['season']

#Scrapes data
def statscraper():
    #Get requested player's ID
    target_id = get_id()

    #Check if a valid player was found 
    if target_id == "-1":
        error = {   "status" : 400,
            "developerMessage" : "No matching player ID was found",
            "userMessage" : "The player's name was not recognized. Make sure the player's name is spelled correctly.", 
            "errorCode" : "01",
        }
        return error

    #Read request data
    target_date = get_date()
    target_season = get_season()
    target_season = target_season[-4] + target_season[-3] + target_season[-2] + target_season[-1] 
    
    #Get url of target player
    target_url = "https://www.espn.com/nba/player/gamelog/_/id/" + str(target_id)
    target_url = target_url.strip('\n')
    if(target_season != '2022'):
        target_url = target_url + "/type/nba/year/" + target_season

    #Start scraping stats
    response = requests.get(str(target_url))
    soup = BeautifulSoup(response.text, 'html.parser')
    season = soup.find_all(class_='filled Table__TR Table__TR--sm Table__even') + soup.find_all(class_="Table__TR Table__TR--sm Table__even") + soup.find_all(class_="bwb-0 Table__TR Table__TR--sm Table__even")
    target_statline = None
    for game in season:
        statline = game.find_all(class_="Table__TD")
        date = statline[0].text
        if '/' in date:
            if target_date == date[4:]:
                target_statline = statline

    #If no result found return an error
    if target_statline is None:
        error = {   "status" : 400,
            "developerMessage" : "Scraped data did not contain a match",
            "userMessage" : "The requested player likely did not play on the given date", 
            "errorCode" : "02",
        }
        return error
        
    #If stats found with no error return statline
    else: 
        player_statline = {
            "status" : 200,
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


    