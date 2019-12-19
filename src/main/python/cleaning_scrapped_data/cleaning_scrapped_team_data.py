from datetime import datetime

def converting_to_int(x):
    if (x == '' or x == 'Rook'):
        return 0
    else:
        return int(x)

def cleaning_NFL_roster_data(team_roster_df):

    list_of_columns_to_convert_to_int = ['No.', 'Age', 'G', 'GS', 'Wt', 'Yrs']
    for col in list_of_columns_to_convert_to_int:
        team_roster_df[col] = list(map(converting_to_int, team_roster_df[col]))

    team_roster_df['BirthDate'] = list(map(lambda x: datetime.strptime(x, '%m/%d/%Y'), team_roster_df['BirthDate']))
    team_roster_df['Ht'] = list(map(lambda x: int(x.split('-')[0])*12 + int(x.split('-')[1]), team_roster_df['Ht']))
    team_roster_df['Salary'] = list(map(lambda x: 0 if (x == '') else int(x.split('$')[1].replace(',', '')), team_roster_df['Salary']))

    cleaned_team_roster_df = team_roster_df
    print ('Cleaned team roster pandas dataframe!')
    return (cleaned_team_roster_df)

def cleaning_NFL_injury_report(injury_roster_df):
    return injury_roster_df

# NO CLEANING OF THE NFL OVERALL TEAM DATA NEEDED

# def cleaning_NFL_team_off_stats(team_off_stats_df):
#     return team_off_stats_df
#
# def cleaning_NFL_team_def_stats(team_def_stats_df):
#     return team_def_stats_df