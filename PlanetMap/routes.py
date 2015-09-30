"""
Routes and views for the bottle application.
"""

from azureml.services import service
from bottle import route, view, request
from datetime import datetime

@route('/')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/map')
@view('map')
def view_map():
    @service(request.query['source'], request.query['apikey'])
    def get_planet_locations(year, month, day, hour):
        pass

    locs = get_planet_locations.map(
        [2015, 2015, 2015, 2015],
        [   1,    2,    3,    4],
        [   1,    1,    1,    1],
        [   0,    0,    0,    0],
    )

    return locs[0]
