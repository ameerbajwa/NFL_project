import pymysql
import pandas as pd
import random
import string

def connect_to_mysql_system():
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user='root',
                                password='%s',
                                host='127.0.0.1',
                                port=3306,
                                database='NFL_database'
                             ) % (connection_to_local_mysql_data_management_system.columns[1])
    return (connection_to_database)

def insert_roster_info_to_mysql(team_roster_info):

    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(team_roster_info)):
        insert_SQL_query = "INSERT INTO `NFL_roster_info_2019_2020_season` " \
                           "(" \
                           "    player_number," \
                           "    player_name," \
                           "    team," \
                           "    age," \
                           "    position," \
                           "    games_played," \
                           "    games_started," \
                           "    weight," \
                           "    height," \
                           "    college," \
                           "    birth_date," \
                           "    years," \
                           "    drafted," \
                           "    salary" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query,
                            (
                               str(team_roster_info.loc[i, 'No.']),
                               team_roster_info.loc[i, 'Player '],
                               team_roster_info.loc[i, 'Team'],
                               str(team_roster_info.loc[i, 'Age']),
                               team_roster_info.loc[i, 'Pos'],
                               str(team_roster_info.loc[i, 'G']),
                               str(team_roster_info.loc[i, 'GS']),
                               str(team_roster_info.loc[i, 'Wt']),
                               str(team_roster_info.loc[i, 'Ht']),
                               team_roster_info.loc[i, 'College/Univ'],
                               str(team_roster_info.loc[i, 'BirthDate']),
                               str(team_roster_info.loc[i, 'Yrs']),
                               team_roster_info.loc[i, 'Drafted (tm/rnd/yr)'],
                               str(team_roster_info.loc[i, 'Salary'])
                            )
                          )

    connection_to_database.commit()
    print(team_roster_info.loc[0, 'Team'] + ' roster insertion to mysql table complete!')

def insert_overall_team_info_to_mysql(overall_team_info):
    team_name = overall_team_info.loc['Arizona Caridinals', 'team']
    connection_to_database = connect_to_mysql_system()

    insert_SQL_query = "INSERT INTO `NFL_team_info_2019_2020_season`" \
                       "(" \
                       "    team," \
                       "    wins," \
                       "    losses," \
                       "    ties," \
                       "    conference," \
                       "    division," \
                       "    coach" \
                       ") VALUES (%s, %s, %s, %s, %s, %s, %s);"

    with connection_to_database.cursor() as cursor:
        cursor.execute(insert_SQL_query,
                       (
                            overall_team_info.loc[team_name, 'team'],
                            str(overall_team_info.loc[team_name, 'wins']),
                            str(overall_team_info.loc[team_name, 'losses']),
                            str(overall_team_info.loc[team_name, 'ties']),
                            overall_team_info.loc[team_name, 'conference'],
                            overall_team_info.loc[team_name, 'division'],
                            overall_team_info.loc[team_name, 'coach']
                       )
                      )

    connection_to_database.commit()
    print (team_name + ' overall team info insertion to mysql table complete!')

def insert_team_off_stats_to_mysql(team_off_stats_df):
    connection_to_database = connect_to_mysql_system()

    insert_SQL_query = "INSERT INTO `NFL_team_offensive_statistics_2019_2020_season`" \
                       "(" \
                       "team," \
                       "points_scored_by_team," \
                        "yards_gained_by_team," \
                        "offensive_plays_by_team," \
                        "yards_per_offensive_play_by_team," \
                        "turnovers_lost_by_team," \
                        "fumbles_lost_by_team," \
                        "first_downs_completed_by_team," \
                        "passes_completed_by_team," \
                        "passes_attempted_by_team," \
                        "yards_gained_through_passing_by_team," \
                        "passing_touchdowns_by_team," \
                        "interceptions_thrown_by_team," \
                        "net_yards_gained_per_pass_attempt_by_team," \
                        "first_downs_through_passing_by_team," \
                        "rushing_attempts_by_team," \
                        "yards_gained_through_rushing_by_team," \
                        "rushing_touchdowns_by_team," \
                        "rushing_yards_per_attempt," \
                        "first_downs_through_rushing_by_team," \
                        "penalties_committed_by_opposing_teams_and_accepted_by_team," \
                        "penalty_yards_accrued_from_opposing_teams," \
                        "first_downs_through_opposing_teams_penalties," \
                        "number_of_drives_by_team," \
                        "per_of_drives_resulting_in_off_score_by_team," \
                        "per_of_drives_resulting_in_off_turnover_by_team," \
                        "average_starting_field_position_by_team," \
                        "average_time_per_drive_by_team," \
                        "average_number_of_plays_per_drive_by_team," \
                        "net_yards_per_drive_by_team," \
                        "average_points_scored_per_drive_by_team," \
                        "third_down_attempts_by_team," \
                        "third_down_conversions_by_team," \
                        "third_down_conversion_per_by_team," \
                        "fourth_down_attempts_by_team," \
                        "fourth_down_conversions_by_team," \
                        "fourth_down_conversion_per_by_team," \
                        "red_zone_attempts_by_team," \
                        "red_zone_touchdown_conversions_by_team," \
                        "red_zone_touchdown_conversion_per_by_team" \
                        ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                       ");"

    with connection_to_database.cursor() as cursor:
        cursor.execute(insert_SQL_query, (
            team_off_stats_df.index[0],
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'PF']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Yds']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Tot_Yds_&_TO_Ply']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Tot_Yds_&_TO_Y/P']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Tot_Yds_&_TO_TO']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'FL']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'1stD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_Cmp']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_Att']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_Yds']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_TD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_Int']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_NY/A']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Passing_1stD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Rushing_Att']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Rushing_Yds']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Rushing_TD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Rushing_Y/A']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Rushing_1stD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Penalties_Pen']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Penalties_Yds']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Penalties_1stPy']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'#Dr']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Sc%']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'TO%']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Average_Drive_Start']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Average_Drive_Time']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Average_Drive_Plays']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Average_Drive_Yds']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'Average_Drive_Pts']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'3DAtt']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'3DConv']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'3D%']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'4DAtt']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'4DConv']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'4D%']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'RZAtt']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'RZTD']),
            str(team_off_stats_df.loc[team_off_stats_df.index[0],'RZPct'])
        ))

    connection_to_database.commit()
    print (team_off_stats_df.index[0] + ' offensive team stats insertion to mysql table complete!')

def insert_team_def_stats_to_mysql(team_def_stats_df):
    connection_to_database = connect_to_mysql_system()
    
    insert_SQL_query = "INSERT INTO `NFL_team_defensive_statistics_2019_2020_season`" \
                       "(" \
                       "        team," \
                                "points_scored_allowed_by_team," \
                                "yards_gained_by_opposing_teams," \
                                "offensive_plays_by_opposing_teams," \
                                "yards_per_offensive_play_by_opposing_teams," \
                                "turnovers_lost_by_opposing_teams," \
                                "fumbles_lost_by_opposing_teams," \
                                "first_downs_completed_by_opposing_teams," \
                                "passes_completed_by_opposing_teams," \
                                "passes_attempted_by_opposing_teams," \
                                "yards_gained_through_passing_by_opposing_teams," \
                                "passing_touchdowns_by_opposing_teams," \
                                "interceptions_thrown_by_opposing_teams," \
                                "net_yards_gained_per_pass_attempt_by_opposing_teams," \
                                "first_downs_through_passing_by_opposing_teams," \
                                "rushing_attempts_by_opposing_teams," \
                                "yards_gained_through_rushing_by_opposing_teams," \
                                "rushing_touchdowns_by_opposing_teams," \
                                "rushing_yards_per_attempt_by_opposing_teams," \
                                "first_downs_through_rushing_by_opposing_teams," \
                                "penalties_committed_by_team_and_accepted_by_opposing_teams," \
                                "penalty_yards_accrued_from_team," \
                                "first_downs_by_teams_penalties," \
                                "number_of_drives_by_opposing_teams," \
                                "per_of_drives_resulting_in_off_score_by_opposing_teams," \
                                "per_of_drives_resulting_in_off_turnover_by_opposing_teams," \
                                "average_starting_field_position_by_opposing_teams," \
                                "average_time_per_drive_by_opposing_teams," \
                                "average_number_of_plays_per_drive_by_opposing_teams," \
                                "net_yards_per_drive_by_opposing_teams," \
                                "average_points_scored_per_drive_by_opposing_teams," \
                                "third_down_attempts_by_opposing_teams," \
                                "third_down_conversions_by_opposing_teams," \
                                "third_down_conversion_per_by_opposing_teams," \
                                "fourth_down_attempts_by_opposing_teams," \
                                "fourth_down_conversions_by_opposing_teams," \
                                "fourth_down_conversion_per_by_opposing_teams," \
                                "red_zone_attempts_by_opposing_teams," \
                                "red_zone_touchdown_conversions_by_opposing_teams," \
                                "red_zone_touchdown_conversion_per_by_opposing_teams" \
                       ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                       ");"

    with connection_to_database.cursor() as cursor:
        cursor.execute(insert_SQL_query, (
            team_def_stats_df.index[0],
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'PF']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Yds']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Tot_Yds_&_TO_Ply']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Tot_Yds_&_TO_Y/P']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Tot_Yds_&_TO_TO']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'FL']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '1stD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_Cmp']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_Att']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_Yds']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_TD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_Int']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_NY/A']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Passing_1stD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Rushing_Att']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Rushing_Yds']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Rushing_TD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Rushing_Y/A']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Rushing_1stD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Penalties_Pen']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Penalties_Yds']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Penalties_1stPy']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '#Dr']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Sc%']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'TO%']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Average_Drive_Start']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Average_Drive_Time']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Average_Drive_Plays']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Average_Drive_Yds']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'Average_Drive_Pts']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '3DAtt']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '3DConv']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '3D%']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '4DAtt']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '4DConv']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], '4D%']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'RZAtt']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'RZTD']),
            str(team_def_stats_df.loc[team_def_stats_df.index[0], 'RZPct'])
        ))

    connection_to_database.commit()
    print (team_def_stats_df.index[0] + ' defensive team stats insertion to mysql table complete!')

def insert_game_summary_data_to_mysql(game_summary_df):
    connection_to_database = connect_to_mysql_system()
    game_id = game_summary_df.index[0]

    insert_SQL_query = "INSERT INTO `game_summary_2019_2020_season`" \
                       "(" \
                       "    game," \
                       "    home_team," \
                       "    away_team," \
                       "    week," \
                       "    date," \
                       "    year," \
                       "    month," \
                       "    day," \
                       "    hour," \
                       "    minute," \
                       "    day_of_week," \
                       "    stadium," \
                       "    attendance," \
                       "    time_of_game," \
                       "    won_toss," \
                       "    roof," \
                       "    surface," \
                       "    weather," \
                       "    score_of_home_team," \
                       "    score_of_away_team" \
                       ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                       "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    with connection_to_database.cursor() as cursor:
        cursor.execute(insert_SQL_query,
                       (
                           game_id,
                           game_summary_df.loc[game_id, 'home_team_name'],
                           game_summary_df.loc[game_id, 'away_team_name'],
                           int(game_summary_df.loc[game_id, 'week']),
                           str(game_summary_df.loc[game_id, 'date']),
                           int(game_summary_df.loc[game_id, 'year']),
                           int(game_summary_df.loc[game_id, 'month']),
                           int(game_summary_df.loc[game_id, 'day']),
                           int(game_summary_df.loc[game_id, 'hour']),
                           int(game_summary_df.loc[game_id, 'minute']),
                           game_summary_df.loc[game_id, 'day_of_week'],
                           game_summary_df.loc[game_id, 'stadium_name'],
                           int(game_summary_df.loc[game_id, 'attendance']),
                           int(game_summary_df.loc[game_id, 'time_of_game']),
                           game_summary_df.loc[game_id, 'won_toss'],
                           game_summary_df.loc[game_id, 'roof'],
                           game_summary_df.loc[game_id, 'surface'],
                           game_summary_df.loc[game_id, 'weather'],
                           int(game_summary_df.loc[game_id, 'home_team_score']),
                           int(game_summary_df.loc[game_id, 'away_team_score'])
                       ))

    connection_to_database.commit()
    print (game_id + ' summary stats insertion to mysql table complete!')

def insert_game_drive_summary_data_to_mysql(game_drive_summary_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0,len(game_drive_summary_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        insert_SQL_query = "INSERT INTO `game_drives_summary_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    team_drive," \
                           "    quarter," \
                           "    time_left_on_clock," \
                           "    line_of_scrimmage," \
                           "    number_of_plays," \
                           "    length_of_drive," \
                           "    yards_gained_from_drive," \
                           "    result_of_drive" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                game_drive_summary_df.loc[i, 'home_team_name'],
                game_drive_summary_df.loc[i, 'away_team_name'],
                game_drive_summary_df.loc[i, 'week'],
                str(game_drive_summary_df.loc[i, 'date']),
                game_drive_summary_df.loc[i, 'team_drive'],
                int(game_drive_summary_df.loc[i, 'Quarter']),
                game_drive_summary_df.loc[i, 'Time'],
                game_drive_summary_df.loc[i, 'LOS'],
                int(game_drive_summary_df.loc[i, 'Plays']),
                game_drive_summary_df.loc[i, 'Length'],
                int(game_drive_summary_df.loc[i, 'Yds']),
                game_drive_summary_df.loc[i, 'Result']
            ))

    connection_to_database.commit()
    print (game_drive_summary_df.loc[0, 'home_team_name'] + ' vs ' + game_drive_summary_df.loc[0, 'away_team_name'] + ' drive summary stats insertion to mysql table complete!')


