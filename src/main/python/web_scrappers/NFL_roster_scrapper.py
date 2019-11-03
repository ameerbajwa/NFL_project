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

list_of_active_teams_roster = []
print (len(list_of_teams))
i = 0
active_team_counter = 0
while i < len(list_of_teams):
    try:
        print (i)
        active_team = list_of_teams[i].find_element_by_tag_name('a').get_attribute('href')
        print (active_team_counter)

        list_of_active_teams_roster.append(
            {
                'team_name': list_of_teams[active_team_counter].find_element_by_tag_name('a').text,
                'roster_url': ''
            }
        )

        driver.get(active_team)
        time.sleep(2)

        active_team_2019 = driver.find_element_by_xpath('//*[@id="team_index"]/tbody/tr[1]/td[2]/a').get_attribute('href')
        driver.get(active_team_2019)
        time.sleep(2)

        list_of_active_teams_roster[active_team_counter]['roster_url'] = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[5]/a').get_attribute('href')
        print(list_of_active_teams_roster[active_team_counter])
        i+=1
        active_team_counter+=1
        driver.get('https://www.pro-football-reference.com/teams/')
        time.sleep(2)
        list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

    except NoSuchElementException:
        i+=1
        pass

sys.exit()


