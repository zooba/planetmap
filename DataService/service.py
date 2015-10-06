from datetime import datetime

#region Boilerplate for deployed service
# If we've published, we need to add the package to sys.path
# so the following import succeeds.
import os, sys
deployed_package = os.path.abspath(r'Script Bundle\vsop.zip')
if os.path.isfile(deployed_package):
    sys.path.append(deployed_package)

#endregion

from vsop.planets import *


def get_all_planets(year, month, day):
    # TODO: Handle ValueError for invalid dates
    t = datetime(year, month, day)
    
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
    # If we're running directly, we want to publish the service and
    # wait for it to finish, then display the URL and the key.

    # TODO: Refactor into own function
    from azureml.services import publish
    from util import wait_for_service
    import webbrowser
    
    print 'You will require an Azure Machine Learning workspace to deploy the service.'
    print
    if raw_input('Create a free workspace now? [y/N] ').startswith('y'):
        print 'Opening web browser. Log in with a Microsoft Account and access your workspace ID'
        print 'and authorization token from Settings.'
        webbrowser.open('https://studio.azureml.net/Home')
    
    workspace_id = raw_input('Please enter your workspace id:')
    auth_token = raw_input('Please enter your authorization token:')
    
    service = publish(get_all_planets, workspace_id, auth_token, files=[('vsop.zip', None)])
    print service.url
    print service.api_key
    wait_for_service(service, 2010, 1, 1)
    print "Press enter to close . . ."
    raw_input()
