from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.main.python.SQL_uploads import insert
from src.main.python.cleaning_scrapped_data import cleaning_scrapped_team_data

import pandas as pd
import time
import os
import pickle
import sys

chromedriver = "/Applications/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def grabbing_nfl_team_urls(type_of_info_from_teams, year):
    driver.get("https://www.pro-football-reference.com/teams/")
    time.sleep(1)
    list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

    list_of_active_teams = []
    i = 0
    team_counter = 0

    while i < len(list_of_teams):
        try:
            active_team = list_of_teams[i].find_element_by_tag_name('a').get_attribute('href')

            list_of_active_teams.append(
                {
                    'team_name': list_of_teams[i].find_element_by_tag_name('a').text,
                    'url': ''
                }
            )

            driver.get(active_team)
            time.sleep(2)

            active_teams = driver.find_elements_by_xpath('//*[@id="team_index"]/tbody//tr')
            for team in active_teams:
                if (team.find_element_by_tag_name('th').text == str(year)):
                    active_team = team.find_element_by_xpath('td[2]/a').get_attribute('href')

            driver.get(active_team)
            time.sleep(2)

            if (type_of_info_from_teams == 'roster'):
                list_of_active_teams[team_counter]['url'] = driver.find_element_by_xpath(
                    '//*[@id="inner_nav"]/ul/li[5]/a').get_attribute('href')
            elif (type_of_info_from_teams == 'injury'):
                list_of_active_teams[team_counter]['url'] = driver.find_element_by_xpath(
                    '//*[@id="inner_nav"]/ul/li[8]/a').get_attribute('href')
            elif (type_of_info_from_teams == 'team'):
                list_of_active_teams[team_counter]['url'] = active_team

            i += 1
            team_counter += 1

            driver.get('https://www.pro-football-reference.com/teams/')
            time.sleep(2)
            list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

        except NoSuchElementException:
            i += 1
            continue

    with open('dictionaries_of_nfl_urls/list_of_active_teams_' + type_of_info_from_teams + '_data_for_season_' + year,
              'wb') as handle:
        pickle.dump(list_of_active_teams, handle, protocol=pickle.HIGHEST_PROTOCOL)

def grabbing_nfl_game_urls(year, week):
    return year, week
