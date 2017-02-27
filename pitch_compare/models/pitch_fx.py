from pitch_compare.models.pitch_stats import PitchStatsRepo
from pitch_compare.enums .data import DataFiles
from pkg_resources import resource_filename
from pitch_compare.utils.pitch_fx import (
    get_game_date,
    get_game_opponent,
    get_game_name,
    get_pitch_call,
    get_game_label,
    get_pitch_type
)
import csv


computed_data_cache = {
    'flat': None,
    'hierarchical': None
}


class PitchFXRepo(object):

    def __init__(self, data_file=DataFiles.pitch_fx):
        self.data_file = data_file

    def get_file_location(self):
        return resource_filename('pitch_compare', self.data_file)

    def load_file(self, flat=False):
        """
        Reads the given file into the following format:

        {
            player_id: {
                game_id: {
                    inning: [pitch_data]
                }
            }
        }

        :return:
        """

        # use a dict as a cache for the pitch data so it only has to be
        # loaded once
        cache_key = 'flat' if flat else 'hierarchical'
        if computed_data_cache[cache_key]:
            return computed_data_cache[cache_key]
        else:
            file_path = self.get_file_location()
            pitch_stats = PitchStatsRepo()

            with open(file_path, 'rw') as fin:
                csv_reader = csv.DictReader(fin)

                if flat:
                    pitch_data = []
                else:
                    pitch_data = {}
                for row in csv_reader:

                    # add day of the week
                    row['game_day'] = get_game_date(row['game_date'])

                    # add opponent name
                    row['opponent'] = get_game_opponent(row['game_id'])

                    # add player name
                    row['player_name'] = pitch_stats.get_player_by_id(
                        row['pitcher_id']
                    )

                    # add game name
                    row['game_display_name'] = get_game_name(row['game_id'])

                    # add ball / strike / other trinary
                    row['ball_strike_other'] = get_pitch_call(row['event_type'])

                    # update display data
                    row['event_result'] = get_game_label(row['event_result'])
                    row['event_type'] = get_game_label(row['event_type'])
                    row['pitch_type'] = get_pitch_type(row['pitch_type'])

                    if flat:
                        pitch_data.append(row)
                    else:
                        # extract unique data
                        pitcher_id = row['pitcher_id']
                        game_id = row['pitcher_id']
                        inning = row['inning']

                        # build player dict
                        game_dict = pitch_data.setdefault(pitcher_id, {})
                        inning_dict = game_dict.setdefault(game_id, {})
                        inning_dict.setdefault(inning, []).append(row)

            # load data into cache
            computed_data_cache[cache_key] = pitch_data

        return pitch_data
