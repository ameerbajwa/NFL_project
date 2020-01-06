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


def selecting_play_by_play_info(year, week):
    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year),
              'rb') as handle:
        dict_of_game_summaries = pickle.load(handle)

    grabbing_play_by_play_info(dict_of_game_summaries)


def determining_team_with_starting_possession(driver):
    home_team_full_name = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a').text
    away_team_full_name = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a').text

    home_team_name = home_team_full_name.split(' ')[-1]
    away_team_name = away_team_full_name.split(' ')[-1]

    won_toss_value = driver.find_element_by_xpath('//*[@id="game_info"]/tbody/tr[1]/td').text
    clean_won_toss_value = won_toss_value.replace('(', '').replace(')', '').split(' ')

    if ('deferred' in clean_won_toss_value):
        possession = clean_won_toss_value[0]
    else:
        if (clean_won_toss_value[0] == home_team_name):
            possession = away_team_name
        else:
            possession = home_team_name

    return possession, home_team_name, away_team_name


def play_by_play_table_scrapper(driver, week):
    possession, home_team_name, away_team_name = determining_team_with_starting_possession(driver)

    raw_column_names = driver.find_elements_by_xpath('//*[@id="pbp"]/thead/tr//th')
    column_names = []

    for col in raw_column_names[:8]:
        if (col == away_team_name):
            column_names.append('away_team_score')
        elif (col == home_team_name):
            column_names.append('home_team_score')
        else:
            column_names.append(col.text)

    print(column_names)

    play_by_play_info_df = pd.DataFrame(columns=column_names)
    play_by_play_info_df['possession'] = ''

    play_by_play_info = driver.find_elements_by_xpath('//*[@id="pbp"]/tbody//tr')

    for play in play_by_play_info:
        if (len(play.find_elements_by_xpath('td')) > 1):
            p = {}
            p['Quarter'] = play.find_element_by_tag_name('th').text
            counter = 1
            for val in play.find_elements_by_xpath('td')[:7]:
                if (val.text == ''):
                    p[column_names[counter]] = '0'
                else:
                    p[column_names[counter]] = val.text
                counter += 1
            if (play.get_attribute('class') == 'divider'):
                if (possession == home_team_name):
                    possession = away_team_name
                else:
                    possession = home_team_name
            p['possession'] = possession

            play_by_play_info_df = play_by_play_info_df.append(p, ignore_index=True)
        else:
            pass

    play_by_play_info_df['week'] = week
    play_by_play_info_df['date'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[1]').text
    play_by_play_info_df['home_team_full_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a').text
    play_by_play_info_df['away_team_full_name'] = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a').text

    return play_by_play_info_df


def grabbing_play_by_play_info(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    week = dict_of_game_summaries['week']

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        play_by_play_info_df = play_by_play_table_scrapper(driver, week)

        clean_play_by_play_info_df = cleaning_scrapped_play_by_play_data.cleaning_play_by_play_info(play_by_play_info_df)

        insert.insert_play_by_play_stats_to_mysql(clean_play_by_play_info_df)


test_dict = {'year': 2019, 'week': 1, 'list_of_game_summary_urls': ['https://www.pro-football-reference.com/boxscores/201909080min.htm']}
grabbing_play_by_play_info(test_dict)

sys.exit()

# test = 'Matt Ryan pass incomplete short left intended for Austin Hooper. Penalty on Kris Boyd: Defensive Pass Interference, 9 yards (no play)'
#
# print (' '.join(test.split('Penalty')[1].split(':')[0].split(' ')[2:]))
