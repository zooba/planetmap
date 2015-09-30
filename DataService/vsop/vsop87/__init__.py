'''Provides access to the VSOP87 data.

Data files obtained from ftp://ftp.imcce.fr/pub/ephem/planets/vsop87/
'''

import pkgutil
import re

def read_data(planet, body_index, series='A'):
    '''Returns a sequence of values for the specified planet.

    `planet` is the three letter code for the planet.
    
    `body_index` is the index used in the files. It is used for
    validation.

    `series` is the VSOP87 series to use.

    Returns a sequence of tuples containing:
        0, 1 or 2 for X, Y or Z coordinate
        n: time power factor
        A: cosine coefficient
        B: cosine term offset
        C: cosine term coefficient

    Each term can be calculated as A*cos(B+C*t), summed over every A B and C
    for a particular n, then multiplied by t**n. Each term is summed over
    every value of n for the given coordinate.

    See http://neoprogrammics.com/vsop87/index.html for more information.
    '''
    first_version = None

    data = pkgutil.get_data("vsop.vsop87", "VSOP87{}.{}".format(series, planet))
    if not data:
        raise ValueError("No data for {} in series {}".format(planet, series))

    for line in data.splitlines():
        if line.lstrip().startswith(b'VSOP'):
            continue
        
        # Some columns are adjacent like "8-12" and need to be
        # split into '8', '-12'.
        bits = [b for b in re.split(br'\s*(-?[\d\.]+)', line) if b]

        version, body, coord, n = [int(c) - int(b'0'[0]) for c in bits[0]]
        if first_version is None:
            first_version = version
        elif first_version != version:
            raise ValueError("Source data contains mixed versions")

        if body != body_index:
            continue

        S, K, A, B, C = (float(b) for b in bits[14:19])
        yield coord-1, n, A, B, C
