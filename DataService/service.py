from azureml.services import publish
from datetime import datetime

# If we've published, we need to add the package to sys.path
# so the following import succeeds.
import os, sys
deployed_package = os.path.abspath(r'Script Bundle\vsop.zip')
if os.path.isfile(deployed_package):
    sys.path.append(deployed_package)

from vsop.planets import *

@publish('45c8640925234741b3ebc29a8a03cbd7', '7e3b512fa4d24df88772bb4652528222',
         files=[('vsop.zip', None)])
def get_all_planets(year, month, day, hour):
    t = datetime(year, month, day, hour)
    return {
        "mercury": Mercury.position_at(t),
        "venus": Venus.position_at(t),
        "earth": Earth.position_at(t),
        "mars": Mars.position_at(t),
        "jupiter": Jupiter.position_at(t),
        "saturn": Saturn.position_at(t),
        "uranus": Uranus.position_at(t),
        "neptune": Neptune.position_at(t),
    }

if __name__ == '__main__':
    # If we're running directly, we've published the service and
    # want to wait for it to finish, view the URL and the key.
    from util import wait_for_service
    print get_all_planets.service.url
    print get_all_planets.service.api_key
    wait_for_service(get_all_planets, 2010, 1, 1, 0)
