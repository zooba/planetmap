"""
Routes and views for the bottle application.
"""

from azureml.services import service
from bottle import route, view, request
from datetime import datetime
from math import sqrt

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

    year = int(request.query.get('year') or 2015)
    month = int(request.query.get('month') or 1)
    day = int(request.query.get('day') or 1)
    locs = get_planet_locations(year, month, day, 0)

    max_x = max(abs(p[0]) for p in locs.values())
    max_y = max(abs(p[1]) for p in locs.values())
    max_xy = max(max_x, max_y)

    def t(x):
        p = x / (2.0 * max_xy)
        assert -0.5 <= p <= 0.5, p
        p = sqrt(p) if p > 0 else -sqrt(-p) if p < 0 else 0
        p += 0.5
        return 0 if p < 0 else 1 if p > 1 else p

    result = {k: (t(p[0]), t(p[1])) for k, p in locs.items()}
    result.update({k: request.query[k] for k in ['source', 'apikey']})
    result.update({'year': year, 'month': month, 'day': day})
    return result