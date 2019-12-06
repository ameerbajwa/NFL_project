from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.main.python.SQL_uploads import insert
from src.main.python.cleaning_scrapped_data import cleaning_scrapped_play_by_play_data

import pandas as pd
import time
import os
import pickle
import sys

def play_by_play_table_scrapper(driver, week):

    raw_column_names = driver.find_elements_by_xpath('//*[@id="pbp"]/thead/tr//th')
    column_names = []

    for col in raw_column_names[:8]:
        column_names.append(col)

    play_by_play_info_df = pd.DataFrame(columns=column_names)

    play_by_play_info = driver.find_elements_by_xpath('//*[@id="pbp"]/tbody//tr')

    for play in play_by_play_info:
        p = {}
        p['Quarter'] = play.find_element_by_tag_name('th').text
        counter = 1
        for val in play.find_elements_by_xpath('td')[:7]:
            if (val.text == ''):
                p[column_names[counter]] = 0
            else:
                p[column_names[counter]] = val.text
            counter += 1

        play_by_play_info_df.append(p, ignore_index=True)

    play_by_play_info_df['week'] = week
    play_by_play_info_df['date'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[1]').text
    play_by_play_info_df['home_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a').text
    play_by_play_info_df['away_team_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a').text

    starting_possession = driver.find_element_by_xpath('//*[@id="game_info"]/tbody/tr[1]/td').text

    return play_by_play_info_df, starting_possession

def grabbing_play_by_play_info(year, week):
    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year), 'rb') as handle:
        dict_of_game_summaries = pickle.load(handle)

    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        play_by_play_info_df = play_by_play_table_scrapper(driver, week)

        clean_play_by_play_info_df = cleaning_scrapped_play_by_play_data.cleaning_play_by_play_info(play_by_play_info_df)