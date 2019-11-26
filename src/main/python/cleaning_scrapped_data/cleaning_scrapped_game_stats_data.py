from datetime import datetime
from time import strptime
import pandas as pd

def transforming_date(df, game_id):
    pieces_of_date = df.loc[game_id, 'day_and_date_of_game'].replace(',', '').split(' ')
    day_of_week = pieces_of_date[0]
    year = pieces_of_date[3]
    month = strptime(pieces_of_date[1], '%b').tm_mon
    day = pieces_of_date[2]
    date = str(pieces_of_date[3]) + '-' + str(month) + '-' + str(pieces_of_date[2])

    return day_of_week, year, month, day, date
    # df['day_of_week'] = pieces_of_date[0]
    # df['year'] = pieces_of_date[3]
    # month = strptime(pieces_of_date[1], '%b').tm_mon
    # df['month'] = month
    # df['day'] = pieces_of_date[2]
    # date = str(pieces_of_date[3]) + '-' + str(month) + '-' + str(pieces_of_date[2])


def cleaning_game_summary_data(game_summary_df):

    game_id = game_summary_df.index[0]
    day_of_week, year, month, day, date = transforming_date(game_summary_df, game_id)
    # pieces_of_date = game_summary_df.loc[game_id, 'day_and_date_of_game'].replace(',', '').split(' ')
    # game_summary_df['day_of_week'] = pieces_of_date[0]
    # game_summary_df['year'] = pieces_of_date[3]
    # month = strptime(pieces_of_date[1], '%b').tm_mon
    # game_summary_df['month'] = month
    # game_summary_df['day'] = pieces_of_date[2]
    # date = str(pieces_of_date[3]) + '-' + str(month) + '-' + str(pieces_of_date[2])
    game_summary_df['day_of_week'] = day_of_week
    game_summary_df['year'] = year
    game_summary_df['month'] = month
    game_summary_df['day'] = day
    game_summary_df['date'] = pd.to_datetime(datetime.strptime(date, '%Y-%m-%d'))

    game_summary_df['hour'] = game_summary_df.loc[game_id, 'start_time_of_game'].split(': ')[1][:-2].split(':')[0]
    game_summary_df['minute'] = game_summary_df.loc[game_id, 'start_time_of_game'].split(': ')[1][:-2].split(':')[1]

    game_summary_df['time_of_game'] = (int(game_summary_df.loc[game_id, 'time_of_game'].split(': ')[1].split(':')[0])*60) + (int(game_summary_df.loc[game_id, 'time_of_game'].split(': ')[1].split(':')[1]))

    game_summary_df['stadium_name'] = game_summary_df.loc[game_id, 'stadium_name'].split(': ')[1]

    game_summary_df['attendance'] = game_summary_df.loc[game_id, 'attendance'].split(': ')[1].replace(',','')

    if ('won_toss' not in game_summary_df):
        game_summary_df['won_toss'] = 'NA'
    if ('roof' not in game_summary_df):
        game_summary_df['roof'] = 'NA'
    if ('surface' not in game_summary_df):
        game_summary_df['surface'] = 'NA'
    if ('weather' not in game_summary_df):
        game_summary_df['weather'] = 'NA'

    return game_summary_df

def cleaning_game_drive_summary(game_drive_summary_df):
    print (game_drive_summary_df.columns)
    print (game_drive_summary_df)

    day_of_week, year, month, day, date = transforming_date(game_drive_summary_df, 0)
    game_drive_summary_df = pd.to_datetime(datetime.strptime(date, '%Y-%m-%d'))

    return game_drive_summary_df