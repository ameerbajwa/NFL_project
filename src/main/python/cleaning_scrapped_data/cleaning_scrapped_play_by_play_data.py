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
    elif ('field' in words and 'goal' in words):
        return ('field goal play')
    elif ('Timeout' in words):
        return 'NA'
    else:
        return ('rush play')

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

    if ('pass' in words or 'sacked' in words or 'punted' in words or 'kicks' in words or 'Penalty' in words or 'field' in words or 'Timeout' in words):
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

def determining_type_of_penalty(play_details):
    words = play_details.split(' ')

    if ('Penalty' in words):
        if ('False' in words and 'Start' in words):
            return ' '.join(play_details.split(':')[1].split(',')[0].split(' ')[1:])
        else:
            return ' '.join(play_details.split('.')[1].split(':')[1].split(',')[0].split(' ')[1:])
    else:
        return 'NA'

def determining_penalty_on_whom(play_details):
    words = play_details.split(' ')

    if ('Penalty' in words):
        if ('False' in words and 'Start' in words):
            return ' '.join(play_details.split(':')[0].split(' ')[2:])
        else:
            return ' '.join(play_details.spilt('.')[1].split(':')[0].split(' ')[3:])
    else:
        return 'NA'

def determining_penalty_accepted(play_details):
    words = play_details.split(' ')

    if ('Penalty' in words):
        if ('(Declined)' in words):
            return 'Declined'
        else:
            return 'Accepted'
    else:
        return 'NA'

def determining_penalty_yards(play_details):
    words = play_details.split(' ')

    if ('Penalty' in words):
        return (play_details.split(',')[1].split(' ')[1])
    else:
        return 'NA'

def determining_yards_gained(play_details):
    words = play_details.split(' ')

    if ('for' in words):
        if ('no' in words and 'gain' in words):
            return '0'
        elif ('incomplete' in words):
            return 'NA'
        else:
            return (words[words.index('for') + 1])
    else:
        return 'NA'

def determining_yards_kicked(play_details):
    words = play_details.split(' ')

    if ('kicks' in words and 'off' in words):
        return (words[4])
    elif ('field' in words and 'goal' in words):
        return (words[2])
    else:
        return 'NA'

def determining_yards_punted(play_details):
    words = play_details.split(' ')

    if ('punts' in words):
        return (words[3])
    else:
        return 'NA'

def determining_yards_returned(play_details):
    words = play_details.split(' ')

    if ('punts' in words or ('kicks' in words and 'off' in words)):
        if ('returned' in words):
            return (words[words.index('for') + 1])
        else:
            return '0'
    else:
        return 'NA'

def determining_quarterback(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words):
        return (words[0] + ' ' + words[1])
    else:
        return 'NA'

def determining_rusher(play_details):
    words = play_details.split(' ')

    if ('pass' in words or 'sacked' in words or 'punted' in words or 'kicks' in words or 'Penalty' in words or 'Timeout' in words):
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

def determining_tackler(play_details):
    words = play_details.split(' ')

    if ('(tackle' in words):
        if ('and' in words):
            return (words[words.index('by') + 1] + ' ' + words[words.index('by') + 2] + ' and ' + words[words.index('by') + 4] + ' ' + words[words.index('by') + 5])
        else:
            return (words[words.index('by') + 1] + ' ' + words[words.index('by') + 2])
    else:
        'NA'

def determining_defender(play_details):
    words = play_details.split(' ')

    if ('(defended' in words):
        return (words[words.index('by') + 1] + ' ' + words[words.index('by') + 2])
    else:
        return 'NA'

def determining_intercepted_by(play_details):
    words = play_details.split(' ')

    if ('intercepted' in words):
        return (words[words.index('intercepted') + 2] + ' ' + words[words.index('intercepted') + 3])
    else:
        return 'NA'

def determining_kicker(play_details):
    words = play_details.split(' ')

    if ('kicks' in words or ('field' in words and 'goal' in words)):
        return (words[0] + ' ' + words[1])
    else:
        return 'NA'

def determining_punter(play_details):
    words = play_details.split(' ')

    if ('punts' in words):
        return (words[0] + ' ' + words[1])

def determining_returner(play_details):
    words = play_details.split(' ')

    if ('punts' in words or ('kicks' in words and 'off' in words)):
        if ('returned' in words or ('fair' in words and 'catch' in words)):
            return (words[words.index('by') + 1] + ' ' + words[words.index('by') + 2])
        else:
            return 'NA'
    else:
        return 'NA'

def cleaning_play_by_play_info(play_by_play_df):

    # type of play, type of pass, type of rush, result of play, type of penalty, penalty on, penalty accepted, penalty yards, yards gained, yards kicked, yards punted, yards_returned
    # qb, rb, receiver, tackler, defender, kicker, punter, returner, intercepted by, fumble recovery by, forced fumble by

    play_by_play_df['new_date'] = list(map(transforming_date, play_by_play_df['date']))
    play_by_play_df['type_of_play'] = list(map(determining_type_of_play, play_by_play_df['Detail']))
    play_by_play_df['type_of_pass'] = list(map(determining_type_of_pass, play_by_play_df['Detail']))
    play_by_play_df['type_of_rush'] = list(map(determining_type_of_run, play_by_play_df['Detail']))
    play_by_play_df['result_of_play'] = list(map(determining_result_of_play, play_by_play_df['Detail']))

    play_by_play_df['type_of_penalty'] = list(map(determining_type_of_penalty, play_by_play_df['Detail']))
    play_by_play_df['penalty_on'] = list(map(determining_penalty_on_whom, play_by_play_df['Detail']))
    play_by_play_df['penalty_accepted'] = list(map(determining_penalty_accepted, play_by_play_df['Detail']))
    play_by_play_df['penalty_yards'] = list(map(determining_penalty_yards, play_by_play_df['Detail']))

    play_by_play_df['yards_gained'] = list(map(determining_yards_gained, play_by_play_df['Detail']))
    play_by_play_df['yards_kicked'] = list(map(determining_yards_kicked, play_by_play_df['Detail']))
    play_by_play_df['yards_punted'] = list(map(determining_yards_punted, play_by_play_df['Detail']))
    play_by_play_df['yards_returned'] = list(map(determining_yards_returned, play_by_play_df['Detail']))

    play_by_play_df['quarterback'] = list(map(determining_quarterback, play_by_play_df['Detail']))
    play_by_play_df['rusher'] = list(map(determining_rusher, play_by_play_df['Detail']))
    play_by_play_df['receiver'] = list(map(determining_receiver, play_by_play_df['Detail']))
    play_by_play_df['tackler'] = list(map(determining_tackler, play_by_play_df['Detail']))
    play_by_play_df['defender'] = list(map(determining_defender, play_by_play_df['Detail']))
    play_by_play_df['intercepted_by'] = list(map(determining_intercepted_by, play_by_play_df['Detail']))

    play_by_play_df['kicker'] = list(map(determining_kicker), play_by_play_df['Detail'])
    play_by_play_df['punter'] = list(map(determining_punter, play_by_play_df['Detail']))
    play_by_play_df['returner'] = list(map(determining_returner, play_by_play_df['Detail']))

    return play_by_play_df

penalty_words = determining_type_of_penalty()
print (penalty_words)