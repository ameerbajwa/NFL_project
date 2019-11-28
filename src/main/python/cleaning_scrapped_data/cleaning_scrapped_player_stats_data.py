
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

def convert_values_to_appropriate_types(list_of_player_stats_df):

    for df in list_of_player_stats_df:
        for col in df.columns[2:]:
            if ('%' in df[col].values):
                df[col] = list(map(lambda x: x.replace('%', '') if '%' in x else x, df[col]))
            else:
                continue

            if ('.' in df[col].values):
                df[col] = list(map(converting_to_float, df[col]))
            else:
                df[col] = list(map(converting_to_int, df[col]))

    return list_of_player_stats_df

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
    cleaner_list_of_player_dfs = convert_values_to_appropriate_types(list_of_player_dfs)
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
    cleaner_list_of_player_dfs = convert_values_to_appropriate_types(list_of_player_dfs)
    cleaner_basic_def_player_stats_df = cleaner_list_of_player_dfs[0]
    cleaner_adv_def_player_stats_df = cleaner_list_of_player_dfs[1]

    cleaner_basic_def_player_stats_df.sort_values(['Tm', 'Tackles_Comb', 'Player'], ascending=[False, True, False], inplace=True)
    cleaner_adv_def_player_stats_df.sort_values(['Tm', 'Comb', 'Player'], ascending=[False, True, False], inplace=True)

    # list_of_new_column_names =

def cleaning_special_team_player_stats(player_stats_df):

    list_of_player_dfs = convert_values_to_appropriate_types([player_stats_df])
    cleaner_player_df = list_of_player_dfs[0]



