from pitch_compare.enums .data import TeamData, PitchData, DataData
from datetime import datetime


# game util functions
def get_game_date(date_string):
    datetime_object = datetime.strptime(date_string, '%d-%b-%y')
    return DataData.day_array[datetime_object.weekday()]


def get_game_name(game_id):
    date_data = game_id[:10]
    team_data = game_id[11:].split('-')
    team1 = team_data[0][:-3]
    team2 = team_data[1][:-3]
    game_num = int(team_data[2])

    team1_data = TeamData.all[team1]
    team2_data = TeamData.all[team2]
    team1_name = '%s %s' % (team1_data['city'], team1_data['name'])
    team2_name = '%s %s' % (team2_data['city'], team2_data['name'])

    title = '%s vs. %s (game: %s) - %s' % (
        team1_name,
        team2_name,
        game_num,
        date_data
    )

    return title


def get_game_opponent(game_id):
    team_data = game_id[11:].split('-')

    team1 = team_data[0][:-3]
    team2 = team_data[1][:-3]

    opponent = team1 if team2 == 'bal' else team2
    opponent_data = TeamData.all[opponent]

    full_name = '%s %s' % (opponent_data['city'], opponent_data['name'])
    return full_name


def get_game_label(input_string):
    if input_string != '':
        clean_event_result = ' '.join(
            word.title() for word in input_string.split('_')
        )
    else:
        clean_event_result = 'None'
    return clean_event_result


# pitch util functions
def get_pitch_type(pitch_code):
    return PitchData.all.get(pitch_code, 'None')


def get_pitch_call(event_type):
    if event_type == 'called_strike' or event_type == 'swinging_strike':
        event_ball_strike = 'Strike'
    elif event_type == 'ball':
        event_ball_strike = 'Ball'
    else:
        event_ball_strike = 'Other'

    return event_ball_strike
