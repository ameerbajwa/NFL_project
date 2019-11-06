from datetime import datetime

def converting_to_int(x):
    if (x == ''):
        return None
    elif (x == 'Rook'):
        return 0
    else:
        return int(x)

def cleaning_NFL_roster_data(team_roster_df):

    list_of_columns_to_convert_to_int = ['No.', 'Age', 'G', 'GS', 'Wt', 'Yrs']
    for col in list_of_columns_to_convert_to_int:
        team_roster_df[col] = list(map(converting_to_int, team_roster_df[col]))

    team_roster_df['BirthDate'] = list(map(lambda x: datetime.strptime(x, '%m/%d/%Y'), team_roster_df['BirthDate']))
    team_roster_df['Ht'] = list(map(lambda x: int(x.split('-')[0])*12 + int(x.split('-')[1]), team_roster_df['Ht']))
    team_roster_df['Salary'] = list(map(lambda x: None if (x == '') else int(x.split('$')[1].replace(',', '')), team_roster_df['Salary']))

    cleaned_team_roster_df = team_roster_df
    print ('Cleaned team roster pandas dataframe!')
    return (cleaned_team_roster_df)