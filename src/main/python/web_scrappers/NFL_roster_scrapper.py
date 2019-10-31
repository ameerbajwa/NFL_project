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
            print (list_of_teams[i].find_element_by_tag_name('a').get_attribute('href'))
            print (list_of_teams[i].find_element_by_tag_name('a').text)
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

sys.exit()


