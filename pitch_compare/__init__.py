from pyramid.config import Configurator


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    # api routes
    config.add_route('pitch_data', '/data/pitch')
    config.add_route('pitcher_data', '/data/pitcher')

    # UI routes
    config.add_route('pitcher_ui', '/pitchers')
    config.add_route('dashboard_ui', '/dashboard')

    config.scan()
    return config.make_wsgi_app()
