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

    grab_passing_data(dict_of_game_summaries)
    grab_rushing_data(dict_of_game_summaries)
    grab_receiving_data(dict_of_game_summaries)
    grab_defensive_data(dict_of_game_summaries)
    grab_kicking_data(dict_of_game_summaries)
    grab_return_data(dict_of_game_summaries)

def grab_passing_data(dict_of_game_summaries):
    return dict_of_game_summaries

def grab_rushing_data(dict_of_game_summaries):
    return dict_of_game_summaries

def grab_receiving_data(dict_of_game_summaries):
    return dict_of_game_summaries

def grab_defensive_data(dict_of_game_summaries):
    return dict_of_game_summaries

def grab_kicking_data(dict_of_game_summaries):
    return dict_of_game_summaries

def grab_return_data(dict_of_game_summaries):
    return dict_of_game_summaries