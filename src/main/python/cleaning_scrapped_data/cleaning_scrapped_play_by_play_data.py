from time import strptime
from datetime import datetime
import pandas as pd

def transforming_date(date_of_game):
    pieces_of_date = date_of_game.replace(',', '').split(' ')
    month = strptime(pieces_of_date[1], '%b').tm_mon
    date = str(pieces_of_date[3]) + '-' + str(month) + '-' + str(pieces_of_date[2])
    return (pd.to_datetime(datetime.strptime(date, '%Y-%m-%d')))

def determining_type_of_play(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words):
        return ('pass play')
    elif ('punted' in words):
        return ('punt play')
    elif ('kicked' in words):
        if ('point' in words):
            return ('extra point play')
        elif ('off' in words):
            return ('kickoff play')
    else:
        return ('rush play')

def determining_quarterback(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words):
        return (words[0] + ' ' + words[1])

def determining_rusher(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words):
        pass
    elif ('punted' in words or 'kicks' in words):
        pass
    else:
        return (words[0] + ' ' + words[1])

def cleaning_play_by_play_info(play_by_play_df):

    play_by_play_df['new_date'] = list(map(transforming_date, play_by_play_df['date']))
    play_by_play_df['type_of_play'] = list(map(determining_type_of_play, play_by_play_df['Detail']))

    play_by_play_df['quarterback'] = list(map(determining_quarterback, play_by_play_df['Detail']))
    play_by_play_df['rusher'] = list(map(determining_rusher, play_by_play_df['Detail']))

    return play_by_play_df