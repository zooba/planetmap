'''Provides a set of singleton planets for our solar system.
'''

__author__ = "Steve Dower <steve.dower@microsoft.com>"
__version__ = "1.0.0"

from vsop import Planet

Mercury = Planet('mer', 1)
Venus = Planet('ven', 2)
Earth = Planet('ear', 3)
Mars = Planet('mar', 4)
Jupiter = Planet('jup', 5)
Saturn = Planet('sat', 6)
Uranus = Planet('ura', 7)
Neptune = Planet('nep', 8)
