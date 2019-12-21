from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from src.main.python.SQL_uploads import insert
from src.main.python.cleaning_scrapped_data import cleaning_scrapped_team_data

import pandas as pd
import time
import os
import pickle
import sys


def selecting_team_info(type_of_info_from_teams, year):
    with open('dictionaries_of_nfl_urls/list_of_active_teams_' + type_of_info_from_teams + '_data_for_season_' + year, 'rb') as handle:
        list_of_active_teams = pickle.load(handle)

    if (type_of_info_from_teams == 'roster'):
        grabbing_team_info(list_of_active_teams)
    elif (type_of_info_from_teams == 'injury'):
        grabbing_injury_info(list_of_active_teams)
    elif (type_of_info_from_teams == 'team'):
        grabbing_team_info(list_of_active_teams)
    elif (type_of_info_from_teams == 'off_def_team'):
        grabbing_off_and_def_team_info(list_of_active_teams)


def grabbing_roster_info(list_of_active_teams):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for active_team_index in range(0, len(list_of_active_teams)):
        driver.get(list_of_active_teams[active_team_index]['url'])
        time.sleep(2)

        raw_roster_column_names = driver.find_elements_by_xpath('//*[@id="games_played_team"]/thead/tr//th')
        roster_column_names = []

        for raw_roster_col_index in range(0,len(raw_roster_column_names)):
            roster_column_names.append(raw_roster_column_names[raw_roster_col_index].text)
        roster_column_names.insert(2, 'Team')

        team_roster_df = pd.DataFrame(columns=roster_column_names)

        raw_roster_info = driver.find_elements_by_xpath('//*[@id="games_played_team"]/tbody//tr')

        for row in raw_roster_info:
            player_roster_info = {}
            if (len(row.find_elements_by_tag_name('th')) > 1):
                continue
            else:
                player_roster_info[roster_column_names[0]] = row.find_element_by_tag_name('th').text

                list_of_values_for_row = []
                for col in row.find_elements_by_tag_name('td'):
                    list_of_values_for_row.append(col.text)
                list_of_values_for_row.insert(1, list_of_active_teams[active_team_index]['team_name'])

                for roster_col_index in range(1, len(roster_column_names)):
                    player_roster_info[roster_column_names[roster_col_index]] = list_of_values_for_row[roster_col_index-1]
                print(player_roster_info)
                team_roster_df = team_roster_df.append(player_roster_info, ignore_index=True)

        cleaned_team_roster_df = cleaning_scrapped_team_data.cleaning_NFL_roster_data(team_roster_df)
        insert.insert_roster_info_to_mysql(cleaned_team_roster_df)


def grabbing_injury_info(list_of_active_teams_injury_reports):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for active_team_injury_report_index in range(0,len(list_of_active_teams_injury_reports)):
        driver.get(list_of_active_teams_injury_reports[active_team_injury_report_index]['url'])
        time.sleep(2)
        injury_report_url = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[8]/a').get_attribute('href')
        driver.get(injury_report_url)
        time.sleep(2)

        raw_column_names = driver.find_elements_by_xpath('//*[@id="team_injuries"]/thead/tr//th')
        column_names = []

        for col_index in range(0,len(raw_column_names)):
            if (col_index == 0):
                column_names.append('Player')
            else:
                column_names.append('game_' + str(col_index))

        injury_report_df = pd.DataFrame(columns=column_names)

        injury_data = driver.find_elements_by_xpath('//*[@id="team_injuries"]/tbody//tr')

        for injured_player in injury_data:
            player = {}
            player['Player'] = injured_player.find_element_by_tag_name('th').text
            injury_timeline = injured_player.find_elements_by_xpath('td')
            for injury_time_index in range(1,len(injury_timeline)+1):
                if (injury_timeline[injury_time_index-1].text == ''):
                    player[column_names[injury_time_index]] = 'NA'
                else:
                    player[column_names[injury_time_index]] = injury_timeline[injury_time_index - 1].text

            injury_report_df = injury_report_df.append(player, ignore_index=True)

        cleaned_injury_report_df = cleaning_scrapped_team_data.cleaning_NFL_injury_report(injury_report_df)


def grabbing_team_info(list_of_active_teams):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for active_team_index in range(0, len(list_of_active_teams)):
        driver.get(list_of_active_teams[active_team_index]['url'])
        time.sleep(2)

        team_info = driver.find_elements_by_xpath('//*[@id="meta"]/div[2]//p')

        team_info_dict = {}

        for info_index in range(0,len(team_info)):
            team_info_dict['team'] = list_of_active_teams[active_team_index]['team_name']
            if (info_index == 0):
                team_info_dict['wins'] = int(team_info[info_index].text.split(',')[0].split(' ')[1].split('-')[0])
                team_info_dict['losses'] = int(team_info[info_index].text.split(',')[0].split(' ')[1].split('-')[1])
                if (len(team_info[info_index].text.split(',')[0].split(' ')[1].split('-')) > 2):
                    team_info_dict['ties'] = int(team_info[info_index].text.split(',')[0].split(' ')[1].split('-')[2])
                else:
                    team_info_dict['ties'] = 0
                team_info_dict['conference'] = team_info[info_index].text.split(',')[1].split(' ')[3]
                team_info_dict['division'] = team_info[info_index].text.split(',')[1].split(' ')[4]
            elif (info_index == 1):
                team_info_dict['coach'] = team_info[info_index].text.split(' ')[1] + ' ' + team_info[info_index].text.split(' ')[2]
            else:
                continue

        team_info_df = pd.DataFrame(data=team_info_dict, index=[list_of_active_teams[active_team_index]['team_name']])
        # NO CLEANING OF THE NFL OVERALL TEAM DATA NEEDED, SO CAN GO STRAIGHT TO INSERTING DATAFRAME TO MYSQL
        insert.insert_overall_team_info_to_mysql(team_info_df)


def grabbing_team_schedule(list_of_active_teams):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for active_team_index in range(0, len(list_of_active_teams)):
        driver.get(list_of_active_teams[active_team_index]['url'])
        time.sleep(2)

        raw_column_names = driver.find_elements_by_xpath('//*[@id="games"]/thead/tr[2]//th')[:10]
        column_names = []

        for raw_col_index in range(0,len(raw_column_names)):
            column_names.append(raw_column_names[raw_col_index].text)

        column_names[3] = 'Time_Game_Starts'
        column_names[4] = 'Boxscore'
        column_names[5] = 'Won/Loss'
        column_names[8] = 'Home/Away'
        column_names.append('Team')

        team_schedule_df = pd.DataFrame(columns=column_names)

        team_schedule_data = driver.find_elements_by_xpath('//*[@id="games"]/tbody//tr')

        for data in team_schedule_data:
            week = {}
            week[column_names[0]] = data.find_element_by_xpath('th').text
            datapoints = data.find_elements_by_xpath('td')[:9]
            for val_index in range(0,len(datapoints)):
                week[column_names[val_index+1]] = datapoints[val_index].text
            week['Team'] = ('_'.join(driver.find_elements_by_xpath('//*[@id="meta"]/div[2]/h1/span[2]').text.split(' '))) + ':week_' + week[column_names[0]]

            team_schedule_df = team_schedule_df.append(week, ignore_index=True)

        print (team_schedule_df)
        clean_team_schedule_df = cleaning_scrapped_team_data.cleaning_NFL_team_schedule(team_schedule_df)
        insert.insert_team_schedule_data(clean_team_schedule_df)


def grabbing_off_and_def_team_info(list_of_active_teams):
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    for active_team_index in range(0, len(list_of_active_teams)):
        driver.get(list_of_active_teams[active_team_index]['url'])
        time.sleep(2)

        raw_column_headers_part_1 = driver.find_elements_by_xpath(('//*[@id="team_stats"]/thead/tr[1]//th'))
        raw_column_names_part_1 = driver.find_elements_by_xpath('//*[@id="team_stats"]/thead/tr[2]//th')
        raw_column_names_part_2 = driver.find_elements_by_xpath('//*[@id="team_conversions"]/thead/tr[2]//th')
        team_stats_column_names = []

        raw_header_index = 1
        inside_counter = 0
        for raw_col_index in range(1,len(raw_column_names_part_1)):
            if (raw_column_headers_part_1[raw_header_index].text != ''):
                if (inside_counter < int(raw_column_headers_part_1[raw_header_index].get_attribute('colspan'))):
                    if (len(raw_column_headers_part_1[raw_header_index].text.split(' ')) > 1):
                        column_header = '_'.join(raw_column_headers_part_1[raw_header_index].text.split(' '))
                    else:
                        column_header = raw_column_headers_part_1[raw_header_index].text
                    inside_counter += 1
                    team_stats_column_names.append(column_header + '_' + raw_column_names_part_1[raw_col_index].text)
                else:
                    inside_counter = 0
                    raw_header_index += 1
                    if (raw_column_headers_part_1[raw_header_index].text != ''):
                        if (len(raw_column_headers_part_1[raw_header_index].text.split(' ')) > 1):
                            column_header = '_'.join(raw_column_headers_part_1[raw_header_index].text.split(' '))
                        else:
                            column_header = raw_column_headers_part_1[raw_header_index].text
                        inside_counter += 1
                        team_stats_column_names.append(column_header + '_' + raw_column_names_part_1[raw_col_index].text)
                    else:
                        team_stats_column_names.append(raw_column_names_part_1[raw_col_index].text)
                        if (raw_col_index >= 23 and raw_col_index <= 25 and inside_counter < int(raw_column_headers_part_1[raw_header_index].get_attribute('colspan'))-1):
                            inside_counter += 1
                        else:
                            raw_header_index += 1
                            inside_counter = 0
            else:
                team_stats_column_names.append(raw_column_names_part_1[raw_col_index].text)
                if (raw_col_index >= 23 and raw_col_index <= 25 and inside_counter < int(raw_column_headers_part_1[raw_header_index].get_attribute('colspan'))-1):
                    inside_counter += 1
                else:
                    raw_header_index += 1
                    inside_counter = 0

        for raw_col_index in range(1,len(raw_column_names_part_2)):
            team_stats_column_names.append(raw_column_names_part_2[raw_col_index].text)

        team_off_stats_dict = {}
        team_def_stats_dict = {}

        team_off_stats_1 = driver.find_elements_by_xpath('//*[@id="team_stats"]/tbody/tr[1]//td')
        team_off_stats_2 = driver.find_elements_by_xpath('//*[@id="team_conversions"]/tbody/tr[1]//td')

        for off_index in range(0, len(team_off_stats_1)):
            team_off_stats_dict[team_stats_column_names[off_index]] = team_off_stats_1[off_index].text
        for off_index in range(0, len(team_off_stats_2)):
            team_off_stats_dict[team_stats_column_names[off_index + len(raw_column_names_part_1) - 1]] = team_off_stats_2[off_index].text

        team_off_stats_df = pd.DataFrame(data=team_off_stats_dict, index=[list_of_active_teams[active_team_index]['team_name']])

        team_def_stats_1 = driver.find_elements_by_xpath('//*[@id="team_stats"]/tbody/tr[2]//td')
        team_def_stats_2 = driver.find_elements_by_xpath('//*[@id="team_conversions"]/tbody/tr[2]//td')

        for def_index in range(0, len(team_def_stats_1)):
            team_def_stats_dict[team_stats_column_names[def_index]] = team_def_stats_1[def_index].text
        for def_index in range(0, len(team_def_stats_2)):
            team_def_stats_dict[team_stats_column_names[def_index + len(raw_column_names_part_1) - 1]] = team_def_stats_2[def_index].text

        team_def_stats_df = pd.DataFrame(data=team_def_stats_dict, index=[list_of_active_teams[active_team_index]['team_name']])

        # NO CLEANING OF THE NFL TEAM OFFENSIVE AND DEFENSIVE DATA NEEDED, SO CAN GO STRAIGHT TO INSERTING DATAFRAME TO MYSQL
        insert.insert_team_off_stats_to_mysql(team_off_stats_df)
        insert.insert_team_def_stats_to_mysql(team_def_stats_df)


# TEST
# test_dict = [{'team_name': 'Arizona Cardinals', 'url': 'https://www.pro-football-reference.com/teams/crd/2019_roster.htm'}]
# grabbing_roster_info(test_dict)

# test_dict = [{'team_name' : 'Arizona Caridinals', 'url': 'https://www.pro-football-reference.com/teams/crd/2019.htm'}]
# grabbing_team_info(test_dict)

test_dict = [{'team_name' : 'Arizona Caridinals', 'url': 'https://www.pro-football-reference.com/teams/crd/2019.htm'}]
grabbing_injury_info(test_dict)

sys.exit()