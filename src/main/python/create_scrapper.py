from src.main.python.web_scrappers import NFL_team_scrapper
import sys

print ('Welcome to the main scrapping central page!')
action = input('What do you want to do? ("c" to create scrapper ...) ')

if (action == 'c'):
    scrapper_type = input('What type of scrapper do you want to create? ("team" for teams, "player_stats" for player stats, or "play_by_play" for play_by_play information) ')
    year = input('For which season year? ')

    if (scrapper_type == 'team'):
        type_of_info_from_teams = input('What type of team data do you want to be scrapped? ("roster" for roster data, "injury" for injury data, "team" for overall team statistics and personel information) ')
        list_of_active_teams = NFL_team_scrapper.grabbing_nfl_team_urls(type_of_info_from_teams, year)

print (list_of_active_teams)
sys.exit()