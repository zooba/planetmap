from datetime import datetime, timedelta
from collections.abc import Sequence

__all__ = ['daterange']

def _make_date(d):
    if isinstance(d, (int, float)):
        return datetime(int(d), 1, 1)

    if isinstance(d, tuple):
        if len(d) < 3:
            d += (1,) * (3 - len(d)) + (0, 0, 0)
        if len(d) < 6:
            d += (0,) * (6 - len(d))
        return datetime(*d)

    return d

def daterange(start, stop, step=None, step_months=None, step_years=None):
    '''Returns a sequence of dates between start (inclusive) and
    stop (exclusive).

    start and stop are `datetime` instances, a year integer, or a
    tuple of at least a year and optionally month, day, hour,
    minute and second.
    '''
    start = _make_date(start)
    stop = _make_date(stop)

    while start < stop:
        yield start
        if (step_years or step_months) is not None:
            year = start.year + (step_years or 0)
            month = start.month + (step_months or 0)
            if month > 12:
                month = 1
                year += 1

            start = datetime(
                year,
                month,
                start.day,
                start.hour,
                start.minute,
                start.second,
                start.microsecond,
                start.tzinfo
            )
        if step is not None:
            start += step

class SolarSystemMap:
    def __init__(self, width, height, date, downscale=4):
        self.data = [' '] * width * height
        self.width = width
        self.height = height
        self.date = date
        self.sx = width // downscale
        self.sy = height // downscale
        self.dx = width // 2
        self.dy = height // 2
        self.data[self.dy * self.width + self.dx] = 'O'

    def add_planet(self, initial, planet):
        x, y, _ = planet.position_at(self.date)
        self.data[(int(y * self.sy) + self.dy) * self.width +
                  int(x * self.sx) + self.dx] = initial

    def __str__(self):
        return '\n'.join(''.join(self.data[i:i+self.width])
                         for i in range(0, len(self.data), self.width))
