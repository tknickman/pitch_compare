from pitch_compare.models.pitch_stats import PitchStatsRepo
from pyramid.view import view_config
import logging
import time


logger = logging.getLogger(__name__)


@view_config(
    route_name='dashboard_ui',
    renderer='templates/dashboard.jinja2'
)
def dashboard_ui(request):

    logger.info('route=/dashboard')

    return {'status': 'ok'}


@view_config(
    route_name='pitcher_ui',
    renderer='templates/pitchers.jinja2'
)
def pitcher_ui(request):

    logger.info('route=/pitchers')

    # init class
    pitcher_data = PitchStatsRepo()

    time_top = time.time()
    all_pitcher_data = pitcher_data.load_file(flat=True)
    time_bottom = time.time()
    logger.info('route=/data/pitcher load_time=%s' % (time_bottom-time_top))

    return {'status': 'ok', 'pitcher_data': all_pitcher_data}






























