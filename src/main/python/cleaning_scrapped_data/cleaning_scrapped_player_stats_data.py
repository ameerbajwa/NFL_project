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

def convert_values_to_appropriate_types(basic_player_stats_df, adv_player_stats_df):

    for df in [basic_player_stats_df, adv_player_stats_df]:
        for col in df.columns[2:]:
            print (col)
            if ('%' in df.loc[0, col]):
                df[col] = list(map(lambda x: x.replace('%', ''), df[col]))

            if ('.' in df.loc[0, col]):
                df[col] = list(map(lambda x: 0.0 if '' else float(x), df[col]))
            else:
                df[col] = list(map(lambda x: 0 if '' else int(x), df[col]))
            print ('conversion complete')

    return (basic_player_stats_df, adv_player_stats_df)

def joining_basic_stats_and_adv_stats(basic_player_stats_df, adv_player_stats_df, list_of_new_column_names, identifier):
    counter = 0
    for row_index in range(0, len(basic_player_stats_df)):
        if (basic_player_stats_df.loc[row_index, identifier] == 0):
            continue
        else:
            for col in list_of_new_column_names:
                adv_player_stats_df.loc[counter, col] = basic_player_stats_df.loc[row_index, col]
            counter += 1

    return (adv_player_stats_df)

def cleaning_offensive_player_stats(basic_off_player_stats_df, adv_off_player_stats_df, type_of_offense):

    if (type_of_offense == 'passing'):

        # ORDER PANDAS DATAFRAME BY TEAM NAME AND THEN PASSING YARDS AND THEN FILL IN MERGE THE TWO TABLES OF STATS USING
        #  THE COUNTER

        cleaner_basic_off_player_stats_df, cleaner_adv_off_player_stats_df = convert_values_to_appropriate_types(basic_off_player_stats_df, adv_off_player_stats_df)

        cleaner_basic_off_player_stats_df.sort_values(by=['Tm', 'Passing_Yds', 'Player'], ascending=[False, True, False], inplace=True)
        cleaner_adv_off_player_stats_df.sort_values(by=['Tm', 'Yds', 'Player'], ascending=[False, True, False], inplace=True)

        list_of_new_column_names = ['Passing_TD', 'Passing_Int', 'Passing_sacked_Yds', 'Passing_Lng', 'Passing_Rate']

        for col in list_of_new_column_names:
            adv_off_player_stats_df[col] = 0

        passing_stats_df = joining_basic_stats_and_adv_stats(cleaner_basic_off_player_stats_df, cleaner_adv_off_player_stats_df, list_of_new_column_names, 'Cmp')

        return (passing_stats_df)

    elif (type_of_offense == 'rushing'):

        # ORDER PANDAS DATAFRAME BY TEAM NAME AND THEN RUSHING ATTEMPTS AND THEN FILL IN MERGE THE TWO TABLES OF STATS USING
        #  THE COUNTER
        basic_off_player_stats_df.sort_values(['Tm', 'Rushing_Att', 'Player'], axis=1, inplace=True)
        adv_off_player_stats_df.sort_values(['Tm', 'Att', 'Player'], axis=1, inplace=True)

    elif (type_of_offense == 'receiving'):

        basic_off_player_stats_df.sort_values(['Tm', 'Receiving_Tgt', 'Player'], axis=1, inplace=True)
        adv_off_player_stats_df.sort_values(['Tm', 'Tgt', 'Player'], axis=1, inplace=True)



