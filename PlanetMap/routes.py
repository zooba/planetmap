"""
Routes and views for the bottle application.
"""

from azureml.services import service
from bottle import route, view, request, abort, redirect
from datetime import datetime, timedelta
from math import sqrt

@route('/')
@view('index')
def home():
    """Renders the home page."""
    return {}

def get_date(year, month, day):
    if year < 1900: year = 1900
    if month < 1: month = 1
    if day < 1: day = 1
    while month > 12:
        month -= 12
        year += 1
    while day > 0:
        try:
            return datetime(year, month, day)
        except ValueError:
            day -= 1
    raise ValueError('Cannot calculate date')

def nextyear(dt):
    y, m, d = dt.year, dt.month, dt.day
    y += 1
    while d > 0:
        try:
            return datetime(y, m, d)
        except ValueError:
            d -= 1
    return None

def nextmonth(dt):
    y, m, d = dt.year, dt.month, dt.day
    m += 1
    if m > 12:
        m = 1
        y =+ 1
    while d > 0:
        try:
            return datetime(y, m, d)
        except ValueError:
            d -= 1
    return None

@route('/map')
@view('map')
def view_map():
    try:
        source = request.query['source']
        apikey = request.query['apikey']
    except KeyError:
        redirect('/')
        return

    @service(source, apikey.replace('-', '+'))
    def get_planet_locations(year, month, day):
        '''Gets X, Y, Z coordinates for the planets in
        our solar system on a particular day.
        '''
        # No implementation is required, because we will
        # invoke the function on the server.
        pass

    # Get the date from URL parametetrs
    try:
        dt = get_date(
            year=int(request.query.get('year') or 2015),
            month=int(request.query.get('month') or 1),
            day=int(request.query.get('day') or 1)
        )
    except ValueError:
        abort(400, "Cannot evaluate specified date")
        return

    # Get the planet locations from the web service
    locs = get_planet_locations(dt.year, dt.month, dt.day)

    # We want to normalize the resulting values in two ways:
    #
    # 1. Scale the range to [0.0, 1.0]
    # 2. Adjust the placement for a more even distribution.
    #
    # The first allows the template to position each planet
    # by simply multiplying the coordinate by the size of
    # the container.
    #
    # The second is because Neptune is actually a really
    # long way away from the sun. When we scale linearly,
    # the closest planets are so close together that it
    # does not look very interesting. By taking the square
    # root of the value, we spread out the inner planets
    # and bring the outer planets closer together. It is
    # astronomically inaccurate, but it looks nicer.
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

    # Update the result with the original query parameters,
    # so that we can generate form elements or URLs.
    result.update({
        'source': request.query['source'],
        'apikey': request.query['apikey'].replace('+', '-'),
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'tomorrow': dt + timedelta(days=1),
        'nextweek': dt + timedelta(days=7),
        'nextmonth': nextmonth(dt),
        'nextyear': nextyear(dt),
    })

    return result