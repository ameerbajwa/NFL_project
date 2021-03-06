from time import strptime
from datetime import datetime
import pandas as pd

def converting_to_int(x):

    if (x == ''):
        return 0
    else:
        return int(x)

def converting_to_float(x):

    if (x == ''):
        return 0.0
    else:
        return float(x)

def defining_opposing_team_and_splitting_player_name(list_of_player_stats_df, list_of_teams):
    new_list_of_player_stats_df = []

    for df in list_of_player_stats_df:
        df['player_first_name'] = list(map(lambda x: ' '.join(x.split(' ')[:-1]) if len(x.split(' ')) > 1 else x.split(' ')[0], df['Player']))
        df['player_last_name'] = list(map(lambda x: x.split(' ')[-1], df['Player']))
        teams = df['Tm'].unique()
        if (len(teams) == 1):
            df['opposing_team'] = list(map(lambda x: list_of_teams[0] if x == list_of_teams[1] else list_of_teams[1], df['Tm']))
        else:
            df['opposing_team'] = list(map(lambda x: teams[0] if x == teams[1] else teams[1], df['Tm']))

        new_list_of_player_stats_df.append(df)

    return (new_list_of_player_stats_df, teams)

def transforming_date(date_of_game):
    pieces_of_date = date_of_game.replace(',', '').split(' ')
    month = strptime(pieces_of_date[1], '%b').tm_mon
    date = str(pieces_of_date[3]) + '-' + str(month) + '-' + str(pieces_of_date[2])
    return (pd.to_datetime(datetime.strptime(date, '%Y-%m-%d')))

def convert_values_to_appropriate_types(list_of_player_stats_df):
    new_list_of_player_stats_df = []
    list_of_columns_set = ['date', 'week', 'home_team_name', 'away_team_name', 'new_date', 'player_first_name', 'player_last_name', 'opposing_team', 'Player', 'Tm']

    for df in list_of_player_stats_df:
        for col in df.columns:
            if (col in list_of_columns_set):
                continue
            else:
                if ('%' in col):
                    df[col] = list(map(lambda x: x.replace('%', '') if '%' in x else x, df[col]))
                    df[col] = list(map(converting_to_float, df[col]))
                elif ('/' in col or col == 'Passing_Rate' or col == 'Rat' or col == 'DADOT' or col == 'Sk'):
                    df[col] = list(map(converting_to_float, df[col]))
                else:
                    df[col] = list(map(converting_to_int, df[col]))

        new_list_of_player_stats_df.append(df)

    return (new_list_of_player_stats_df)

def defining_new_columns(list_of_new_column_names, cleaner_adv_off_player_stats_df):

    for col in list_of_new_column_names:
        cleaner_adv_off_player_stats_df[col] = 0

    return (cleaner_adv_off_player_stats_df)

def joining_basic_stats_and_adv_stats(basic_player_stats_df, adv_player_stats_df, list_of_new_column_names):

    counter = 0
    for row_index in range(0, len(basic_player_stats_df)):
        if (counter < len(adv_player_stats_df)):
            if (basic_player_stats_df.loc[row_index, 'Player'] == adv_player_stats_df.loc[counter, 'Player']):
                for col in list_of_new_column_names:
                    adv_player_stats_df.loc[counter, col] = basic_player_stats_df.loc[row_index, col]
                counter += 1
        else:
            continue

    return (adv_player_stats_df)

def cleaning_offensive_player_stats(basic_off_player_stats_df, adv_off_player_stats_df, type_of_offense):

    list_of_player_dfs = [basic_off_player_stats_df, adv_off_player_stats_df]
    tms = [1,2]
    new_list_of_player_dfs, teams = defining_opposing_team_and_splitting_player_name(list_of_player_dfs, tms)

    for df in new_list_of_player_dfs:
        df['new_date'] = list(map(transforming_date, df['date']))

    cleaner_list_of_player_dfs = convert_values_to_appropriate_types(new_list_of_player_dfs)
    cleaner_basic_off_player_stats_df = cleaner_list_of_player_dfs[0]
    cleaner_adv_off_player_stats_df = cleaner_list_of_player_dfs[1]

    if (type_of_offense == 'passing'):

        cleaner_basic_off_player_stats_df.sort_values(by=['Tm', 'Passing_Yds', 'Player'], ascending=[False, True, False], inplace=True)
        cleaner_adv_off_player_stats_df.sort_values(by=['Tm', 'Yds', 'Player'], ascending=[False, True, False], inplace=True)

        list_of_new_column_names = ['Passing_TD', 'Passing_Int', 'Passing_sacked_Yds', 'Passing_Lng', 'Passing_Rate', 'Fumbles_Fmb', 'Fumbles_FL']

        new_adv_off_player_stats_df = defining_new_columns(list_of_new_column_names, cleaner_adv_off_player_stats_df)

        passing_stats_df = joining_basic_stats_and_adv_stats(cleaner_basic_off_player_stats_df, new_adv_off_player_stats_df, list_of_new_column_names)

        return (passing_stats_df)

    elif (type_of_offense == 'rushing'):

        cleaner_basic_off_player_stats_df.sort_values(['Tm', 'Rushing_Att', 'Player'], ascending=[False, True, False], inplace=True)
        cleaner_adv_off_player_stats_df.sort_values(['Tm', 'Att', 'Player'], ascending=[False, True, False], inplace=True)

        list_of_new_column_names = ['Rushing_TD', 'Rushing_Lng', 'Fumbles_Fmb', 'Fumbles_FL']

        new_adv_off_player_stats_df = defining_new_columns(list_of_new_column_names, cleaner_adv_off_player_stats_df)

        rushing_stats_df = joining_basic_stats_and_adv_stats(cleaner_basic_off_player_stats_df, new_adv_off_player_stats_df, list_of_new_column_names)

        return (rushing_stats_df)

    elif (type_of_offense == 'receiving'):

        cleaner_basic_off_player_stats_df.sort_values(['Tm', 'Receiving_Tgt', 'Player'], ascending=[False, True, False], inplace=True)
        cleaner_adv_off_player_stats_df.sort_values(['Tm', 'Tgt', 'Player'], ascending=[False, True, False], inplace=True)

        list_of_new_column_names = ['Receiving_TD', 'Receiving_Lng', 'Fumbles_Fmb', 'Fumbles_FL']

        new_adv_off_player_stats_df = defining_new_columns(list_of_new_column_names, cleaner_adv_off_player_stats_df)

        receiving_stats_df = joining_basic_stats_and_adv_stats(cleaner_basic_off_player_stats_df, new_adv_off_player_stats_df, list_of_new_column_names)

        return (receiving_stats_df)

def cleaning_defensive_player_stats(basic_def_player_stats_df, adv_def_player_stats_df):

    list_of_player_dfs = [basic_def_player_stats_df, adv_def_player_stats_df]
    tms = [1,2]
    new_list_of_player_dfs, teams = defining_opposing_team_and_splitting_player_name(list_of_player_dfs, tms)

    for df in new_list_of_player_dfs:
        df['new_date'] = list(map(transforming_date, df['date']))

    cleaner_list_of_player_dfs = convert_values_to_appropriate_types(new_list_of_player_dfs)
    cleaner_basic_def_player_stats_df = cleaner_list_of_player_dfs[0]
    cleaner_adv_def_player_stats_df = cleaner_list_of_player_dfs[1]

    cleaner_basic_def_player_stats_df.sort_values(['Tm', 'Tackles_Comb', 'Player'], ascending=[False, True, False], inplace=True)
    cleaner_adv_def_player_stats_df.sort_values(['Tm', 'Comb', 'Player'], ascending=[False, True, False], inplace=True)

    list_of_new_column_names =['Def Interceptions_Yds', 'Def Interceptions_TD', 'Def Interceptions_Lng', 'Def Interceptions_PD',
                               'Tackles_Solo', 'Tackles_Ast', 'Tackles_TFL', 'Fumbles_FR', 'Fumbles_Yds', 'Fumbles_TD', 'Fumbles_FF']

    new_adv_def_player_stats_df = defining_new_columns(list_of_new_column_names, cleaner_adv_def_player_stats_df)

    defensive_player_stats = joining_basic_stats_and_adv_stats(cleaner_basic_def_player_stats_df, new_adv_def_player_stats_df, list_of_new_column_names)

    return (defensive_player_stats)

def cleaning_kicking_player_stats(player_stats_df):

    player_stats_df['new_date'] = list(map(transforming_date, player_stats_df['date']))

    list_of_player_dfs = [player_stats_df]
    tms = [1,2]
    new_list_of_player_dfs, teams = defining_opposing_team_and_splitting_player_name(list_of_player_dfs, tms)

    newer_list_of_player_dfs = convert_values_to_appropriate_types(new_list_of_player_dfs)
    cleaner_player_df = newer_list_of_player_dfs[0]

    return (cleaner_player_df, teams)

def cleaning_return_player_stats(player_stats_df, teams):

    player_stats_df['new_date'] = list(map(transforming_date, player_stats_df['date']))

    list_of_player_dfs = [player_stats_df]
    new_list_of_player_dfs, tms = defining_opposing_team_and_splitting_player_name(list_of_player_dfs, teams)

    newer_list_of_player_dfs = convert_values_to_appropriate_types(new_list_of_player_dfs)
    cleaner_player_df = newer_list_of_player_dfs[0]

    return (cleaner_player_df)



