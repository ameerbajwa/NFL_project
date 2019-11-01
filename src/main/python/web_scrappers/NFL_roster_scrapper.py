from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import time
import os
import sys

chromedriver = "/Applications/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.pro-football-reference.com/teams/")
time.sleep(1)
list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

list_of_active_teams = []

for i in range(0,len(list_of_teams)):
    if (i < len(list_of_teams)):
        try:
            list_of_active_teams.append(
                {
                    'team_name': list_of_teams[i].find_element_by_tag_name('a').text,
                    'team_url': list_of_teams[i].find_element_by_tag_name('a').get_attribute('href')
                }
            )
        except NoSuchElementException:
            pass
    else:
        break

print (list_of_active_teams)

for active_team in list_of_active_teams:
    driver.get(active_team['team_url'])
    time.sleep(1)

    team_roster_2019_2020_url = driver.find_element_by_xpath('//*[@id="team_index"]/tbody/tr[1]/td[2]/a').get_attribute('href')
    print (team_roster_2019_2020_url)
    active_team['team_url'] = team_roster_2019_2020_url

print (list_of_active_teams)

sys.exit()


