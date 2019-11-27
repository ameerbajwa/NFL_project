from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.main.python.SQL_uploads import insert
from src.main.python.cleaning_scrapped_data import cleaning_scrapped_player_stats_data

import pandas as pd
import time
import os
import pickle
import sys

def selecting_player_info(year, week):
    with open('dictionaries_of_nfl_urls/list_of_game_summaries_from_week_' + str(week) + '_season_' + str(year), 'rb') as handle:
        dict_of_game_summaries = pickle.load(handle)

    grab_offensive_player_data(dict_of_game_summaries)
    grab_defensive_player_data(dict_of_game_summaries)
    grab_special_teams_player_data(dict_of_game_summaries)

def table_scrapper(id_of_table, driver):

    # unique ids_for_table scrapping of player stats by game: player_offense, passing_advanced, rushing_advanced, receiving_advanced, player_defense, defense_advanced

    # FOR COLUMN NAMES FOR THE BASIC OFFENSE AND DEFENSE TABLE, HAVE TO GRAB BOTH ROWS OF THEADS TO DIFFER BETWEEN THE
    #  PASSING, RUSHING, AND RECEIVING COLUMNS

    if (len(driver.find_elements_by_xpath('//*[@id="' + id_of_table + '"]/thead//tr')) > 1):
        raw_column_names = driver.find_elements_by_xpath('//*[@id="' + id_of_table + '"]/thead/tr[2]//th')  # id_of_table
    else:
        raw_column_names = driver.find_elements_by_xpath('//*[@id="' + id_of_table + '"]/thead/tr//th')

    column_names = []

    if (len(driver.find_elements_by_xpath('//*[@id="' + id_of_table + '"]/thead//tr')) > 1):
        raw_headers = driver.find_elements_by_xpath('//*[@id="' + id_of_table + '"]/thead/tr[1]//th')
        headers = []
        headers.append({'header_name': '', 'number_of_columns_covered': 2})
        for head in raw_headers[1:]:
            header_dict = {}
            header_dict['header_name'] = head.text
            if (header_dict['header_name'] == ''):
                header_dict['number_of_columns_covered'] = 1
            else:
                header_dict['number_of_columns_covered'] = int(head.get_attribute('colspan'))
            headers.append(header_dict)

        header_counter = 0
        start = headers[header_counter]['number_of_columns_covered']
        end = headers[header_counter + 1]['number_of_columns_covered'] + 2
        column_names.append(raw_column_names[0].text)
        column_names.append(raw_column_names[1].text)
        for col_index in range(2,len(raw_column_names)):
            if (col_index >= start and col_index < end):
                if (col_index == 8 and id_of_table == 'player_offense'):
                    column_names.append(headers[header_counter + 1]['header_name'] + '_sacked_' + raw_column_names[col_index].text)
                else:
                    column_names.append(headers[header_counter + 1]['header_name'] + '_' + raw_column_names[col_index].text)
            else:
                header_counter += 1
                if (headers[header_counter + 1]['header_name'] == ''):
                    column_names.append(raw_column_names[col_index].text)
                    header_counter += 1
                    start = end + 1
                    end += (headers[header_counter + 1]['number_of_columns_covered']) + 1
                else:
                    column_names.append(headers[header_counter + 1]['header_name'] + '_' + raw_column_names[col_index].text)
                    start = end + 1
                    end += (headers[header_counter + 1]['number_of_columns_covered'])
    else:
        for col in raw_column_names:
            column_names.append(col.text)

    player_stats_df = pd.DataFrame(columns=column_names)

    player_stats = driver.find_elements_by_xpath('//*[@id="'+ id_of_table + '"]/tbody//tr') # id_of_table

    for player in player_stats:
        player_stats = {}
        if (len(player.find_elements_by_tag_name('th')) > 1):
            continue
        else:
            player_stats[column_names[0]] = player.find_element_by_tag_name('th').text

            list_of_stats = []
            for stat in player.find_elements_by_tag_name('td'):
                list_of_stats.append(stat.text)

            for i in range(1, len(column_names)):
                if (list_of_stats[i-1] == ''):
                    list_of_stats[i-1] = 0
                player_stats[column_names[i]] = list_of_stats[i - 1]

            player_stats_df = player_stats_df.append(player_stats, ignore_index=True)

    print (player_stats_df)
    return (player_stats_df)

def grab_offensive_player_data(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        basic_off_player_stats_df = table_scrapper('player_offense', driver)
        adv_passing_player_stats_df = table_scrapper('passing_advanced', driver)
        adv_rushing_player_stats_df = table_scrapper('rushing_advanced', driver)
        adv_receiving_player_stats_df = table_scrapper('receiving_advanced', driver)

        # clean_passing_stats_df = cleaning_scrapped_player_stats_data.cleaning_offensive_player_stats(basic_off_player_stats_df, adv_passing_player_stats_df, 'passing')
        # clean_rushing_stats_df = cleaning_scrapped_player_stats_data.cleaning_offensive_player_stats(basic_off_player_stats_df, adv_rushing_player_stats_df, 'rushing')
        # clean_receiving_stats_df = cleaning_scrapped_player_stats_data.cleaning_offensive_player_stats(basic_off_player_stats_df, adv_receiving_player_stats_df, 'receiving')

def grab_defensive_player_data(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        basic_def_player_stats_df = table_scrapper('player_defense', driver)
        adv_def_player_stats_df = table_scrapper('defense_advanced', driver)

        # cleaning_defensive_stats_df = cleaning_scrapped_player_stats_data.cleaning_defensive_stats(basic_def_player_stats_df, adv_def_player_stats_df)

def grab_special_teams_player_data(dict_of_game_summaries):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for game_summary in dict_of_game_summaries['list_of_game_summary_urls']:
        driver.get(game_summary)
        time.sleep(1)

        return_player_stats_df = table_scrapper('returns', driver) # //*[@id="returns"]/thead
        kicking_punting_player_stats_df = table_scrapper('kicking', driver) # //*[@id="kicking"]/thead

# test_dict = {'year' : 2019, 'week': 1, 'list_of_game_summary_urls': ['https://www.pro-football-reference.com/boxscores/201909080tam.htm']}
# grab_offensive_player_data(test_dict)
#
# sys.exit()