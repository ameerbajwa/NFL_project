from datetime import datetime, timedelta
from time import strptime


def converting_to_int(x):
    if (x == '' or x == 'Rook'):
        return 0
    else:
        return int(x)


dates = []


def creating_new_date(date):
    if (date != ''):
        month_number = str(strptime(date.split(' ')[0][:3], '%b').tm_mon)
        day_number = str(date.split(' ')[1])

        if (len(month_number) == 1):
            month_number = '0' + month_number

        if (len(day_number) == 1):
            day_number = '0' + day_number

        dates.append(month_number + '/' + day_number + '/2019')
        return (month_number + '/' + day_number + '/2019')
    else:
        raw_bye_date = datetime.strptime(dates[-1], '%m/%d/%Y')
        bye_date = raw_bye_date + timedelta(days=7)
        return (bye_date.strftime('%m/%d/%Y'))


def cleaning_body_part_info(body_part_info):
    print (body_part_info)
    if (body_part_info == 'NA' or body_part_info == float('NaN')):
        return 'NA'
    else:
        if (body_part_info.split(':')[-1] == ''):
            return 'NA'
        else:
            return body_part_info.split(':')[-1][1:]


def cleaning_NFL_roster_data(team_roster_df):

    list_of_columns_to_convert_to_int = ['No.', 'Age', 'G', 'GS', 'Wt', 'Yrs']
    for col in list_of_columns_to_convert_to_int:
        team_roster_df[col] = list(map(converting_to_int, team_roster_df[col]))

    team_roster_df['BirthDate'] = list(map(lambda x: datetime.strptime(x, '%m/%d/%Y'), team_roster_df['BirthDate']))
    team_roster_df['Ht'] = list(map(lambda x: int(x.split('-')[0])*12 + int(x.split('-')[1]), team_roster_df['Ht']))
    team_roster_df['Salary'] = list(map(lambda x: 0 if (x == '') else int(x.split('$')[1].replace(',', '')), team_roster_df['Salary']))

    cleaned_team_roster_df = team_roster_df
    print ('Cleaned team roster pandas dataframe!')
    return cleaned_team_roster_df


def cleaning_NFL_injury_report(injury_roster_df):

    for i in range(1,int((len(injury_roster_df)-2)/2)):
        injury_roster_df['body_part_'+str(i)] = list(map(cleaning_body_part_info, injury_roster_df['body_part_'+str(i)]))

    return injury_roster_df


def cleaning_NFL_team_schedule(team_schedule_df):
    team_schedule_df.drop('Boxscore', axis=1, inplace=True)
    team_schedule_df['new_date'] = list(map(creating_new_date, team_schedule_df['Date']))
    team_schedule_df['date'] = list(map(lambda x: datetime.strptime(x, '%m/%d/%Y'), team_schedule_df['new_date']))
    team_schedule_df['month_of_game'] = list(map(lambda x: x.split(' ')[0] if x != '' else 'NA', team_schedule_df['Date']))
    team_schedule_df['day_of_game'] = list(map(lambda x: int(x.split(' ')[1]) if x != '' else 0, team_schedule_df['Date']))
    team_schedule_df['hour_of_game'] = list(map(lambda x: int(x.split(' ')[0].split(':')[0]) if x != '' else 0, team_schedule_df['Time_Game_Starts']))
    team_schedule_df['minute_of_game'] = list(map(lambda x: int(x.split(' ')[0].split(':')[1][:2]) if x != '' else 0, team_schedule_df['Time_Game_Starts']))
    team_schedule_df['Won/Loss'] = list(map(lambda x: 'NA' if x == '' else x, team_schedule_df['Won/Loss']))
    team_schedule_df['OT'] = list(map(lambda x: 'NA' if x == '' else x, team_schedule_df['OT']))
    team_schedule_df['Home/Away'] = list(map(lambda x: 'Away' if x == '@' else 'Home', team_schedule_df['Home/Away']))

    dates = []
    return team_schedule_df

# NO CLEANING OF THE NFL OVERALL TEAM DATA NEEDED

# def cleaning_NFL_team_off_stats(team_off_stats_df):
#     return team_off_stats_df
#
# def cleaning_NFL_team_def_stats(team_def_stats_df):
#     return team_def_stats_df