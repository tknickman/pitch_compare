from pitch_compare.enums .data import DataFiles
from pkg_resources import resource_filename
import csv


computed_data_cache = {
    'flat': None,
    'hierarchical': None
}


class PitchStatsRepo(object):

    def __init__(self, data_file=DataFiles.pitch_stats):
        self.data_file = data_file

    def get_file_location(self):
        return resource_filename('pitch_compare', self.data_file)

    def get_player_by_id(self, player_id):
        pitcher_data = self.load_file()
        return pitcher_data[player_id]['name']

    def load_file(self, flat=False):
        """
        Reads the given file into the following format:

        {
            pitcher_id: {
                organization: {
                    year: [pitcher_data]
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

            with open(file_path, 'rw') as fin:
                csv_reader = csv.DictReader(fin)

                if flat:
                    pitcher_data = []
                else:
                    pitcher_data = {}

                for row in csv_reader:

                    # extract unique data
                    pitcher_id = row['pitcher_id']
                    year = row['Year']
                    name = row['Name']
                    organization = row['org']

                    # clean percentage keys
                    row['GB'] = row['GB.']
                    row['LD'] = row['LD.']
                    row['FB'] = row['FB.']

                    if flat:
                        pitcher_data.append(row)
                    else:
                        # build player dict
                        org_dict = pitcher_data.setdefault(
                            pitcher_id, {'name': name}
                        )
                        year_dict = org_dict.setdefault(organization, {})
                        year_dict.setdefault(year, []).append(row)

            computed_data_cache[cache_key] = pitcher_data

        return pitcher_data

























