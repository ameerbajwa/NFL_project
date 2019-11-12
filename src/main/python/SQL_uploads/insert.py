import pymysql
import pandas as pd

def insert_roster_info_to_mysql(team_roster_info):
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user='root',
                                password='%s',
                                host='127.0.0.1',
                                port=3306,
                                database='NFL_database'
                             ) % (connection_to_local_mysql_data_management_system.columns[1])

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
    print (team_name)
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user='root',
                                password='%s',
                                host='127.0.0.1',
                                port=3306,
                                database='NFL_database'
                             ) % (connection_to_local_mysql_data_management_system.columns[1])

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
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user='root',
                                password='%s',
                                host='127.0.0.1',
                                port=3306,
                                database='NFL_database'
                             ) % (connection_to_local_mysql_data_management_system.columns[1])


def insert_team_def_stats_to_mysql(team_def_stats_df):
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user='root',
                                password='%s',
                                host='127.0.0.1',
                                port=3306,
                                database='NFL_database'
                             ) % (connection_to_local_mysql_data_management_system.columns[1])



