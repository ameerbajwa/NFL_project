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

def selecting_player_info(year, week):
    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year), 'rb') as handle:
        dict_of_game_summaries = pickle.load(handle)

    grab_offensive_player_data(dict_of_game_summaries)
    grab_defensive_player_data(dict_of_game_summaries)
    grab_special_teams_player_data(dict_of_game_summaries)

def grab_offensive_player_data(dict_of_game_summaries):

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        raw_basic_off_column_names = driver.find_elements_by_xpath('//*[@id="player_offense"]/thead/tr[2]//th')
        basic_off_column_names = []

        for basic_off_col in raw_basic_off_column_names:
            basic_off_column_names.append(basic_off_col.text)

        basic_off_player_stats_df = pd.DataFrame(columns=basic_off_column_names)

        basic_off_player_stats = driver.find_elements_by_xpath('//*[@id="player_offense"]/tbody//tr')

        for player in basic_off_player_stats:
            player_stats = {}
            if (len(player.find_elements_by_tag_name('th')) > 1):
                continue
            else:
                player_stats[basic_off_column_names[0]] = player.find_element_by_xpath('/th/a').text

                list_of_stats = []
                for stat in player.find_elements_by_tag_name('td'):
                    list_of_stats.append(stat.text)

                for i in range(1,len(basic_off_column_names)):
                    player_stats[basic_off_column_names[i]] = list_of_stats[i-1]

                basic_off_player_stats_df = basic_off_player_stats_df.append(player_stats, ignore_index=True)


def grab_defensive_player_data(dict_of_game_summaries):

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

    raw_basic_def_column_names = driver.find_elements_by_xpath('//*[@id="player_defense"]/thead/tr[2]//th')
    basic_def_column_names = []

    for basic_def_col in raw_basic_def_column_names:
        basic_def_column_names.append(basic_def_col.text)

    basic_def_player_stats_df = pd.DataFrame(columns=basic_def_column_names)

    basic_def_player_stats = driver.find_elements_by_xpath('//*[@id="player_defense"]/tbody//tr')

    for player in basic_def_player_stats:
        player_stats = {}
        if (len(player.find_elements_by_tag_name('th')) > 1):
            continue
        else:
            player_stats[basic_def_column_names[0]] = player.find_element_by_xpath('/th/a').text

            list_of_stats = []
            for stat in player.find_elements_by_tag_name('td'):
                list_of_stats.append(stat.text)

            for i in range(1, len(basic_def_column_names)):
                player_stats[basic_def_column_names[i]] = list_of_stats[i - 1]

            basic_def_player_stats_df = basic_def_player_stats_df.append(player_stats, ignore_index=True)

def grab_special_teams_player_data(dict_of_game_summaries):

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)