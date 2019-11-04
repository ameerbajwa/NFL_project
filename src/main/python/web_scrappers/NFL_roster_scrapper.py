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

list_of_active_teams_roster = []
i = 0
active_team_counter = 0

while i < len(list_of_teams):
    try:
        active_team = list_of_teams[i].find_element_by_tag_name('a').get_attribute('href')

        list_of_active_teams_roster.append(
            {
                'team_name': list_of_teams[i].find_element_by_tag_name('a').text,
                'url': ''
            }
        )

        driver.get(active_team)
        time.sleep(2)

        active_team_2019 = driver.find_element_by_xpath('//*[@id="team_index"]/tbody/tr[1]/td[2]/a').get_attribute('href')

        driver.get(active_team_2019)
        time.sleep(2)

        list_of_active_teams_roster[active_team_counter]['url'] = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[5]/a').get_attribute('href')

        i += 1
        active_team_counter += 1

        driver.get('https://www.pro-football-reference.com/teams/')
        time.sleep(2)
        list_of_teams = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/table/tbody//th')

    except NoSuchElementException:
        i += 1
        continue

def grabbing_roster_info(list_of_active_teams):

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

                team_roster_df = team_roster_df.append(player_roster_info, ignore_index=True)

        print (team_roster_df)

# TEST
# test_dict = [{'team_name': 'Arizona Cardinals', 'url': 'https://www.pro-football-reference.com/teams/crd/2019_roster.htm'}]
# grabbing_roster_info(test_dict)

grabbing_roster_info(list_of_active_teams_roster)

sys.exit()