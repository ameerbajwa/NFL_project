from src.main.python.web_scrappers import NFL_url_scrapper, NFL_team_scrapper, NFL_player_scrapper
import sys

exit_program = False

while (exit_program == False):
    print ('Welcome to the main scrapping central page!')
    action = input('Action?'
                   '("define_urls" to create scrapper for grabbing necessary urls,'
                   '"create_inserter" to create scrapper for inserting data,'
                   '"create_updater" to create scrapper to update data,'
                   '"exit" to exit program)')

    if (action == 'define_urls'):
        scrapper_type = input('What type of inserting scrapper do you want to create? ("team" for teams, "player_stats" for player stats, or "play_by_play" for play_by_play information) ')
        year = input('For which season year? ')

        if (scrapper_type == 'team'):
            type_of_info_from_teams = input('What type of team data do you want to be scrapped? ("roster" for roster data, "injury" for injury data, "team" for overall team statistics and personel information) ')
            NFL_url_scrapper.grabbing_nfl_team_urls(type_of_info_from_teams, year)
        elif (scrapper_type == 'player_stats'):
            week = input("Which week do you want player\'s data to be scrapped from?")
            NFL_url_scrapper.grabbing_nfl_game_urls(year, week)

    if (action == 'create_inserter'):
        scrapper_type = input('What type of inserting scrapper do you want to create? ("team" for teams, "player_stats" for player stats, or "play_by_play" for play_by_play information) ')
        year = input('For which season year? ')

        if (scrapper_type == 'team'):
            type_of_info_from_teams = input('What type of team data do you want to be scrapped? ("roster" for roster data, "injury" for injury data, "team" for overall team statistics and personel information) ')
            NFL_team_scrapper.selecting_info(type_of_info_from_teams, year)

    if (action == 'exit'):
        sys.exit()