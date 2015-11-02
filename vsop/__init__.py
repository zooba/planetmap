'''Provides calculations for the locations of the planets in
our solar system on a particular date.

Coordinates are derived from the VSOP87 data set and are
rectangular with the sun at the center (heliocentric).
'''

__author__ = "Steve Dower <steve.dower@microsoft.com>"
__version__ = "1.0.0"

from datetime import datetime
import math
import vsop.vsop87

class Planet:
    def __init__(self, vsop_code, vsop_index):
        X, Y, Z = {}, {}, {}
        for c, n, A, B, C in vsop.vsop87.read_data(vsop_code, vsop_index):
            data = [X, Y, Z][c]
            data.setdefault(n, []).append((A, B, C))
        self._X = X
        self._Y = Y
        self._Z = Z

    @staticmethod
    def _coord_at(data, t):
        res = 0.0
        for n, ABC in data.items():
            x = 0.0
            for A, B, C in ABC:
                x += A * math.cos(B + t * C)
            x *= t ** n
            res += x
        return res

    def position_at(self, day):
        '''Calculates the location of the planet at a particular day and time.

        Returns rectangular coordinates X, Y, Z.
        '''
        t = ((day - datetime(2000, 1, 1, 12)).total_seconds()) / (24 * 60 * 60 * 365250)
        X = self._coord_at(self._X, t)
        Y = self._coord_at(self._Y, t)
        Z = self._coord_at(self._Z, t)
        return X, Y, Z

