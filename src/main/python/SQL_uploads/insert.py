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
                passing_stats_df.loc[i, 'week'],
                passing_stats_df.loc[i, 'date'],
                passing_stats_df.loc[i, 'Cmp'],
                passing_stats_df.loc[i, 'Att'],
                passing_stats_df.loc[i, 'Yds'],
                passing_stats_df.loc[i, '1D'],
                passing_stats_df.loc[i, '1D%'],
                passing_stats_df.loc[i, 'IAY'],
                passing_stats_df.loc[i, 'IAY/PA'],
                passing_stats_df.loc[i, 'CAY'],
                passing_stats_df.loc[i, 'CAY/Cmp'],
                passing_stats_df.loc[i, 'CAY/PA'],
                passing_stats_df.loc[i, 'YAC'],
                passing_stats_df.loc[i, 'YAC/Cmp'],
                passing_stats_df.loc[i, 'Drops'],
                passing_stats_df.loc[i, 'Drops%'],
                passing_stats_df.loc[i, 'BadTh'],
                passing_stats_df.loc[i, 'Bad%'],
                passing_stats_df.loc[i, 'Bltz'],
                passing_stats_df.loc[i, 'Hrry'],
                passing_stats_df.loc[i, 'Hits'],
                passing_stats_df.loc[i, 'Scrm'],
                passing_stats_df.loc[i, 'Yds/Scr'],
                passing_stats_df.loc[i, 'Passing_TD'],
                passing_stats_df.loc[i, 'Passing_Int'],
                passing_stats_df.loc[i, 'Passing_Sk'],
                passing_stats_df.loc[i, 'Passing_Yds'],
                passing_stats_df.loc[i, 'Passing_Lng'],
                passing_stats_df.loc[i, 'Passing_Rate'],
                passing_stats_df.loc[i, 'Fumbles_Fmb'],
                passing_stats_df.loc[i, 'Fumbles_FL'],
            ))

    connection_to_database.commit()
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
                           "    rushing_attempts_per_broken_tackle," \
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
                rushing_stats_df.loc[i, 'week'],
                rushing_stats_df.loc[i, 'date'],
                rushing_stats_df.loc[i, 'player_first_name'],
                rushing_stats_df.loc[i, 'Att'],
                rushing_stats_df.loc[i, 'Yds'],
                rushing_stats_df.loc[i, '1D'],
                rushing_stats_df.loc[i, 'YBC'],
                rushing_stats_df.loc[i, 'YBC/Att'],
                rushing_stats_df.loc[i, 'YAC'],
                rushing_stats_df.loc[i, 'YAC/Att'],
                rushing_stats_df.loc[i, 'BrkTkl'],
                rushing_stats_df.loc[i, 'Att/Br'],
                rushing_stats_df.loc[i, 'Rushing_TD'],
                rushing_stats_df.loc[i, 'Rushing_Lng'],
                rushing_stats_df.loc[i, 'Fumbles_Fmb'],
                rushing_stats_df.loc[i, 'Fumbles_FL']
            ))

    connection_to_database.commit()
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
                           "    total_yards_passed_through_air_before_caught," \
                           "    yards_before_catch_per_reception," \
                           "    yards_after_catch," \
                           "    yards_after_catch_per_reception," \
                           "    broken_tackles_on_recptions," \
                           "    receptions_per_broken_tackle," \
                           "    dropped_passes," \
                           "    dropped_passes_per_target," \
                           "    receiving_touchdowns," \
                           "    longest_reception," \
                           "    number_of_times_fumbled," \
                           "    fumbles_lost" \
                           ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                           "          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
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
                receiving_stats_df.loc[i, 'week'],
                receiving_stats_df.loc[i, 'date'],
                receiving_stats_df.loc[i, 'Tgt'],
                receiving_stats_df.loc[i, 'Rec'],
                receiving_stats_df.loc[i, 'Yds'],
                receiving_stats_df.loc[i, '1D'],
                receiving_stats_df.loc[i, 'YBC'],
                receiving_stats_df.loc[i, 'YBC/R'],
                receiving_stats_df.loc[i, 'YAC'],
                receiving_stats_df.loc[i, 'YAC/R'],
                receiving_stats_df.loc[i, 'BrkTkl'],
                receiving_stats_df.loc[i, 'Rec/Br'],
                receiving_stats_df.loc[i, 'Drop'],
                receiving_stats_df.loc[i, 'Drop%'],
                receiving_stats_df.loc[i, 'Receiving_TD'],
                receiving_stats_df.loc[i, 'Receiving_Lng'],
                receiving_stats_df.loc[i, 'Fumbles_Fmb'],
                receiving_stats_df.loc[i, 'Fumbles_FL']
            ))

    connection_to_database.commit()
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
                defensive_stats_df.loc[i, 'week'],
                defensive_stats_df.loc[i, 'date'],
                defensive_stats_df.loc[i, 'Int'],
                defensive_stats_df.loc[i, 'Def Interceptions_Yds'],
                defensive_stats_df.loc[i, 'Def Interceptions_TD'],
                defensive_stats_df.loc[i, 'Def Interceptions_Lng'],
                defensive_stats_df.loc[i, 'Def Interceptions_PD'],
                defensive_stats_df.loc[i, 'Tgt'],
                defensive_stats_df.loc[i, 'Cmp'],
                defensive_stats_df.loc[i, 'Cmp%'],
                defensive_stats_df.loc[i, 'Yds'],
                defensive_stats_df.loc[i, 'Yds/Cmp'],
                defensive_stats_df.loc[i, 'Yds/Tgt'],
                defensive_stats_df.loc[i, 'TD'],
                defensive_stats_df.loc[i, 'Rat'],
                defensive_stats_df.loc[i, 'DADOT'],
                defensive_stats_df.loc[i, 'Air'],
                defensive_stats_df.loc[i, 'YAC'],
                defensive_stats_df.loc[i, 'Bltz'],
                defensive_stats_df.loc[i, 'Hrry'],
                defensive_stats_df.loc[i, 'QBKD'],
                defensive_stats_df.loc[i, 'Sk'],
                defensive_stats_df.loc[i, 'Prss'],
                defensive_stats_df.loc[i, 'Comb'],
                defensive_stats_df.loc[i, 'Tackles_Solo'],
                defensive_stats_df.loc[i, 'Tackles_Ast'],
                defensive_stats_df.loc[i, 'Tackles_TFL'],
                defensive_stats_df.loc[i, 'MTkl'],
                defensive_stats_df.loc[i, 'MTkl%'],
                defensive_stats_df.loc[i, 'Fumbles_FR'],
                defensive_stats_df.loc[i, 'Fumbles_Yds'],
                defensive_stats_df.loc[i, 'Fumbles_TD'],
                defensive_stats_df.loc[i, 'Fumbles_FF']
            ))

    connection_to_database.commit()
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
                           "    punt_return," \
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
                return_stats_df.loc[i, 'week'],
                return_stats_df.loc[i, 'date'],
                return_stats_df.loc[i, 'Kick Returns_Rt'],
                return_stats_df.loc[i, 'Kick Returns_Yds'],
                return_stats_df.loc[i, 'Kick Returns_Y/Rt'],
                return_stats_df.loc[i, 'Kick Returns_TD'],
                return_stats_df.loc[i, 'Kick Returns_Lng'],
                return_stats_df.loc[i, 'Punt Returns_Rt'],
                return_stats_df.loc[i, 'Punt Returns_Yds'],
                return_stats_df.loc[i, 'Punt Returns_Y/R'],
                return_stats_df.loc[i, 'Punt Returns_TD'],
                return_stats_df.loc[i, 'Punt Returns_Lng']
            ))

    connection_to_database.commit()
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
                           "    home_team" \
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
                kick_punt_stats_df.loc[i, 'week'],
                kick_punt_stats_df.loc[i, 'date'],
                kick_punt_stats_df.loc[i, 'Scoring_XPM'],
                kick_punt_stats_df.loc[i, 'Scoring_XPA'],
                kick_punt_stats_df.loc[i, 'Scoring_FGM'],
                kick_punt_stats_df.loc[i, 'Scoring_FGA'],
                kick_punt_stats_df.loc[i, 'Punting_Pnt'],
                kick_punt_stats_df.loc[i, 'Punting_Yds'],
                kick_punt_stats_df.loc[i, 'Punting_Y/P'],
                kick_punt_stats_df.loc[i, 'Punting_Lng']
            ))

    connection_to_database.commit()
    print (kick_punt_stats_df.loc[0, 'home_team_name'] + ' vs ' + kick_punt_stats_df.loc[0, 'away_team_name'] + ' game\'s kicking and punting stats insertion to mysql table complete!')

