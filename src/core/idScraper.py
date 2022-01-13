from bs4 import BeautifulSoup
import requests
from csv import writer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

base_link = "https://en.wikipedia.org/wiki/2021_NBA_draft"
file = open("../playerIDs.txt", "a", encoding='utf-8')
response = requests.get(base_link)
soup = BeautifulSoup(response.text, 'html.parser')
players = soup.find_all(class_='fn')

chromedriver_PATH = "../chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_PATH)

for player in players:
    #Navigate to target player url
    driver.get("http://google.com")
    searchbar = driver.find_element_by_name('q')
    searchbar.send_keys(str(player.text) + " Game by Game Stats and Performance nba")
    searchbar.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()
    link = driver.current_url
    parts = link.split("/")
    id = parts[len(parts)-2]
    if id is not None:
        file.write(player.text + ", " + str(id) + '\n')
        print(player.text + ", " +str(id))
    
    id = None

file.close()
