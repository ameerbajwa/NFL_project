import pymysql
import pandas as pd

def insert_roster_info_to_mysql(): # team_roster_info
    connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

    connection_to_database = pymysql.connect(
                                user=connection_to_local_mysql_data_management_system.columns[0],
                                password=connection_to_local_mysql_data_management_system.columns[1],
                                host=connection_to_local_mysql_data_management_system.columns[2],
                                port=connection_to_local_mysql_data_management_system.columns[3],
                                database='NFL_database'
                             )

    insert_SQL_query = "SELECT * FROM NFL_roster_info_2019_2020_season"
    table = pd.read_sql(insert_SQL_query, connection_to_database)
    print (table)

insert_roster_info_to_mysql()

    # for i in range(0, len(team_roster_info)):
    #     insert_SQL_query = "INSERT INTO `NFL_roster_info_2019_2020_season` " \
    #                        "(" \
    #                        "    player_number," \
    #                        "    player_name," \
    #                        "    team," \
    #                        "    age," \
    #                        "    position," \
    #                        "    games_played," \
    #                        "    games_started," \
    #                        "    weight," \
    #                        "    height," \
    #                        "    college," \
    #                        "    birthdate," \
    #                        "    experience," \
    #                        "    drafted," \
    #                        "    salary" \
    #                        ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    #
    #     with connection_to_database.cursor() as cursor:
    #         cursor.execute(insert_SQL_query,
    #                         (
    #                            team_roster_info.loc[i, 'No.'],
    #                            team_roster_info.loc[i, 'Player '],
    #                            team_roster_info.loc[i, 'Team'],
    #                            team_roster_info.loc[i, 'Age'],
    #                            team_roster_info.loc[i, 'Pos'],
    #                            team_roster_info.loc[i, 'G'],
    #                            team_roster_info.loc[i, 'GS'],
    #                            team_roster_info.loc[i, 'Wt'],
    #                            team_roster_info.loc[i, 'Ht'],
    #                            team_roster_info.loc[i, 'College/Univ'],
    #                            team_roster_info.loc[i, 'BirthDate'],
    #                            team_roster_info.loc[i, 'Yrs'],
    #                            team_roster_info.loc[i, 'Drafted (tm/rnd/yr)'],
    #                            team_roster_info.loc[i, 'Salary']
    #                         )
    #                       )
    #
    #     connection_to_database.commit()
    #     print(team_roster_info.loc[0, 'Team'] + 'roster insertion complete!')


