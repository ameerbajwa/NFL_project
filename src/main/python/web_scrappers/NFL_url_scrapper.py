from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
import os
import pickle

def grabbing_nfl_team_urls(type_of_info_from_teams, year):
    chromedriver = "/usr/local/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    driver.get("https://www.pro-football-reference.com/teams/")
    time.sleep(1)
    list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

    list_of_active_teams = []
    i = 0
    team_counter = 0

    while i < len(list_of_teams):
        try:
            active_team = list_of_teams[i].find_element_by_tag_name('a').get_attribute('href')
            print(list_of_teams[i].find_element_by_tag_name('a').text)

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

            if type_of_info_from_teams == 'roster':
                list_of_active_teams[team_counter]['url'] = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[5]/a').get_attribute('href')
            elif type_of_info_from_teams == 'injury':
                list_of_active_teams[team_counter]['url'] = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[8]/a').get_attribute('href')
            elif type_of_info_from_teams == 'team' or type_of_info_from_teams == 'schedule' or type_of_info_from_teams == 'off_def_team':
                print(team.find_element_by_xpath('td[2]/a').text)
                list_of_active_teams[team_counter]['url'] = active_team

            i += 1
            team_counter += 1

            driver.get('https://www.pro-football-reference.com/teams/')
            time.sleep(2)
            list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

        except NoSuchElementException:
            i += 1
            continue

    with open('dictionaries_of_nfl_urls/list_of_active_teams_' + type_of_info_from_teams + '_data_for_season_' + year, 'wb') as handle:
        pickle.dump(list_of_active_teams, handle, protocol=pickle.HIGHEST_PROTOCOL)

def grabbing_nfl_game_urls(year, week):
    chromedriver = "/usr/local/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    driver.get('https://www.pro-football-reference.com/years/')
    time.sleep(1)

    list_of_seasons = driver.find_elements_by_xpath('//*[@id="years"]/tbody//tr')

    for season in list_of_seasons:
        if (str(year) == season.find_element_by_tag_name('a').text):
            driver.get(season.find_element_by_tag_name('a').get_attribute('href'))
            time.sleep(1)
            break
        else:
            continue

    list_of_weeks = driver.find_elements_by_xpath('//*[@id="div_week_games"]/div//div')

    for week_of_season in list_of_weeks:
        if (week == week_of_season.find_element_by_tag_name('a').text.split(' ')[1]):
            driver.get(week_of_season.find_element_by_tag_name('a').get_attribute('href'))
            time.sleep(1)
            break
        else:
            continue

    dict_of_game_summary_urls = {
        'year': year,
        'week': week,
        'list_of_game_summary_urls': []
    }
    list_of_game_summaries = driver.find_elements_by_xpath('//*[@id="content"]/div[5]//div')

    for game_summary in list_of_game_summaries:
        dict_of_game_summary_urls['list_of_game_summary_urls'].append(game_summary.find_element_by_xpath('//*[@id="content"]/div[5]/div[1]/table[1]/tbody/tr[2]/td[3]/a').get_attribute('href'))

    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year), 'wb') as handle:
        pickle.dump(dict_of_game_summary_urls, handle, protocol=pickle.HIGHEST_PROTOCOL)