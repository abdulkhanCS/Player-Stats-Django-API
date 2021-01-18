from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from statscraper import player_statline

data = None

@api_view(['GET'])
def get(request):
    global data 
    data = request.data
    exec(open("statscraper.py").read())
    return Response(player_statline)

def get_name():
    return data['player']

def get_date():
    return data['date']