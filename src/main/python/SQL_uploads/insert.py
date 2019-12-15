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
    connection_to_database.close()
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
    connection_to_database.close()
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
    connection_to_database.close()
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
    connection_to_database.close()
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
    connection_to_database.close()
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
    connection_to_database.close()
    print (game_drive_summary_df.loc[0, 'home_team_name'] + ' vs ' + game_drive_summary_df.loc[0, 'away_team_name'] + ' drive summary stats insertion to mysql table complete!')

def insert_passing_stats_to_mysql(passing_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0,len(passing_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        insert_SQL_query = "INSERT INTO `NFL_player_passing_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    completed_passes," \
                           "    attempted_passes," \
                           "    yards_gained_by_passing," \
                           "    first_downs_through_passing," \
                           "    first_downs_through_passing_per_pass_play," \
                           "    intended_air_yards_on_all_pass_attempts," \
                           "    average_depth_of_target_per_pass_attempt," \
                           "    total_yards_passed_and_caught_traveling_through_the_air_past_LOS," \
                           "    completed_air_yards_per_pass_completion," \
                           "    completed_air_yards_per_pass_attempt," \
                           "    pass_yards_after_catch," \
                           "    pass_yards_after_catch_per_pass_completion," \
                           "    passes_dropped," \
                           "    passes_dropped_per_pass_attempt," \
                           "    poor_throws," \
                           "    poor_throws_per_pass_attempt," \
                           "    times_blitzed," \
                           "    times_hurried," \
                           "    times_hit," \
                           "    scrambles," \
                           "    yards_per_scrabble_attempt," \
                           "    passing_touchdowns," \
                           "    passing_interceptions," \
                           "    times_sacked," \
                           "    yards_lost_due_to_sacks," \
                           "    longest_completed_pass_thrown," \
                           "    QB_rating," \
                           "    number_of_times_fumbled," \
                           "    fumbles_lost" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                passing_stats_df.loc[i, 'player_first_name'],
                passing_stats_df.loc[i, 'player_last_name'],
                passing_stats_df.loc[i, 'Tm'],
                passing_stats_df.loc[i, 'opposing_team'],
                passing_stats_df.loc[i, 'home_team_name'],
                passing_stats_df.loc[i, 'away_team_name'],
                str(passing_stats_df.loc[i, 'week']),
                str(passing_stats_df.loc[i, 'new_date']),
                str(passing_stats_df.loc[i, 'Cmp']),
                str(passing_stats_df.loc[i, 'Att']),
                str(passing_stats_df.loc[i, 'Yds']),
                str(passing_stats_df.loc[i, '1D']),
                str(passing_stats_df.loc[i, '1D%']),
                str(passing_stats_df.loc[i, 'IAY']),
                str(passing_stats_df.loc[i, 'IAY/PA']),
                str(passing_stats_df.loc[i, 'CAY']),
                str(passing_stats_df.loc[i, 'CAY/Cmp']),
                str(passing_stats_df.loc[i, 'CAY/PA']),
                str(passing_stats_df.loc[i, 'YAC']),
                str(passing_stats_df.loc[i, 'YAC/Cmp']),
                str(passing_stats_df.loc[i, 'Drops']),
                str(passing_stats_df.loc[i, 'Drop%']),
                str(passing_stats_df.loc[i, 'BadTh']),
                str(passing_stats_df.loc[i, 'Bad%']),
                str(passing_stats_df.loc[i, 'Bltz']),
                str(passing_stats_df.loc[i, 'Hrry']),
                str(passing_stats_df.loc[i, 'Hits']),
                str(passing_stats_df.loc[i, 'Scrm']),
                str(passing_stats_df.loc[i, 'Yds/Scr']),
                str(passing_stats_df.loc[i, 'Passing_TD']),
                str(passing_stats_df.loc[i, 'Passing_Int']),
                str(passing_stats_df.loc[i, 'Sk']),
                str(passing_stats_df.loc[i, 'Passing_sacked_Yds']),
                str(passing_stats_df.loc[i, 'Passing_Lng']),
                str(passing_stats_df.loc[i, 'Passing_Rate']),
                str(passing_stats_df.loc[i, 'Fumbles_Fmb']),
                str(passing_stats_df.loc[i, 'Fumbles_FL'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (passing_stats_df.loc[0, 'home_team_name'] + ' vs ' + passing_stats_df.loc[0, 'away_team_name'] + ' game\'s passing stats insertion to mysql table complete!')

def insert_rushing_stats_to_mysql(rushing_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(rushing_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        insert_SQL_query = "INSERT INTO `NFL_player_rushing_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    rushing_attempts," \
                           "    rushing_yards_gained," \
                           "    first_downs_through_rushing," \
                           "    rushing_yards_before_contact," \
                           "    rushing_yards_before_contact_per_rushing_attempt," \
                           "    rushing_yards_after_contact," \
                           "    rushing_yards_after_contact_per_rushing_attempt," \
                           "    broken_tackles_on_rushes," \
                           "    rush_attempts_per_broken_tackle," \
                           "    rushing_touchdowns," \
                           "    longest_rushing_attempt," \
                           "    number_of_times_fumbled," \
                           "    fumbles_lost" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                rushing_stats_df.loc[i, 'player_first_name'],
                rushing_stats_df.loc[i, 'player_last_name'],
                rushing_stats_df.loc[i, 'Tm'],
                rushing_stats_df.loc[i, 'opposing_team'],
                rushing_stats_df.loc[i, 'home_team_name'],
                rushing_stats_df.loc[i, 'away_team_name'],
                str(rushing_stats_df.loc[i, 'week']),
                str(rushing_stats_df.loc[i, 'new_date']),
                str(rushing_stats_df.loc[i, 'Att']),
                str(rushing_stats_df.loc[i, 'Yds']),
                str(rushing_stats_df.loc[i, '1D']),
                str(rushing_stats_df.loc[i, 'YBC']),
                str(rushing_stats_df.loc[i, 'YBC/Att']),
                str(rushing_stats_df.loc[i, 'YAC']),
                str(rushing_stats_df.loc[i, 'YAC/Att']),
                str(rushing_stats_df.loc[i, 'BrkTkl']),
                str(rushing_stats_df.loc[i, 'Att/Br']),
                str(rushing_stats_df.loc[i, 'Rushing_TD']),
                str(rushing_stats_df.loc[i, 'Rushing_Lng']),
                str(rushing_stats_df.loc[i, 'Fumbles_Fmb']),
                str(rushing_stats_df.loc[i, 'Fumbles_FL'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (rushing_stats_df.loc[0, 'home_team_name'] + ' vs ' + rushing_stats_df.loc[0, 'away_team_name'] + ' game\'s rushing stats insertion to mysql table complete!')

def insert_receiving_stats_to_mysql(receiving_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(receiving_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        insert_SQL_query = "INSERT INTO `NFL_player_receiving_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    pass_targets," \
                           "    receptions," \
                           "    receiving_yards," \
                           "    first_downs_through_receiving," \
                           "    total_yards_passed_through_the_air_before_caught," \
                           "    yards_before_catch_per_reception," \
                           "    yards_after_catch," \
                           "    yards_after_catch_per_reception," \
                           "    broken_tackles_on_receptions," \
                           "    receptions_per_broken_tackle," \
                           "    dropped_passes," \
                           "    dropped_passes_per_target," \
                           "    receiving_touchdowns," \
                           "    longest_reception," \
                           "    number_of_times_fumbled," \
                           "    fumbles_lost" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                receiving_stats_df.loc[i, 'player_first_name'],
                receiving_stats_df.loc[i, 'player_last_name'],
                receiving_stats_df.loc[i, 'Tm'],
                receiving_stats_df.loc[i, 'opposing_team'],
                receiving_stats_df.loc[i, 'home_team_name'],
                receiving_stats_df.loc[i, 'away_team_name'],
                str(receiving_stats_df.loc[i, 'week']),
                str(receiving_stats_df.loc[i, 'new_date']),
                str(receiving_stats_df.loc[i, 'Tgt']),
                str(receiving_stats_df.loc[i, 'Rec']),
                str(receiving_stats_df.loc[i, 'Yds']),
                str(receiving_stats_df.loc[i, '1D']),
                str(receiving_stats_df.loc[i, 'YBC']),
                str(receiving_stats_df.loc[i, 'YBC/R']),
                str(receiving_stats_df.loc[i, 'YAC']),
                str(receiving_stats_df.loc[i, 'YAC/R']),
                str(receiving_stats_df.loc[i, 'BrkTkl']),
                str(receiving_stats_df.loc[i, 'Rec/Br']),
                str(receiving_stats_df.loc[i, 'Drop']),
                str(receiving_stats_df.loc[i, 'Drop%']),
                str(receiving_stats_df.loc[i, 'Receiving_TD']),
                str(receiving_stats_df.loc[i, 'Receiving_Lng']),
                str(receiving_stats_df.loc[i, 'Fumbles_Fmb']),
                str(receiving_stats_df.loc[i, 'Fumbles_FL'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (receiving_stats_df.loc[0, 'home_team_name'] + ' vs ' + receiving_stats_df.loc[0, 'away_team_name'] + ' game\'s receiving stats insertion to mysql table complete!')

def insert_defensive_stats_to_mysql(defensive_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(defensive_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        insert_SQL_query = "INSERT INTO `NFL_player_defensive_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    passes_intercepted," \
                           "    yards_returned_from_interceptions," \
                           "    interceptions_returned_for_touchdown," \
                           "    longest_interception_return," \
                           "    passes_deflected," \
                           "    times_targeted_by_a_pass," \
                           "    completed_passes_when_targeted," \
                           "    completion_percentage_allowed_when_targeted," \
                           "    receiving_yards_allowed_on_completion," \
                           "    receiving_yards_per_reception_allowed," \
                           "    receiving_yards_per_time_targeted," \
                           "    receiving_touchdowns_allowed," \
                           "    passer_rating_allowed_when_targeted," \
                           "    averaged_depth_of_receiver_when_targeted," \
                           "    total_air_yards_on_completions," \
                           "    yards_after_catch_on_completion," \
                           "    times_brought_on_for_blitz," \
                           "    QB_hurries," \
                           "    QB_knockdowns," \
                           "    sacks," \
                           "    QB_pressures," \
                           "    total_tackles," \
                           "    solo_tackles," \
                           "    assisted_tackles," \
                           "    tackles_for_loss," \
                           "    missed_tackles," \
                           "    missed_tackles_percentage," \
                           "    fumbles_recovered," \
                           "    yards_receovered_after_fumble," \
                           "    touchdowns_from_fumble_recovery," \
                           "    forced_fumbles" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                defensive_stats_df.loc[i, 'player_first_name'],
                defensive_stats_df.loc[i, 'player_last_name'],
                defensive_stats_df.loc[i, 'Tm'],
                defensive_stats_df.loc[i, 'opposing_team'],
                defensive_stats_df.loc[i, 'home_team_name'],
                defensive_stats_df.loc[i, 'away_team_name'],
                str(defensive_stats_df.loc[i, 'week']),
                str(defensive_stats_df.loc[i, 'new_date']),
                str(defensive_stats_df.loc[i, 'Int']),
                str(defensive_stats_df.loc[i, 'Def Interceptions_Yds']),
                str(defensive_stats_df.loc[i, 'Def Interceptions_TD']),
                str(defensive_stats_df.loc[i, 'Def Interceptions_Lng']),
                str(defensive_stats_df.loc[i, 'Def Interceptions_PD']),
                str(defensive_stats_df.loc[i, 'Tgt']),
                str(defensive_stats_df.loc[i, 'Cmp']),
                str(defensive_stats_df.loc[i, 'Cmp%']),
                str(defensive_stats_df.loc[i, 'Yds']),
                str(defensive_stats_df.loc[i, 'Yds/Cmp']),
                str(defensive_stats_df.loc[i, 'Yds/Tgt']),
                str(defensive_stats_df.loc[i, 'TD']),
                str(defensive_stats_df.loc[i, 'Rat']),
                str(defensive_stats_df.loc[i, 'DADOT']),
                str(defensive_stats_df.loc[i, 'Air']),
                str(defensive_stats_df.loc[i, 'YAC']),
                str(defensive_stats_df.loc[i, 'Bltz']),
                str(defensive_stats_df.loc[i, 'Hrry']),
                str(defensive_stats_df.loc[i, 'QBKD']),
                str(defensive_stats_df.loc[i, 'Sk']),
                str(defensive_stats_df.loc[i, 'Prss']),
                str(defensive_stats_df.loc[i, 'Comb']),
                str(defensive_stats_df.loc[i, 'Tackles_Solo']),
                str(defensive_stats_df.loc[i, 'Tackles_Ast']),
                str(defensive_stats_df.loc[i, 'Tackles_TFL']),
                str(defensive_stats_df.loc[i, 'MTkl']),
                str(defensive_stats_df.loc[i, 'MTkl%']),
                str(defensive_stats_df.loc[i, 'Fumbles_FR']),
                str(defensive_stats_df.loc[i, 'Fumbles_Yds']),
                str(defensive_stats_df.loc[i, 'Fumbles_TD']),
                str(defensive_stats_df.loc[i, 'Fumbles_FF'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (defensive_stats_df.loc[0, 'home_team_name'] + ' vs ' + defensive_stats_df.loc[0, 'away_team_name'] + ' game\'s defensive stats insertion to mysql table complete!')

def insert_return_stats_to_mysql(return_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(return_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        insert_SQL_query = "INSERT INTO `NFL_player_return_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    kickoff_returns," \
                           "    yards_after_kickoff_returns," \
                           "    yards_per_kickoff_returns," \
                           "    kickoff_return_touchdowns," \
                           "    longest_kickoff_return," \
                           "    punt_returns," \
                           "    yards_after_punt_returns," \
                           "    yards_per_punt_return," \
                           "    punt_return_touchdowns," \
                           "    longest_punt_return" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                return_stats_df.loc[i, 'player_first_name'],
                return_stats_df.loc[i, 'player_last_name'],
                return_stats_df.loc[i, 'Tm'],
                return_stats_df.loc[i, 'opposing_team'],
                return_stats_df.loc[i, 'home_team_name'],
                return_stats_df.loc[i, 'away_team_name'],
                str(return_stats_df.loc[i, 'week']),
                str(return_stats_df.loc[i, 'new_date']),
                str(return_stats_df.loc[i, 'Kick Returns_Rt']),
                str(return_stats_df.loc[i, 'Kick Returns_Yds']),
                str(return_stats_df.loc[i, 'Kick Returns_Y/Rt']),
                str(return_stats_df.loc[i, 'Kick Returns_TD']),
                str(return_stats_df.loc[i, 'Kick Returns_Lng']),
                str(return_stats_df.loc[i, 'Punt Returns_Ret']),
                str(return_stats_df.loc[i, 'Punt Returns_Yds']),
                str(return_stats_df.loc[i, 'Punt Returns_Y/R']),
                str(return_stats_df.loc[i, 'Punt Returns_TD']),
                str(return_stats_df.loc[i, 'Punt Returns_Lng'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (return_stats_df.loc[0, 'home_team_name'] + ' vs ' + return_stats_df.loc[0, 'away_team_name'] + ' game\'s return stats insertion to mysql table complete!')


def insert_kick_punt_stats_to_mysql(kick_punt_stats_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(kick_punt_stats_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        insert_SQL_query = "INSERT INTO `NFL_player_kicking_stats_per_game_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    player_first_name," \
                           "    player_last_name," \
                           "    team," \
                           "    opposing_team," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    extra_points_made," \
                           "    extra_points_attempted," \
                           "    field_goals_made," \
                           "    field_goals_attempted," \
                           "    times_punted," \
                           "    total_punt_yardage," \
                           "    yards_per_punt," \
                           "    longest_punt" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s);"

        with connection_to_database.cursor() as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                kick_punt_stats_df.loc[i, 'player_first_name'],
                kick_punt_stats_df.loc[i, 'player_last_name'],
                kick_punt_stats_df.loc[i, 'Tm'],
                kick_punt_stats_df.loc[i, 'opposing_team'],
                kick_punt_stats_df.loc[i, 'home_team_name'],
                kick_punt_stats_df.loc[i, 'away_team_name'],
                str(kick_punt_stats_df.loc[i, 'week']),
                str(kick_punt_stats_df.loc[i, 'new_date']),
                str(kick_punt_stats_df.loc[i, 'Scoring_XPM']),
                str(kick_punt_stats_df.loc[i, 'Scoring_XPA']),
                str(kick_punt_stats_df.loc[i, 'Scoring_FGM']),
                str(kick_punt_stats_df.loc[i, 'Scoring_FGA']),
                str(kick_punt_stats_df.loc[i, 'Punting_Pnt']),
                str(kick_punt_stats_df.loc[i, 'Punting_Yds']),
                str(kick_punt_stats_df.loc[i, 'Punting_Y/P']),
                str(kick_punt_stats_df.loc[i, 'Punting_Lng'])
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (kick_punt_stats_df.loc[0, 'home_team_name'] + ' vs ' + kick_punt_stats_df.loc[0, 'away_team_name'] + ' game\'s kicking and punting stats insertion to mysql table complete!')

def insert_play_by_play_stats_to_mysql(play_by_play_df):
    connection_to_database = connect_to_mysql_system()

    for i in range(0, len(play_by_play_df)):
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        insert_SQL_query = "INSERT INTO `play_by_play_info_2019_2020_season`" \
                           "(" \
                           "    id," \
                           "    home_team," \
                           "    away_team," \
                           "    week," \
                           "    date," \
                           "    quarter," \
                           "    time," \
                           "    down," \
                           "    yards_to_go," \
                           "    location_on_field," \
                           "    possession," \
                           "    type_of_play," \
                           "    type_of_pass," \
                           "    type_of_rush," \
                           "    result_of_play," \
                           "    type_of_penalty," \
                           "    penalty_on," \
                           "    penalty_accepted," \
                           "    penalty_yards," \
                           "    yards_gained," \
                           "    quarterback," \
                           "    rusher," \
                           "    receiver," \
                           "    sacker," \
                           "    sack_yards," \
                           "    tackler," \
                           "    defender," \
                           "    kicker," \
                           "    yards_kicked," \
                           "    punter," \
                           "    yards_punted," \
                           "    returner," \
                           "    yards_returned," \
                           "    intercepted_by," \
                           "    interception_location" \
                           "    interception_yards," \
                           "    fumbled_by," \
                           "    fumble_recovery_by," \
                           "    forced_fumble_by," \
                           "    fumble_recovery_location," \
                           "    fumble_yards," \
                           "    lateral_to," \
                           "    lateral_yards" \
                           "    home_team_score," \
                           "    away_team_score" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                           "          %s, %s, %s, %s, %s);"

        with connection_to_database.cursor as cursor:
            cursor.execute(insert_SQL_query, (
                random_id,
                play_by_play_df.loc[i, 'home_team_full_name'],
                play_by_play_df.loc[i, 'away_team_full_name'],
                play_by_play_df.loc[i, 'week'],
                play_by_play_df.loc[i, 'new_date'],
                play_by_play_df.loc[i, 'Quarter'],
                play_by_play_df.loc[i, 'Time'],
                play_by_play_df.loc[i, 'Down'],
                play_by_play_df.loc[i, 'ToGo'],
                play_by_play_df.loc[i, 'Location'],
                play_by_play_df.loc[i, 'possession'],
                play_by_play_df.loc[i, 'type_of_play'],
                play_by_play_df.loc[i, 'type_of_pass'],
                play_by_play_df.loc[i, 'type_of_rush'],
                play_by_play_df.loc[i, 'result_of_play'],
                play_by_play_df.loc[i, 'type_of_penalty'],
                play_by_play_df.loc[i, 'penalty_on'],
                play_by_play_df.loc[i, 'penalty_accepted'],
                play_by_play_df.loc[i, 'penalty_yards'],
                play_by_play_df.loc[i, 'yards_gained'],
                play_by_play_df.loc[i, 'quarterback'],
                play_by_play_df.loc[i, 'rusher'],
                play_by_play_df.loc[i, 'receiver'],
                play_by_play_df.loc[i, 'sacker'],
                play_by_play_df.loc[i, 'sack_yards'],
                play_by_play_df.loc[i, 'tackler'],
                play_by_play_df.loc[i, 'defender'],
                play_by_play_df.loc[i, 'kicker'],
                play_by_play_df.loc[i, 'yards_kicked'],
                play_by_play_df.loc[i, 'punter'],
                play_by_play_df.loc[i, 'yards_punted'],
                play_by_play_df.loc[i, 'returner'],
                play_by_play_df.loc[i, 'yards_returned'],
                play_by_play_df.loc[i, 'intercepted_by'],
                play_by_play_df.loc[i, 'interception_location'],
                play_by_play_df.loc[i, 'interception_yards'],
                play_by_play_df.loc[i, 'fumbled_by'],
                play_by_play_df.loc[i, 'fumble_recovered_by'],
                play_by_play_df.loc[i, 'fumble_forced_by'],
                play_by_play_df.loc[i, 'fumble_recovery_location'],
                play_by_play_df.loc[i, 'fumble_yards'],
                play_by_play_df.loc[i, 'lateral_to'],
                play_by_play_df.loc[i, 'lateral_yards'],
                play_by_play_df.loc[i, 'home_team_score'],
                play_by_play_df.loc[i, 'away_team_score']
            ))

    connection_to_database.commit()
    connection_to_database.close()
    print (play_by_play_df.loc[0, 'home_team_full_name'] + ' vs ' + play_by_play_df.loc[0, 'away_team_full_name'] + ' play by play stats insertion to mysql table complete!')


