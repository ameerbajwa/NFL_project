print ('Welcome to the main scrapping central page!')

from src.main.python.web_scrappers import NFL_url_scrapper, NFL_team_scrapper, NFL_player_scrapper, NFL_play_by_play_scrapper
import sys

exit_program = False

while (exit_program == False):

    action = input('Action? '
                   '("define_urls" to create scrapper for grabbing necessary urls,'
                   '"create_insert_scrapper" to create scrapper for inserting data,'
                   '"create_update_scrapper" to create scrapper to update data,'
                   '"exit" to exit program) ')

    if (action == 'define_urls'):
        scrapper_type = input('What type of urls do you want to grab? '
                              '("team" for teams, '
                              '"player_stats" for player stats, '
                              '"game_summary" for game summary, '
                              '"game_drive_summary" for both teams drives summaries from a game, '
                              'or "play_by_play" for play_by_play information) ')
        year = input('For which season year? ')

        if (scrapper_type == 'team'):
            type_of_info_from_teams = input('What type of team data do you want to be scrapped? '
                                            '("roster" for roster data, '
                                            '"injury" for injury data, '
                                            '"team" for overall team statistics and personnel information) ')
            NFL_url_scrapper.grabbing_nfl_team_urls(type_of_info_from_teams, year)

        elif (scrapper_type == 'player_stats' or scrapper_type == 'game_summary' or scrapper_type == 'game_drive_summary'):
            week = input("Which week do you want player\'s data to be scrapped from? ")
            NFL_url_scrapper.grabbing_nfl_game_urls(year, week)

    if (action == 'create_inserter'):
        scrapper_type = input('What type of inserting scrapper do you want to create? '
                              '("team" for teams, '
                              '"player_stats" for player stats, '
                              '"game_summary" for game summary, '
                              '"game_drive_summary" for both teams drives summaries from a game, '
                              'or "play_by_play" for play_by_play information) ')
        year = input('For which season year? ')

        if (scrapper_type == 'team'):
            type_of_info_from_teams = input('What type of team data do you want to be scrapped? '
                                            '("roster" for roster data, '
                                            '"injury" for injury data, '
                                            '"team" for overall team statistics and personnel information, '
                                            'or "off_def_team" for offensive and defensive team statistics over the course of the season) ')
            NFL_team_scrapper.selecting_team_info(type_of_info_from_teams, year)

        if (scrapper_type == 'player_stats'):
            week = input('For which week in ' + year + ' season? ')
            NFL_player_scrapper.selecting_player_info(year, week)

        if (scrapper_type == 'play_by_play'):
            week = input('For which week in ' + year + ' season? ')
            NFL_play_by_play_scrapper.selecting_play_by_play_info(year, week)

    if (action == 'exit'):
        exit_program = True

sys.exit()