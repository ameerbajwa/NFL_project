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
    else:
        return 'NA'

def determining_type_of_pass(play_details):
    words = play_details.split(' ')

    if ('pass' in words):
        if ('complete' in words or 'incomplete' in words):
            return (words[4] + ' ' + words[5])
        else:
            return 'NA'
    else:
        return 'NA'

def determining_type_of_run(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words or 'punted' in words or 'kicks' in words or 'Penalty' in words):
        return 'NA'
    else:
        if ('up' in words):
            return (words[2] + ' ' + words[3] + ' ' + words[4])
        else:
            return (words[2] + ' ' + words[3])

def determining_result_of_play(play_details):
    words = play_details.split(' ')

    if ('pass' in words):
        return (words[2] + ' ' + words[3])
    elif ('sacked' in words):
        return (words[2])
    elif ('touchdown' in words):
        return (words[-1])


def determining_rusher(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words or 'punted' in words or 'kicks' in words or 'Penalty' in words):
        return 'NA'
    else:
        return (words[0] + ' ' + words[1])

def determining_receiver(play_details):
    words = play_details.split(' ')

    if (len(words) > 6):
        if ('pass' in words):
            if ('incomplete' in words and 'intended' in words and 'for' in words):
                return (words[8] + ' ' + words[9])
            elif ('complete' in words):
                return (words[7] + ' ' + words[8])
            else:
                return 'NA'
        else:
            return 'NA'
    else:
        return 'NA'

def cleaning_play_by_play_info(play_by_play_df):

    # type of play, type of pass, type of rush, result of play, type of penalty, penalty on, penalty accepted, penalty yards, yards gained, yards kicked, yards punted
    # qb, rb, receiver, tackler, defender, kicker, punter, returner, intercepted by, fumble recovery by, forced fumble by

    play_by_play_df['new_date'] = list(map(transforming_date, play_by_play_df['date']))
    play_by_play_df['type_of_play'] = list(map(determining_type_of_play, play_by_play_df['Detail']))
    play_by_play_df['type_of_pass'] = list(map(determining_type_of_pass, play_by_play_df['Detail']))
    play_by_play_df['type_of_rush'] = list(map(determining_type_of_run, play_by_play_df['Detail']))
    play_by_play_df['result_of_play'] = list(map(determining_result_of_play, play_by_play_df['Detail']))


    play_by_play_df['quarterback'] = list(map(determining_quarterback, play_by_play_df['Detail']))
    play_by_play_df['rusher'] = list(map(determining_rusher, play_by_play_df['Detail']))
    play_by_play_df['receiver'] = list(map(determining_receiver, play_by_play_df['Detail']))


    return play_by_play_df