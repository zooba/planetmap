'''Makes many calls into the service method.

This script is intended to be profiled.
'''

from datetime import timedelta
from service import get_all_planets
from vsop.util import daterange


if __name__ == '__main__':
    for d in daterange(
        start=(2012, 1, 1),
        stop=(2013, 1, 1),
        step=timedelta(days=1),
    ):
        get_all_planets(d.year, d.month, d.day)
