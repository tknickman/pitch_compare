from pitch_compare.models.pitch_fx import PitchFXRepo
from pitch_compare.models.pitch_stats import PitchStatsRepo
from pyramid.view import view_config
import logging
import time


logger = logging.getLogger(__name__)


@view_config(route_name='pitch_data', request_method='GET', renderer='json')
def pitch_data(request):
    logger.info('route=/data/pitch')

    # init class
    pitch_data = PitchFXRepo()

    time_top = time.time()
    all_pitch_data = pitch_data.load_file(flat=True)
    time_bottom = time.time()
    logger.info('route=/data/pitch load_time=%s' % (time_bottom-time_top))

    return {'status': 'ok', 'pitch_data': all_pitch_data}


@view_config(route_name='pitcher_data', request_method='GET', renderer='json')
def pitcher_data(request):
    logger.info('route=/data/pitcher')

    # init class
    pitcher_data = PitchStatsRepo()

    time_top = time.time()
    all_pitcher_data = pitcher_data.load_file(flat=True)
    time_bottom = time.time()
    logger.info('route=/data/pitcher load_time=%s' % (time_bottom-time_top))

    return {'status': 'ok', 'pitch_data': all_pitcher_data}
