import api_key

import requests
import json
from termcolor import colored

event_key = input("Tba key: ")

api_url = f'event/{event_key}/matches/simple'
full_url = f'https://www.thebluealliance.com/api/v3/{api_url}'
request = requests.get(full_url, headers=api_key.request_headers)
matches = request.json()

for match in matches:
    blue = match["alliances"]["blue"]["team_keys"]
    red = match["alliances"]["red"]["team_keys"]

    print(colored(red, 'red'), colored(blue, 'blue'))
