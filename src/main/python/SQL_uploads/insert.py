import pymysql
import pandas as pd

connection_to_local_mysql_data_management_system = pd.read_csv('~/Desktop/connection_to_local_mysql_system.csv')

connection_to_database = pymysql.connect(
                            user=connection_to_local_mysql_data_management_system.columns[0],
                            password=connection_to_local_mysql_data_management_system.column[1],
                            host=connection_to_local_mysql_data_management_system.column[2],
                            port=connection_to_local_mysql_data_management_system.column[3],
                            database='NFL_roster_info_2019_2020_season'
                         )

