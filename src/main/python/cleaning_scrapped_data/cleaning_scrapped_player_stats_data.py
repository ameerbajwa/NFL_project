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

def cleaning_offensive_player_stats(basic_off_player_stats_df, adv_off_player_stats_df, type_of_offense):

    if (type_of_offense == 'passing'):

        list_of_new_column_names = ['TD', 'Int', 'Sk', 'Yds', 'Lng', 'Rate']

        for col in list_of_new_column_names:
            adv_off_player_stats_df[col] = 0

        passer_counter = 0
        for row_index in range(0, len(basic_off_player_stats_df)):
            if (basic_off_player_stats_df.loc[row_index, 'Cmp'] == '0'):
                continue
            else:
                for col in list_of_new_column_names:
                    adv_off_player_stats_df.loc[passer_counter, col] = basic_off_player_stats_df.loc[row_index, col]
                passer_counter += 1

        for col in adv_off_player_stats_df.columns:
            if ('.' in adv_off_player_stats_df.loc[0, col]):
                adv_off_player_stats_df[col] = list(map(converting_to_float, adv_off_player_stats_df[col]))
            else:
                adv_off_player_stats_df[col] = list(map(converting_to_int, adv_off_player_stats_df[col]))

        return (adv_off_player_stats_df)