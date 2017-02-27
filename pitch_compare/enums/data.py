
class DataFiles(object):
    pitch_fx = 'data/Pitchfx.csv'
    pitch_stats = 'data/Pitching_Statistics.csv'


class PitchData(object):

    all = {
        'FA': 'Fastball',
        'FF': 'Splitter',
        'FT': 'Cutter',
        'SI': 'Pitch Out',
        'FS': 'Curveball',
        'FC': 'Four-Seam Fastball',
        'FO/PO': 'Two-seam Fastball',
        'CU/CB': 'Sinker',
        'KC': 'Knuckle-curve',
        'EP': 'Eephus',
        'CH': 'Changeup',
        'SC': 'Screwball',
        'KN': 'Knuckleball',
        'AB': 'Auto. Ball',
        'UN/XX': 'Unidentified',
    }


class DataData(object):

    day_array = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]


class PitcherStats(object):

    all = {
        'pitcher_id': 'Unique pitcher identifier',
        'Name': 'Name',
        'birth_date': 'Date of birth',
        'org': 'Organization',
        'League': 'League',
        'G': 'Games played',
        'GS': 'Games started',
        'TBF': 'Batters faced',
        'Year': 'Year',
        'X1B': 'Singles',
        'X2B': 'Doubles',
        'X3B': 'Triples',
        'HR': 'Home Runs',
        'BB': 'Unintentional walks',
        'IBB': 'Intentional walks',
        'HBP': 'Pitches that hit batter',
        'SO': 'Strikeouts',
        'GB': 'Percentage of BIP that are GB',
        'LD': 'Percentage of BIP that are LD',
        'FB': 'Percentage of BIP that are FB',
        'BB': 'Walk Percentage',
        'ERA': 'Earned Run Average',
        'FIP': 'Fielding Independent Pitching',
        'rWAR': 'Wins Above Replacement'
    }


class TeamData(object):

    all = {
        'ana': {
            'city': 'Los Angeles',
            'name': 'Angels',
            'league': 'American',
            'division': 'West'
        },
        'tex': {
            'city': 'Texas',
            'name': 'Rangers',
            'league': 'American',
            'division': 'West'
        },
        'sea': {
            'city': 'Seattle',
            'name': 'Mariners',
            'league': 'American',
            'division': 'West'
        },
        'ari': {
            'city': 'Arizona',
            'name': 'Diamondbacks',
            'league': 'National',
            'division': 'West'
        },
        'pit': {
            'city': 'Pittsburgh',
            'name': 'Pirates',
            'league': 'National',
            'division': 'Central'
        },
        'cha': {
            'city': 'Chicago',
            'name': 'White Sox',
            'league': 'American',
            'division': 'Central'
        },
        'mil': {
            'city': 'Milwaukee',
            'name': 'Brewers',
            'league': 'National',
            'division': 'West'
        },
        'min': {
            'city': 'Minnesota',
            'name': 'Twins',
            'league': 'American',
            'division': 'Central'
        },
        'tor': {
            'city': 'Toronto',
            'name': 'Blue Jays',
            'league': 'American',
            'division': 'East'
        },
        'cle': {
            'city': 'Cleveland',
            'name': 'Indians',
            'league': 'American',
            'division': 'Central'
        },
        'oak': {
            'city': 'Oakland',
            'name': 'Athletics',
            'league': 'American',
            'division': 'West'
        },
        'chn': {
            'city': 'Chicago',
            'name': 'Cubs',
            'league': 'National',
            'division': 'Central'
        },
        'hou': {
            'city': 'Houston',
            'name': 'Astros',
            'league': 'American',
            'division': 'West'
        },
        'nyn': {
            'city': 'New York',
            'name': 'Mets',
            'league': 'National',
            'division': 'East'
        },
        'nya': {
            'city': 'New York',
            'name': 'Yankees',
            'league': 'American',
            'division': 'East'
        },
        'was': {
            'city': 'Washington',
            'name': 'Nationals',
            'league': 'National',
            'division': 'East'
        },
        'phi': {
            'city': 'Philadelphia',
            'name': 'Phillies',
            'league': 'National',
            'division': 'East'
        },
        'kca': {
            'city': 'Kansas City',
            'name': 'Royals',
            'league': 'American',
            'division': 'Central'
        },
        'sfn': {
            'city': 'San Francisco',
            'name': 'Giants',
            'league': 'National',
            'division': 'West'
        },
        'tba': {
            'city': 'Tampa Bay',
            'name': 'Rays',
            'league': 'American',
            'division': 'Central'
        },
        'sdn': {
            'city': 'San Diego',
            'name': 'Padres',
            'league': 'National',
            'division': 'West'
        },
        'atl': {
            'city': 'Atlanta',
            'name': 'Braves',
            'league': 'National',
            'division': 'East'
        },
        'bos': {
            'city': 'Boston',
            'name': 'Red Sox',
            'league': 'American',
            'division': 'East'
        },
        'det': {
            'city': 'Detroit',
            'name': 'Tigers',
            'league': 'American',
            'division': 'Central'
        },
        'cin': {
            'city': 'Cincinnati',
            'name': 'Reds',
            'league': 'National',
            'division': 'Central'
        },
        'sln': {
            'city': 'St. Louis',
            'name': 'Cardinals',
            'league': 'National',
            'division': 'Central'
        },
        'bal': {
            'city': 'Baltimore',
            'name': 'Orioles',
            'league': 'American',
            'division': 'East'
        }
    }
