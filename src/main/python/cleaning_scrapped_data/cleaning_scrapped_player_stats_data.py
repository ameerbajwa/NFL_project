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

def joining_basic_stats_and_adv_stats(basic_off_player_stats_df, adv_off_player_stats_df, list_of_new_column_names, identifier):
    counter = 0
    for row_index in range(0, len(basic_off_player_stats_df)):
        if (basic_off_player_stats_df.loc[row_index, identifier] == '0'):
            continue
        else:
            for col in list_of_new_column_names:
                adv_off_player_stats_df.loc[counter, col] = basic_off_player_stats_df.loc[row_index, col]
            counter += 1

    for col in adv_off_player_stats_df.columns:
        if ('.' in adv_off_player_stats_df.loc[0, col]):
            adv_off_player_stats_df[col] = list(map(converting_to_float, adv_off_player_stats_df[col]))
        else:
            adv_off_player_stats_df[col] = list(map(converting_to_int, adv_off_player_stats_df[col]))

    return (adv_off_player_stats_df)

def cleaning_offensive_player_stats(basic_off_player_stats_df, adv_off_player_stats_df, type_of_offense):

    if (type_of_offense == 'passing'):

        # ORDER PANDAS DATAFRAME BY TEAM NAME AND THEN PASSING YARDS AND THEN FILL IN MERGE THE TWO TABLES OF STATS USING
        #  THE COUNTER
        basic_off_player_stats_df.sort_values(['Tm', 'Passing_Yds', 'Player'], axis=1, inplace=True)
        adv_off_player_stats_df.sort_values(['Tm', 'Yds', 'Player'], axis=1, inplace=True)

        list_of_new_column_names = ['TD', 'Int', 'Sk', 'Yds', 'Lng', 'Rate']

        for col in list_of_new_column_names:
            adv_off_player_stats_df[col] = 0
        
        passing_stats_df = joining_basic_stats_and_adv_stats(basic_off_player_stats_df, adv_off_player_stats_df, list_of_new_column_names, 'Cmp')

        return (passing_stats_df)

    elif (type_of_offense == 'rushing'):

        # ORDER PANDAS DATAFRAME BY TEAM NAME AND THEN RUSHING ATTEMPTS AND THEN FILL IN MERGE THE TWO TABLES OF STATS USING
        #  THE COUNTER
        basic_off_player_stats_df.sort_values(['Tm', 'Rushing_Att', 'Player'], axis=1, inplace=True)
        adv_off_player_stats_df.sort_values(['Tm', 'Att', 'Player'], axis=1, inplace=True)

    elif (type_of_offense == 'receiving'):

        basic_off_player_stats_df.sort_values(['Tm', 'Receiving_Tgt', 'Player'], axis=1, inplace=True)
        adv_off_player_stats_df.sort_values(['Tm', 'Tgt', 'Player'], axis=1, inplace=True)



