from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.main.python.SQL_uploads import insert
from src.main.python.cleaning_scrapped_data import cleaning_scrapped_game_stats_data

import pandas as pd
import time
import os
import pickle
import sys

def selecting_game_info(year, week):
    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year), 'rb') as handle:
        dict_of_game_summaries = pickle.load(handle)

    grab_game_summary_data(dict_of_game_summaries)
    grab_game_drive_summary_data(dict_of_game_summaries)

def grab_game_summary_data(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        game_summary_dict = {}
        game_summary_dict['week'] = dict_of_game_summaries['week']
        game_summary_dict['home_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a').text
        game_summary_dict['away_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a').text

        game_summary_dict['home_team_score'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div').text
        game_summary_dict['away_team_score'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div').text

        game_summary_dict['day_and_date_of_game'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[1]').text
        game_summary_dict['start_time_of_game'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[2]').text
        game_summary_dict['stadium_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[3]').text
        game_summary_dict['attendance'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[4]').text
        game_summary_dict['time_of_game'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[5]').text

        for row in driver.find_elements_by_xpath('//*[@id="game_info"]/tbody//tr'):
            if (row.find_element_by_tag_name('th').text == 'Won Toss'):
                game_summary_dict['won_toss'] = row.find_element_by_tag_name('td').text
            elif (row.find_element_by_tag_name('th').text == 'Roof'):
                game_summary_dict['roof'] = row.find_element_by_tag_name('td').text
            elif (row.find_element_by_tag_name('th').text == 'Surface'):
                game_summary_dict['surface'] = row.find_element_by_tag_name('td').text
            elif (row.find_element_by_tag_name('th').text == 'Weather'):
                game_summary_dict['weather'] = row.find_element_by_tag_name('td').text

        game_summary_df = pd.DataFrame(data=game_summary_dict, index=['_'.join(game_summary_dict['home_team_name'].split(' ')) + '_vs_' + '_'.join(game_summary_dict['away_team_name'].split(' '))])
        clean_game_summary_df = cleaning_scrapped_game_stats_data.cleaning_game_summary_data(game_summary_df)

def grab_game_drive_summary_data(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        game_drive_summary_dict = {}
        game_drive_summary_dict['week'] = dict_of_game_summaries['week']
        game_drive_summary_dict['home_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a').text
        game_drive_summary_dict['away_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a').text

        game_drive_summary_dict['day_and_date_of_game'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[1]').text

        raw_drive_summary_headers = driver.find_elements_by_xpath('//*[@id="home_drives"]/thead/tr//th')
        headers = ['week', 'home_team_name', 'away_team_name', 'day_and_date_of_game', 'team_drive']

        for header in raw_drive_summary_headers:
            headers.append(header.text)
        headers.remove('#')

        game_drive_summary_df = pd.DataFrame(columns=headers)
        drives = ['home_drives', 'vis_drives']

        for drive_index in range(0,len(drives)):
            game_drive_summary_dict['team_drive'] = driver.find_element_by_xpath('//*[@id="all_' + drives[drive_index] + '"]/div[1]/h2').text
            rows_in_drive = driver.find_elements_by_xpath('//*[@id="' + drives[drive_index] + '"]/tbody//tr')
            for row in rows_in_drive:
                header_index = 5
                list_of_values_of_drive = row.find_elements_by_tag_name('td')
                for col in list_of_values_of_drive:
                    game_drive_summary_dict[headers[header_index]] = col.text
                    header_index += 1
                game_drive_summary_df = game_drive_summary_df.append(game_drive_summary_dict, ignore_index=True)

        clean_game_drive_summary_df = cleaning_scrapped_game_stats_data.cleaning_game_drive_summary(game_drive_summary_df)

test_dict = {'year' : 2019, 'week': 1, 'list_of_game_summary_urls': ['https://www.pro-football-reference.com/boxscores/201909080mia.htm']}
grab_game_drive_summary_data(test_dict)

sys.exit()