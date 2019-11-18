import pymysql
import pandas as pd

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
    # connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')
    #
    # connection_to_database = pymysql.connect(
    #                             user='root',
    #                             password='%s',
    #                             host='127.0.0.1',
    #                             port=3306,
    #                             database='NFL_database'
    #                          ) % (connection_to_local_mysql_data_management_system.columns[1])

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

    # connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')
    #
    # connection_to_database = pymysql.connect(
    #                             user='root',
    #                             password='%s',
    #                             host='127.0.0.1',
    #                             port=3306,
    #                             database='NFL_database'
    #                          ) % (connection_to_local_mysql_data_management_system.columns[1])
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
                        "average_staring_field_position_by_team," \
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
            str(team_off_stats_df.iloc[0,0]),
            str(team_off_stats_df.iloc[0,1]),
            str(team_off_stats_df.iloc[0,2]),
            str(team_off_stats_df.iloc[0,3]),
            str(team_off_stats_df.iloc[0,4]),
            str(team_off_stats_df.iloc[0,5]),
            str(team_off_stats_df.iloc[0,6]),
            str(team_off_stats_df.iloc[0,7]),
            str(team_off_stats_df.iloc[0,8]),
            str(team_off_stats_df.iloc[0,9]),
            str(team_off_stats_df.iloc[0,10]),
            str(team_off_stats_df.iloc[0,11]),
            str(team_off_stats_df.iloc[0,12]),
            str(team_off_stats_df.iloc[0,13]),
            str(team_off_stats_df.iloc[0,14]),
            str(team_off_stats_df.iloc[0,15]),
            str(team_off_stats_df.iloc[0,16]),
            str(team_off_stats_df.iloc[0,17]),
            str(team_off_stats_df.iloc[0,18]),
            str(team_off_stats_df.iloc[0,19]),
            str(team_off_stats_df.iloc[0,20]),
            str(team_off_stats_df.iloc[0,21]),
            str(team_off_stats_df.iloc[0,22]),
            str(team_off_stats_df.iloc[0,23]),
            str(team_off_stats_df.iloc[0,24]),
            str(team_off_stats_df.iloc[0,25]),
            str(team_off_stats_df.iloc[0,26]),
            str(team_off_stats_df.iloc[0,27]),
            str(team_off_stats_df.iloc[0,28]),
            str(team_off_stats_df.iloc[0,29]),
            str(team_off_stats_df.iloc[0,30]),
            str(team_off_stats_df.iloc[0,31]),
            str(team_off_stats_df.iloc[0,32]),
            str(team_off_stats_df.iloc[0,33]),
            str(team_off_stats_df.iloc[0,34]),
            str(team_off_stats_df.iloc[0,35]),
            str(team_off_stats_df.iloc[0,36]),
            str(team_off_stats_df.iloc[0,37]),
            str(team_off_stats_df.iloc[0,38])
        ))

    connection_to_database.commit()
    print (team_off_stats_df.index[0] + ' offensive team stats insertion to mysql table complete!')

def insert_team_def_stats_to_mysql(team_def_stats_df):
    connection_to_database = connect_to_mysql_system()

    # connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')
    #
    # connection_to_database = pymysql.connect(
    #                             user='root',
    #                             password='%s',
    #                             host='127.0.0.1',
    #                             port=3306,
    #                             database='NFL_database'
    #                          ) % (connection_to_local_mysql_data_management_system.columns[1])
    
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
                                "rushing_toudowns_by_opposing_teams," \
                                "rushing_yards_per_attempt_by_opposing_teams," \
                                "first_downs_through_rushing_by_opposing_teams," \
                                "penalties_committed_by_team_and_accepted_by_opposing_teams," \
                                "penalty_yards_accured_from_team," \
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
            str(team_def_stats_df.iloc[0,0]),
            str(team_def_stats_df.iloc[0,1]),
            str(team_def_stats_df.iloc[0,2]),
            str(team_def_stats_df.iloc[0,3]),
            str(team_def_stats_df.iloc[0,4]),
            str(team_def_stats_df.iloc[0,5]),
            str(team_def_stats_df.iloc[0,6]),
            str(team_def_stats_df.iloc[0,7]),
            str(team_def_stats_df.iloc[0,8]),
            str(team_def_stats_df.iloc[0,9]),
            str(team_def_stats_df.iloc[0,10]),
            str(team_def_stats_df.iloc[0,11]),
            str(team_def_stats_df.iloc[0,12]),
            str(team_def_stats_df.iloc[0,13]),
            str(team_def_stats_df.iloc[0,14]),
            str(team_def_stats_df.iloc[0,15]),
            str(team_def_stats_df.iloc[0,16]),
            str(team_def_stats_df.iloc[0,17]),
            str(team_def_stats_df.iloc[0,18]),
            str(team_def_stats_df.iloc[0,19]),
            str(team_def_stats_df.iloc[0,20]),
            str(team_def_stats_df.iloc[0,21]),
            str(team_def_stats_df.iloc[0,22]),
            str(team_def_stats_df.iloc[0,23]),
            str(team_def_stats_df.iloc[0,24]),
            str(team_def_stats_df.iloc[0,25]),
            str(team_def_stats_df.iloc[0,26]),
            str(team_def_stats_df.iloc[0,27]),
            str(team_def_stats_df.iloc[0,28]),
            str(team_def_stats_df.iloc[0,29]),
            str(team_def_stats_df.iloc[0,30]),
            str(team_def_stats_df.iloc[0,31]),
            str(team_def_stats_df.iloc[0,32]),
            str(team_def_stats_df.iloc[0,33]),
            str(team_def_stats_df.iloc[0,34]),
            str(team_def_stats_df.iloc[0,35]),
            str(team_def_stats_df.iloc[0,36]),
            str(team_def_stats_df.iloc[0,37]),
            str(team_def_stats_df.iloc[0,38])
        ))

    connection_to_database.commit()
    print (team_def_stats_df.index[0] + ' defensive team stats insertion to mysql table complete!')

